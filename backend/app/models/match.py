"""Match model for storing football match data"""
from datetime import datetime
from app import db

class Match(db.Model):
    """Match model"""
    __tablename__ = 'matches'
    
    id = db.Column(db.Integer, primary_key=True)
    match_id = db.Column(db.String(100), unique=True, nullable=False)
    home_team = db.Column(db.String(100), nullable=False)
    away_team = db.Column(db.String(100), nullable=False)
    league = db.Column(db.String(100), nullable=False)
    match_date = db.Column(db.DateTime, nullable=False)
    home_odds = db.Column(db.Float)
    draw_odds = db.Column(db.Float)
    away_odds = db.Column(db.Float)
    status = db.Column(db.String(20), default='scheduled')  # scheduled, live, finished
    home_score = db.Column(db.Integer)
    away_score = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationship
    predictions = db.relationship('Prediction', backref='match', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            'id': self.id,
            'match_id': self.match_id,
            'home_team': self.home_team,
            'away_team': self.away_team,
            'league': self.league,
            'match_date': self.match_date.isoformat(),
            'status': self.status,
            'home_score': self.home_score,
            'away_score': self.away_score,
            'odds': {
                'home': self.home_odds,
                'draw': self.draw_odds,
                'away': self.away_odds
            }
        }