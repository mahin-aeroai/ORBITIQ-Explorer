from fastapi import APIRouter, Query
import httpx
import os

router = APIRouter()
NASA_API_KEY = os.getenv("NASA_API_KEY", "DEMO_KEY")

@router.get("/")
async def search(q: str = Query(..., min_length=2), category: str = Query("all")):
    results = []
    q_lower = q.lower()

    if category in ("all", "asteroid"):
        url = f"https://api.nasa.gov/neo/rest/v1/neo/browse?api_key={NASA_API_KEY}"
        async with httpx.AsyncClient(timeout=15) as client:
            try:
                r = await client.get(url)
                if r.status_code == 200:
                    data = r.json()
                    for neo in data.get("near_earth_objects", []):
                        if q_lower in neo["name"].lower():
                            results.append({"type": "asteroid", "name": neo["name"], "id": neo["id"],
                                            "is_hazardous": neo.get("is_potentially_hazardous_asteroid", False)})
            except Exception:
                pass

    # Add mock results if nothing found
    if not results:
        if "iss" in q_lower or "station" in q_lower:
            results.append({"type": "satellite", "name": "ISS (ZARYA)", "id": "25544", "altitude_km": 408})
        if "starlink" in q_lower:
            results.append({"type": "satellite", "name": "STARLINK Constellation", "id": "starlink", "count": "6000+"})
        if "halley" in q_lower:
            results.append({"type": "comet", "name": "1P/Halley", "id": "1P", "period_years": 75.3})
        if "perseids" in q_lower:
            results.append({"type": "meteor_shower", "name": "Perseids", "id": "perseids", "peak_rate": 100})

    return {"query": q, "category": category, "results": results, "count": len(results)}
