import requests

CORE = "http://core.webkurier"

def send_telemetry(data):
    try:
        requests.post(f"{CORE}/api/telemetry", json=data, timeout=1)
    except:
        print("LTE failed → fallback LoRa")

def send_command(cmd):
    requests.post(f"{CORE}/api/autopilot", json={"cmd": cmd})