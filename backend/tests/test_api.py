"""Tests for API endpoints"""
import pytest
from app import create_app, db
from app.models.match import Match
from datetime import datetime, timedelta

@pytest.fixture
def client():
    """Create test client"""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()

def test_health_check(client):
    """Test health check endpoint"""
    response = client.get('/api/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert data['service'] == 'Football Predictor API'

def test_get_matches_empty(client):
    """Test getting matches when none exist"""
    response = client.get('/api/matches')
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] is True
    assert data['data'] == []

def test_create_match(client):
    """Test creating a match"""
    match_data = {
        'match_id': 'MATCH_001',
        'home_team': 'Manchester United',
        'away_team': 'Liverpool',
        'league': 'Premier League',
        'match_date': (datetime.utcnow() + timedelta(days=7)).isoformat(),
        'home_odds': 2.1,
        'draw_odds': 3.5,
        'away_odds': 3.2
    }
    
    response = client.post('/api/matches', json=match_data)
    assert response.status_code == 201
    data = response.get_json()
    assert data['success'] is True
    assert data['data']['home_team'] == 'Manchester United'

def test_get_teams(client):
    """Test getting teams"""
    response = client.get('/api/teams')
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] is True

def test_get_predictions(client):
    """Test getting predictions"""
    response = client.get('/api/predictions')
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] is True