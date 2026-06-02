# Football Predictor Backend API

Python Flask-based REST API for football match predictions using machine learning.

## Setup

### Prerequisites
- Python 3.11+
- pip
- Virtual environment (recommended)

### Installation

1. **Create virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the application:**
```bash
python -m app.main
```

The API will be available at `http://localhost:5000`

## API Endpoints

### Health Check
- `GET /api/health` - Check API status

### Matches
- `GET /api/matches` - Get all matches (paginated)
- `GET /api/matches/<id>` - Get specific match
- `POST /api/matches` - Create new match

### Predictions
- `GET /api/predictions` - Get all predictions
- `GET /api/predictions/<id>` - Get specific prediction
- `POST /api/predictions/match/<match_id>` - Generate prediction

### Teams
- `GET /api/teams` - Get all teams
- `GET /api/teams/<id>` - Get specific team
- `GET /api/teams/by-name/<name>` - Get team by name

## Testing

```bash
pytest
pytest --cov=app
```

## Docker

```bash
docker build -t football-predictor-backend .
docker run -p 5000:5000 football-predictor-backend
```