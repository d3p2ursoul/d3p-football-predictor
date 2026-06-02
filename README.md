# Football Predictor 🏆⚽

An AI-powered football match prediction system that provides intelligent predictions for football matches using machine learning models and real-time data from legitimate sports APIs.

## Features

- 🤖 **ML-Powered Predictions** - Advanced machine learning models for match outcome prediction
- 📊 **Real-Time Data** - Integration with legitimate sports APIs (TheSportsDB, RapidAPI)
- 🎯 **Multiple Leagues** - Support for major football leagues worldwide
- 📈 **Historical Analysis** - Trend analysis and team statistics
- 🌐 **Web Interface** - Interactive dashboard for viewing predictions
- 🔄 **REST API** - Comprehensive backend API for predictions
- 📝 **Documentation** - Complete API and setup documentation
- ✅ **Testing** - Full test coverage with unit and integration tests

## Quick Start

### Backend
```bash
cd backend
pip install -r requirements.txt
python -m app.main
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

### Docker
```bash
docker-compose up
```

## Tech Stack

**Backend:** Flask, Python, scikit-learn, pandas, numpy
**Frontend:** React, Tailwind CSS, Chart.js
**Database:** SQLite (dev) / PostgreSQL (prod)
**DevOps:** Docker, GitHub Actions, pytest

## API Endpoints

- `GET /api/health` - Health check
- `GET /api/predictions` - Get all predictions
- `POST /api/predictions/match/<id>` - Generate prediction
- `GET /api/matches` - Get matches
- `GET /api/teams` - Get teams

## Documentation

- [Backend Setup](./backend/README.md)
- [Frontend Setup](./frontend/README.md)
- [API Reference](./docs/API.md)
- [ML Models](./docs/MODELS.md)

## Disclaimer

⚠️ **Important:** Predictions are for informational purposes only. Never use for betting without proper research.

## License

MIT License