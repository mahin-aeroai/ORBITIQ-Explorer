from fastapi import APIRouter

router = APIRouter()

METEOR_SHOWERS = [
    {"id": "perseids", "name": "Perseids", "parent_body": "109P/Swift-Tuttle",
     "peak_date": "2026-08-12", "peak_rate": 100, "active_start": "2026-07-17", "active_end": "2026-08-24",
     "radiant_ra": "46°", "radiant_dec": "+58°", "velocity_kms": 59, "best_time": "after midnight",
     "description": "One of the most popular showers, known for bright meteors and fireballs."},
    {"id": "geminids", "name": "Geminids", "parent_body": "3200 Phaethon (asteroid)",
     "peak_date": "2026-12-14", "peak_rate": 150, "active_start": "2026-12-04", "active_end": "2026-12-17",
     "radiant_ra": "112°", "radiant_dec": "+33°", "velocity_kms": 35, "best_time": "10pm-4am",
     "description": "The richest annual shower, unique in originating from an asteroid rather than a comet."},
    {"id": "leonids", "name": "Leonids", "parent_body": "55P/Tempel-Tuttle",
     "peak_date": "2026-11-17", "peak_rate": 15, "active_start": "2026-11-06", "active_end": "2026-11-30",
     "radiant_ra": "152°", "radiant_dec": "+22°", "velocity_kms": 71, "best_time": "after midnight",
     "description": "Fast meteors, can produce spectacular storms every 33 years."},
    {"id": "quadrantids", "name": "Quadrantids", "parent_body": "2003 EH1 (asteroid)",
     "peak_date": "2026-01-03", "peak_rate": 120, "active_start": "2025-12-28", "active_end": "2026-01-12",
     "radiant_ra": "230°", "radiant_dec": "+49°", "velocity_kms": 41, "best_time": "pre-dawn",
     "description": "High peak rate but very short peak window of only a few hours."},
    {"id": "orionids", "name": "Orionids", "parent_body": "1P/Halley",
     "peak_date": "2026-10-21", "peak_rate": 25, "active_start": "2026-10-02", "active_end": "2026-11-07",
     "radiant_ra": "95°", "radiant_dec": "+16°", "velocity_kms": 66, "best_time": "after midnight",
     "description": "Debris from Halley's Comet, known for fast and bright meteors."},
    {"id": "eta-aquariids", "name": "Eta Aquariids", "parent_body": "1P/Halley",
     "peak_date": "2026-05-06", "peak_rate": 60, "active_start": "2026-04-19", "active_end": "2026-05-28",
     "radiant_ra": "338°", "radiant_dec": "-1°", "velocity_kms": 66, "best_time": "pre-dawn",
     "description": "Best from southern hemisphere; debris from Halley's Comet like Orionids."},
    {"id": "lyrids", "name": "Lyrids", "parent_body": "C/1861 G1 (Thatcher)",
     "peak_date": "2026-04-22", "peak_rate": 20, "active_start": "2026-04-16", "active_end": "2026-04-25",
     "radiant_ra": "271°", "radiant_dec": "+34°", "velocity_kms": 49, "best_time": "after midnight",
     "description": "One of the oldest recorded meteor showers, observed for 2,700+ years."},
    {"id": "draconids", "name": "Draconids", "parent_body": "21P/Giacobini-Zinner",
     "peak_date": "2026-10-08", "peak_rate": 10, "active_start": "2026-10-06", "active_end": "2026-10-10",
     "radiant_ra": "262°", "radiant_dec": "+54°", "velocity_kms": 20, "best_time": "evening",
     "description": "Slow meteors; rare outbursts can produce thousands of meteors per hour."},
]

FIREBALL_EVENTS = [
    {"date": "2026-06-10", "location": "Eastern Europe", "magnitude": -12, "type": "Superbolide", "fragmented": True},
    {"date": "2026-05-22", "location": "Western USA", "magnitude": -8, "type": "Fireball", "fragmented": False},
    {"date": "2026-04-15", "location": "India (Rajasthan)", "magnitude": -6, "type": "Bolide", "fragmented": True},
    {"date": "2026-03-30", "location": "Pacific Ocean", "magnitude": -14, "type": "Superbolide", "fragmented": True},
    {"date": "2026-02-18", "location": "South America", "magnitude": -7, "type": "Fireball", "fragmented": False},
]

@router.get("/showers")
async def get_meteor_showers():
    return {"showers": METEOR_SHOWERS, "count": len(METEOR_SHOWERS)}

@router.get("/fireballs")
async def get_fireball_events():
    return {"fireballs": FIREBALL_EVENTS, "count": len(FIREBALL_EVENTS)}

@router.get("/showers/{shower_id}")
async def get_shower(shower_id: str):
    for s in METEOR_SHOWERS:
        if s["id"] == shower_id.lower():
            return s
    return {"error": "Shower not found"}
