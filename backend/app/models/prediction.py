"""Prediction model for storing match predictions"""
from datetime import datetime
from app import db

class Prediction(db.Model):
    """Prediction model"""
    __tablename__ = 'predictions'
    
    id = db.Column(db.Integer, primary_key=True)
    match_id = db.Column(db.Integer, db.ForeignKey('matches.id'), nullable=False)
    home_win_probability = db.Column(db.Float, nullable=False)
    draw_probability = db.Column(db.Float, nullable=False)
    away_win_probability = db.Column(db.Float, nullable=False)
    predicted_winner = db.Column(db.String(50))  # 'home', 'draw', 'away'
    confidence_score = db.Column(db.Float)
    model_version = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            'id': self.id,
            'match_id': self.match_id,
            'probabilities': {
                'home_win': self.home_win_probability,
                'draw': self.draw_probability,
                'away_win': self.away_win_probability
            },
            'predicted_winner': self.predicted_winner,
            'confidence': self.confidence_score,
            'model_version': self.model_version,
            'created_at': self.created_at.isoformat()
        }