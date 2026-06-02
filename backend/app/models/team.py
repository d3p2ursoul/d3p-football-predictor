"""Team model for storing team statistics"""
from datetime import datetime
from app import db

class Team(db.Model):
    """Team model"""
    __tablename__ = 'teams'
    
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    league = db.Column(db.String(100), nullable=False)
    wins = db.Column(db.Integer, default=0)
    draws = db.Column(db.Integer, default=0)
    losses = db.Column(db.Integer, default=0)
    goals_for = db.Column(db.Integer, default=0)
    goals_against = db.Column(db.Integer, default=0)
    points = db.Column(db.Integer, default=0)
    ranking = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            'id': self.id,
            'team_id': self.team_id,
            'name': self.name,
            'league': self.league,
            'stats': {
                'wins': self.wins,
                'draws': self.draws,
                'losses': self.losses,
                'goals_for': self.goals_for,
                'goals_against': self.goals_against,
                'points': self.points
            },
            'ranking': self.ranking
        }