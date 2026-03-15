import json
import os

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from engine.autopilot.models.mission_schema import MissionBuildRequest, MissionPlan
from engine.autopilot.services.mission_demo_live import (
    build_simple_survey_grid,
    validate_mission_plan,
)
from engine.autopilot.mavlink.mavlink_bridge import MavlinkBridge
from engine.autopilot.mavlink.mission_uploader import upload_live, MissionUploadError

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MODE_PATH = os.path.join(BASE_DIR, "config", "mode.json")
TELEMETRY_PATH = os.path.join(BASE_DIR, "config", "telemetry_config.json")


def load_json(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def upload_demo(plan: MissionPlan):
    return {
        "status": "demo_saved",
        "message": "DEMO mode active. Mission not sent to Pixhawk.",
        "mission_name": plan.name,
        "items_count": len(plan.items)
    }


mode_cfg = load_json(MODE_PATH)
telemetry_cfg = load_json(TELEMETRY_PATH)

bridge = None
if mode_cfg.get("mode", "DEMO").upper() == "LIVE" and mode_cfg.get("mavlink_enabled", False):
    bridge = MavlinkBridge(
        connection_string=telemetry_cfg["connection_string"],
        baudrate=telemetry_cfg.get("baudrate", 57600),
    )

app = FastAPI(title="WebKurier DroneHybrid Mission API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_event():
    if bridge is not None:
        bridge.start()


@app.get("/api/autopilot/status")
def status():
    mode = mode_cfg.get("mode", "DEMO").upper()
    fc = "not_connected"

    if bridge is not None:
        latest = bridge.get_latest()
        fc = "connected" if latest.get("link_alive") else "not_connected"

    return {
        "mode": mode,
        "api": "online",
        "fc": fc,
        "connection_string": telemetry_cfg.get("connection_string")
    }


@app.get("/api/autopilot/telemetry/live")
def telemetry_live():
    if bridge is None:
        return {
            "link_alive": False,
            "flight_mode": None,
            "armed": None,
            "gps_fix_type": None,
            "satellites_visible": None,
            "battery_remaining_pct": None,
            "voltage_v": None,
            "lat": None,
            "lon": None,
            "altitude_m": None,
            "ground_speed_mps": None,
            "heading_deg": None,
            "current_mission_seq": None,
            "climb_rate_mps": None,
            "home_lat": None,
            "home_lon": None,
            "home_distance_m": None,
            "radio_rssi": None,
            "link_quality_pct": None,
            "ekf_status": None,
            "failsafe_state": None,
            "last_message_type": None
        }
    return bridge.get_latest()


@app.post("/api/autopilot/mission/build", response_model=MissionPlan)
def mission_build(req: MissionBuildRequest):
    return build_simple_survey_grid(req)


@app.post("/api/autopilot/mission/validate")
def mission_validate(plan: MissionPlan):
    return validate_mission_plan(plan)


@app.post("/api/autopilot/mission/upload")
def mission_upload(plan: MissionPlan):
    validation = validate_mission_plan(plan)
    if not validation["valid"]:
        raise HTTPException(status_code=400, detail=validation)

    mode = mode_cfg.get("mode", "DEMO").upper()

    if mode == "DEMO":
        result = upload_demo(plan)
    elif mode == "LIVE":
        if bridge is None:
            raise HTTPException(status_code=500, detail="LIVE bridge is not initialized")
        master = bridge.get_master()
        try:
            result = upload_live(plan, master)
        except MissionUploadError as exc:
            raise HTTPException(status_code=500, detail=str(exc))
    else:
        raise HTTPException(status_code=500, detail=f"unsupported mode: {mode}")

    return {
        **result,
        "validation": validation
    }