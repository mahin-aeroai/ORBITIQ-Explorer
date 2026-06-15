from fastapi import APIRouter, Query
import httpx
import os
from datetime import datetime, timedelta

router = APIRouter()
NASA_API_KEY = os.getenv("NASA_API_KEY", "DEMO_KEY")
NEO_BASE = "https://api.nasa.gov/neo/rest/v1"

@router.get("/neo/feed")
async def get_neo_feed(days: int = Query(7, le=7)):
    """Get Near Earth Object feed from NASA API"""
    start = datetime.now().strftime("%Y-%m-%d")
    end = (datetime.now() + timedelta(days=days)).strftime("%Y-%m-%d")
    url = f"{NEO_BASE}/feed?start_date={start}&end_date={end}&api_key={NASA_API_KEY}"
    async with httpx.AsyncClient(timeout=30) as client:
        try:
            response = await client.get(url)
            if response.status_code == 200:
                data = response.json()
                neos = []
                for date, objects in data.get("near_earth_objects", {}).items():
                    for obj in objects:
                        neos.append({
                            "id": obj["id"],
                            "name": obj["name"],
                            "date": date,
                            "is_hazardous": obj["is_potentially_hazardous_asteroid"],
                            "diameter_min_km": obj["estimated_diameter"]["kilometers"]["estimated_diameter_min"],
                            "diameter_max_km": obj["estimated_diameter"]["kilometers"]["estimated_diameter_max"],
                            "close_approach": obj["close_approach_data"][0] if obj["close_approach_data"] else {},
                            "nasa_url": obj.get("nasa_jpl_url", ""),
                        })
                return {"neo_objects": neos, "count": len(neos), "source": "nasa"}
        except Exception as e:
            pass
    return {"neo_objects": get_mock_neos(), "count": 5, "source": "mock"}

@router.get("/hazardous")
async def get_potentially_hazardous():
    """Get list of Potentially Hazardous Asteroids"""
    url = f"{NEO_BASE}/neo/browse?api_key={NASA_API_KEY}"
    async with httpx.AsyncClient(timeout=30) as client:
        try:
            response = await client.get(url)
            if response.status_code == 200:
                data = response.json()
                hazardous = [n for n in data.get("near_earth_objects", []) if n.get("is_potentially_hazardous_asteroid")]
                return {"hazardous": hazardous[:20], "count": len(hazardous)}
        except Exception:
            pass
    return {"hazardous": get_mock_neos(hazardous_only=True), "count": 3, "source": "mock"}

@router.get("/{asteroid_id}")
async def get_asteroid(asteroid_id: str):
    url = f"{NEO_BASE}/neo/{asteroid_id}?api_key={NASA_API_KEY}"
    async with httpx.AsyncClient(timeout=30) as client:
        try:
            response = await client.get(url)
            if response.status_code == 200:
                return response.json()
        except Exception:
            pass
    return {"id": asteroid_id, "name": f"Asteroid {asteroid_id}", "source": "mock"}

def get_mock_neos(hazardous_only=False):
    neos = [
        {"id": "2021PL", "name": "(2021 PL1)", "date": "2026-06-15", "is_hazardous": True,
         "diameter_min_km": 0.12, "diameter_max_km": 0.27, "velocity_kms": 18.5, "miss_distance_km": 2100000},
        {"id": "2019QX", "name": "(2019 QX1)", "date": "2026-06-16", "is_hazardous": False,
         "diameter_min_km": 0.05, "diameter_max_km": 0.11, "velocity_kms": 12.3, "miss_distance_km": 5800000},
        {"id": "2022AB", "name": "(2022 AB3)", "date": "2026-06-17", "is_hazardous": True,
         "diameter_min_km": 0.31, "diameter_max_km": 0.69, "velocity_kms": 22.1, "miss_distance_km": 1300000},
        {"id": "2018HX", "name": "(2018 HX5)", "date": "2026-06-18", "is_hazardous": False,
         "diameter_min_km": 0.02, "diameter_max_km": 0.04, "velocity_kms": 9.7, "miss_distance_km": 7200000},
        {"id": "2020YW", "name": "(2020 YW2)", "date": "2026-06-19", "is_hazardous": True,
         "diameter_min_km": 0.45, "diameter_max_km": 1.01, "velocity_kms": 25.6, "miss_distance_km": 890000},
    ]
    if hazardous_only:
        return [n for n in neos if n["is_hazardous"]]
    return neos
