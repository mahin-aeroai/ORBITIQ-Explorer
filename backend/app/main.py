from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import satellites, asteroids, comets, meteors, search

app = FastAPI(
    title="ORBITIQ API",
    description="Real-time space tracking and visualization API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(satellites.router, prefix="/api/satellites", tags=["Satellites"])
app.include_router(asteroids.router, prefix="/api/asteroids", tags=["Asteroids"])
app.include_router(comets.router, prefix="/api/comets", tags=["Comets"])
app.include_router(meteors.router, prefix="/api/meteors", tags=["Meteors"])
app.include_router(search.router, prefix="/api/search", tags=["Search"])

@app.get("/")
def root():
    return {"message": "ORBITIQ API v1.0.0", "status": "operational"}

@app.get("/health")
def health():
    return {"status": "healthy"}
