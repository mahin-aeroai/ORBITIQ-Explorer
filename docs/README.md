# 🛰 ORBITIQ Explorer

**Real-time Space Tracking & Visualization Platform**

A full-stack aerospace intelligence platform covering satellite tracking, asteroid monitoring, comet exploration, meteor shower calendars, and an interactive 3D Earth globe — styled as a NASA Mission Control dashboard.

---

## ✨ Features

### 🛰 Satellite Tracker
- ISS real-time position with live latitude/longitude updates
- Starlink constellation tracking (6,000+ satellites)
- GPS, GLONASS, Galileo, BeiDou constellations
- **NavIC** (India Regional Navigation Satellite System)
- Weather satellites (METEOSAT, INSAT, GOES, NOAA)
- Earth Observation satellites (Sentinel-2, Landsat 9, Cartosat-3)
- TLE data sourced from **CelesTrak** (updated every 2 hours)

### ⚠️ Asteroid Dashboard
- Near Earth Object (NEO) 7-day feed via **NASA NEO API**
- Potentially Hazardous Asteroid (PHA) catalog
- Close approach distance, velocity, and diameter data
- Risk classification (LOW / MEDIUM / HIGH)

### ☄️ Comet Explorer
- 6 featured active/notable comets including:
  - C/2023 A3 (Tsuchinshan-ATLAS)
  - 67P/Churyumov-Gerasimenko (Rosetta target)
  - 1P/Halley
  - C/2024 G3 (ATLAS)
- Perihelion distance, magnitude, discoverer, description

### ✨ Meteor Center
- 2026 full meteor shower calendar (9 major showers)
- ZHR (Zenithal Hourly Rate), velocity, active period
- Fireball event log with magnitude and location
- Parent comet/asteroid association

### 🌍 Interactive 3D Globe
- Canvas-based animated Earth visualization
- ISS live orbit track animation
- Starlink shell ring
- NavIC GSO satellites
- Orbital layer toggles (LEO/MEO/GEO)
- ISS pass predictions for Hyderabad

### 🔍 Search Engine
- Unified search across all object types
- Category filters: Satellites / Asteroids / Comets / Meteors
- Real-time results from in-memory catalog

### 📡 Space Events Feed
- Upcoming rocket launches (SpaceX, ISRO)
- Astronomical events (oppositions, solstices)
- NEO close approach alerts
- Meteor shower peaks

---

## 🏗 Architecture

```
orbitiq/
├── frontend/
│   └── orbitiq.html          # Single-file app (open directly in browser)
│
├── backend/
│   ├── requirements.txt
│   └── app/
│       ├── main.py           # FastAPI app entry point
│       └── routers/
│           ├── satellites.py # CelesTrak TLE integration
│           ├── asteroids.py  # NASA NEO API integration
│           ├── comets.py     # Comet catalog
│           ├── meteors.py    # Meteor shower data
│           └── search.py     # Unified search endpoint
│
├── docker/
│   ├── docker-compose.yml
│   ├── Dockerfile.frontend
│   └── Dockerfile.backend
│
└── docs/
    └── README.md
```

---

## 🚀 Quick Start

### Option 1: Open Directly (No Server Required)
```bash
# Just open in your browser:
open frontend/orbitiq.html
# or
xdg-open frontend/orbitiq.html
```

### Option 2: Docker (Full Stack)
```bash
cd docker
cp .env.example .env
# Add your NASA API key to .env:
# NASA_API_KEY=your_key_here

docker compose up --build
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000/docs
```

### Option 3: Backend Only
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
# Swagger docs: http://localhost:8000/docs
```

---

## 🔑 API Keys

| Service | URL | Free Tier |
|---------|-----|-----------|
| NASA NEO API | https://api.nasa.gov | 1000 req/hr (DEMO_KEY for testing) |
| CelesTrak | https://celestrak.org | Free, no key needed |
| JPL Small Body DB | https://ssd.jpl.nasa.gov | Free, no key needed |

Get a NASA API key (free): https://api.nasa.gov/#signUp

---

## 📡 API Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /api/satellites/tle/{group}` | TLE data for a satellite group |
| `GET /api/satellites/live/{norad_id}` | Live position for a satellite |
| `GET /api/asteroids/neo/feed` | NASA NEO 7-day feed |
| `GET /api/asteroids/hazardous` | PHA catalog |
| `GET /api/comets/` | All featured comets |
| `GET /api/meteors/showers` | 2026 meteor shower calendar |
| `GET /api/meteors/fireballs` | Recent fireball events |
| `GET /api/search/?q={query}` | Unified search |

Interactive API docs: `http://localhost:8000/docs`

---

## 🖥 Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend App | HTML5 · CSS3 · Vanilla JS |
| Globe Rendering | HTML5 Canvas (WebGL-ready) |
| Backend API | Python · FastAPI |
| Database | PostgreSQL 16 |
| HTTP Client | HTTPX (async) |
| Containerization | Docker · Docker Compose |
| Data Sources | CelesTrak · NASA NEO · JPL |

---

## 🎨 Design System

- **Theme**: NASA Mission Control dark mode
- **Primary**: `#00d4ff` (plasma cyan)
- **Warning**: `#f59e0b` (amber)
- **Danger**: `#ef4444` (red)
- **Nebula**: `#8b5cf6` (purple)
- **Typefaces**: Rajdhani (display) · Inter (body) · Space Mono (data)

---

## 🛣 Roadmap

- [ ] CesiumJS 3D globe integration
- [ ] WebSocket live telemetry streaming
- [ ] User accounts and watch lists
- [ ] Push notifications for close approaches
- [ ] Mobile app (React Native)
- [ ] Augmented Reality sky overlay
- [ ] APOD (NASA Astronomy Picture of the Day) integration

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

*Data sources: CelesTrak, NASA NEO API, JPL Small Body Database, International Meteor Organization*
