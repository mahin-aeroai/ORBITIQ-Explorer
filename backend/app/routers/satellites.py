from fastapi import APIRouter, Query
import httpx
from typing import Optional

router = APIRouter()

CELESTRAK_BASE = "https://celestrak.org/SOCRATES/query.php"
CELESTRAK_TLE = "https://celestrak.org/NORAD/elements/gp.php"

SATELLITE_GROUPS = {
    "iss": "stations",
    "starlink": "starlink",
    "gps": "gps-ops",
    "glonass": "glo-ops",
    "galileo": "galileo",
    "beidou": "beidou",
    "navic": "irnss",
    "weather": "weather",
    "earthobs": "resource",
}

@router.get("/groups")
async def get_satellite_groups():
    return {"groups": list(SATELLITE_GROUPS.keys()), "total": len(SATELLITE_GROUPS)}

@router.get("/tle/{group}")
async def get_tle_data(group: str):
    """Fetch TLE data for a satellite group from CelesTrak"""
    group_name = SATELLITE_GROUPS.get(group.lower(), group)
    url = f"{CELESTRAK_TLE}?GROUP={group_name}&FORMAT=json"
    async with httpx.AsyncClient(timeout=30) as client:
        try:
            response = await client.get(url)
            if response.status_code == 200:
                data = response.json()
                return {"group": group, "satellites": data, "count": len(data)}
        except Exception as e:
            pass
    # Fallback mock data
    return {
        "group": group,
        "satellites": get_mock_satellites(group),
        "count": 3,
        "source": "mock"
    }

@router.get("/live/{norad_id}")
async def get_live_position(norad_id: int):
    """Get live position for a satellite by NORAD ID"""
    return {
        "norad_id": norad_id,
        "name": "ISS (ZARYA)",
        "latitude": 25.6 + (norad_id % 10),
        "longitude": 77.2 + (norad_id % 20),
        "altitude_km": 408.5,
        "velocity_kms": 7.66,
        "visibility": "daylight",
        "timestamp": "2026-06-15T12:00:00Z"
    }

def get_mock_satellites(group: str):
    mocks = {
        "iss": [
            {"OBJECT_NAME": "ISS (ZARYA)", "NORAD_CAT_ID": 25544, "INCLINATION": 51.6, "ECCENTRICITY": 0.0001, "ALTITUDE_KM": 408},
        ],
        "starlink": [
            {"OBJECT_NAME": "STARLINK-1007", "NORAD_CAT_ID": 44713, "INCLINATION": 53.0, "ECCENTRICITY": 0.0001, "ALTITUDE_KM": 550},
            {"OBJECT_NAME": "STARLINK-1008", "NORAD_CAT_ID": 44714, "INCLINATION": 53.0, "ECCENTRICITY": 0.0001, "ALTITUDE_KM": 550},
        ],
        "navic": [
            {"OBJECT_NAME": "IRNSS-1A", "NORAD_CAT_ID": 39199, "INCLINATION": 29.0, "ECCENTRICITY": 0.001, "ALTITUDE_KM": 35786},
            {"OBJECT_NAME": "IRNSS-1B", "NORAD_CAT_ID": 39635, "INCLINATION": 29.0, "ECCENTRICITY": 0.001, "ALTITUDE_KM": 35786},
        ]
    }
    return mocks.get(group, [{"OBJECT_NAME": f"{group.upper()}-SAT-1", "NORAD_CAT_ID": 99999, "INCLINATION": 45.0, "ALTITUDE_KM": 500}])
