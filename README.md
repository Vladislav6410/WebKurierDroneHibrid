
# WebKurierDroneHibrid — Unified Transport Intelligence for UAV & UGV Platforms

**WebKurierDroneHibrid** is the dedicated domain hub for all aerial and ground mobility intelligence in the WebKurier ecosystem.  
It integrates UAV flight control, UGV navigation, geodesy, photogrammetry, mission planning, 3D terrain analysis, solar PV planning, telemetry, safety checks, and regulatory compliance into one cohesive engine.

This repository powers:
- Drone autopilot (manual/auto/geodesy/acro/swarm)
- Ground-vehicle autopilot (future extension)
- Geodesy/photogrammetry processing
- GSD and overlap calculation pipelines
- ODM-based 3D reconstruction workflows
- Mission builder and route generator
- PV planner, 3D terrain engine, shadow simulation
- Full telemetry stack (batteries, sensors, warnings)
- UAS zone compliance and Remote-ID validation
- High-fidelity geo-report generator (PDF, LAS, GeoTIFF)

VehicleHub is the **transport brain** of the entire WebKurier system.

---

# 1. Role in the Ecosystem (Hierarchy Level 2)

```text
Level 0 — WebKurierHybrid (orchestrator)
Level 1 — WebKurierCore (user gateway)
Level 2 — WebKurierDroneHibrid (THIS REPOSITORY)
Level 2 — WebKurierPhoneCore
Level 2 — WebKurierChain
Level 2 — WebKurierSecurity
Level 3 — Mobile Apps
Level 4 — Public Site
Level 5 — Future/X Labs

DroneHibrid is the primary executor for all mobility, geospatial, and mission-related tasks.

Routing example:

User → WebKurierCore Terminal
     → WebKurierDroneHibrid (autopilot/geodesy/missions)
     → Core returns response to user


⸻

2. Repository Structure (High-Level)

WebKurierDroneHibrid/
├── engine/
│   ├── autopilot/
│   │   ├── manual_mode.py
│   │   ├── auto_mode.py
│   │   ├── geodesy_mode.py
│   │   ├── acro_mode.py
│   │   └── swarm_mode.py
│   ├── geodesy/
│   │   ├── geodesy_agent/
│   │   │   ├── gsd_calculator.py
│   │   │   ├── overlap_planner.py
│   │   │   ├── gcp_processor.py
│   │   │   ├── odm_pipeline.py
│   │   │   └── ortho_builder.py
│   ├── missions/
│   │   ├── mission_planner.py
│   │   ├── mission_templates/
│   │   └── path_optimizer.py
│   ├── gsd/
│   │   ├── gsd_math.py
│   │   └── lens_profiles.json
│   ├── power/
│   │   ├── mode_tether.py
│   │   ├── mode_solar.py
│   │   └── hybrid_energy.py
│   ├── telemetry/
│   │   ├── sensors.py
│   │   ├── health_monitor.py
│   │   └── warnings.py
│   ├── compliance/
│   │   ├── uas_zones_loader.py
│   │   ├── uas_zones_check.py
│   │   ├── remoteid_validator.py
│   │   └── insurance_rules.json
│   ├── geoviz3d/
│   │   ├── terrain_loader.py
│   │   ├── temporal_analyzer.py
│   │   └── geo_renderer.py
│   ├── pv/
│   │   ├── roof_analyzer.py
│   │   ├── field_optimizer.py
│   │   ├── shade_simulator.py
│   │   └── solar_report.py
│   └── reports/
│       ├── report_generator.py
│       ├── templates/
│       └── exporters/
├── docs/
│   ├── AUTOPILOT.md
│   ├── GEODESY.md
│   ├── GSD.md
│   ├── MISSIONS.md
│   └── PV_PLANNER.md
└── tools/
    ├── calibration/
    ├── camera_profiles/
    └── cli_helpers/


⸻

3. Core Responsibilities

3.1. Autopilot Engine (UAV & UGV)
	•	Manual mode (direct control)
	•	Auto mode (GPS-based navigation)
	•	Geodesy mode (overlap-consistent flight lines)
	•	Acro mode (advanced maneuvers)
	•	Swarm mode (multi-vehicle coordination)
	•	Sensor fusion, EKF filters, IMU/GPS integration
	•	Real-time vehicle state machine

3.2. Geodesy & Photogrammetry
	•	GSD calculation
	•	Overlap planning (front/side overlap)
	•	Flight-line generator
	•	ODM dataset ingestion & preprocessing
	•	Generation of:
	•	orthomosaic,
	•	DSM/DTM,
	•	point clouds,
	•	volume calculations
	•	Automated QC and reconstruction pipelines

3.3. Mission Planning
	•	JSON mission output
	•	Import/export for core mission templates
	•	Path optimization
	•	Terrain-follow flight profiles
	•	GCP integration

3.4. PV Planner & 3D Terrain Engine
	•	Roof plane segmentation
	•	Field layout optimizer
	•	Seasonal shade simulation
	•	Panel density maps
	•	Exportable PV reports

3.5. Telemetry & Health Monitoring
	•	Battery prediction
	•	Motor health
	•	Environmental sensors
	•	Emergency triggers
	•	Log export

3.6. Compliance & Safety
	•	UAS geo-zone parsing (EU/US/INT)
	•	Polygon intersection checks
	•	Remote-ID rules
	•	Weather constraints
	•	Country-specific restrictions

3.7. Report Generation
	•	PDF
	•	GeoTIFF
	•	LAS (point cloud)
	•	Project summary sheets

⸻

4. Cross-Repository Interaction

With WebKurierCore

Core sends all transport tasks to DroneHibrid:

Core → DroneHibrid.autopilot
Core → DroneHibrid.geodesy
Core → DroneHibrid.missions
Core → DroneHibrid.pv
Core → DroneHibrid.reports

With WebKurierPhoneCore

PhoneCore may request:
	•	Voice descriptions of missions
	•	Real-time translation during flight
	•	Warning notifications to user devices

With WebKurierChain
	•	Integrity hashes of missions
	•	Blockchain storage of flight logs
	•	WebCoin billing per mission (optional)

With WebKurierSecurity
	•	Scan mission JSON
	•	Validate uploaded datasets
	•	Prevent malicious ODM files

⸻

5. CI/CD Policy

DroneHibrid builds include:
	•	Python pipelines
	•	Node-based visualization modules
	•	Artifact deployment
	•	Cloud Run or VM runtime
	•	Versioning controlled by WebKurierHybrid

Secrets are never stored in this repo.

⸻

6. Agent Glossary (EN + RU translations only)

AutopilotAgent — Агент автопилота
DroneAgent — Агент дрона
PilotAgent — Пилот

GeodesyAgent — Геодезист
GSDCalculator — Калькулятор GSD
OverlapPlanner — Планировщик перекрытия
GCProcessor — Обработчик GCP
ODMProcessor — ODM-пайплайн

MissionAgent — Агент миссий
PathOptimizer — Оптимизатор маршрутов

GeoViz3DAgent — Гео-визуализатор 3D
PVPlannerAgent — ПВ-планировщик

TelemetryAgent — Телеметрия
HealthMonitor — Монитор здоровья системы

ComplianceAgent — Агент нормативов
RemoteIDValidator — Валидатор RemoteID

GeoReportAgent — Генератор геоотчётов


⸻

7. Governance

WebKurierDroneHibrid is maintained under the coordination of:
Vladyslav Hushchyn (VladoExport)
Germany, EU.

⸻



