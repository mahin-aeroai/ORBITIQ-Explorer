from fastapi import APIRouter
import httpx

router = APIRouter()

COMETS = [
    {"id": "C2023A3", "name": "C/2023 A3 (Tsuchinshan-ATLAS)", "type": "Long-period", "period_years": None,
     "perihelion_au": 0.391, "perihelion_date": "2024-09-27", "magnitude": 4.9,
     "discoverer": "Tsuchinshan + ATLAS", "status": "past perihelion",
     "description": "One of the brightest comets of the 21st century, visible to naked eye in late 2024."},
    {"id": "C2017K2", "name": "C/2017 K2 (PanSTARRS)", "type": "Long-period", "period_years": None,
     "perihelion_au": 1.80, "perihelion_date": "2022-12-19", "magnitude": 8.2,
     "discoverer": "PanSTARRS", "status": "receding",
     "description": "Largest cometary coma ever observed at great heliocentric distance."},
    {"id": "67P", "name": "67P/Churyumov-Gerasimenko", "type": "Short-period", "period_years": 6.44,
     "perihelion_au": 1.21, "perihelion_date": "2021-11-02", "magnitude": 10.5,
     "discoverer": "Churyumov & Gerasimenko", "status": "active",
     "description": "Target of ESA's Rosetta mission; Philae lander made first comet landing in 2014."},
    {"id": "1P", "name": "1P/Halley", "type": "Short-period", "period_years": 75.3,
     "perihelion_au": 0.586, "perihelion_date": "1986-02-09", "magnitude": 2.1,
     "discoverer": "Edmond Halley", "status": "distant/outbound",
     "description": "The most famous periodic comet, next perihelion expected around 2061."},
    {"id": "C2020F3", "name": "C/2020 F3 (NEOWISE)", "type": "Long-period", "period_years": 6800,
     "perihelion_au": 0.295, "perihelion_date": "2020-07-03", "magnitude": 0.9,
     "discoverer": "NEOWISE", "status": "receding",
     "description": "Brightest northern comet since Hale-Bopp (1997), visible to naked eye for weeks."},
    {"id": "C2024G3", "name": "C/2024 G3 (ATLAS)", "type": "Long-period", "period_years": None,
     "perihelion_au": 0.089, "perihelion_date": "2025-01-13", "magnitude": -3.0,
     "discoverer": "ATLAS", "status": "post-perihelion",
     "description": "Spectacular sungrazing comet that may have disrupted near perihelion."},
]

@router.get("/")
async def get_comets():
    return {"comets": COMETS, "count": len(COMETS)}

@router.get("/{comet_id}")
async def get_comet(comet_id: str):
    for c in COMETS:
        if c["id"].lower() == comet_id.lower():
            return c
    return {"error": "Comet not found", "id": comet_id}
