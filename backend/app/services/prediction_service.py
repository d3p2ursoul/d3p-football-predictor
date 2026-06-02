"""Prediction service using ML models"""
import numpy as np
from sklearn.preprocessing import StandardScaler
import os

class PredictionService:
    """Service for generating match predictions"""
    
    def __init__(self):
        """Initialize prediction service"""
        self.scaler = StandardScaler()
    
    def predict_match(self, match):
        """Predict match outcome"""
        try:
            # Extract features from match
            features = self._extract_features(match)
            
            # Generate probabilities using ensemble approach
            probabilities = self._calculate_probabilities(features)
            
            # Determine winner
            predicted_winner = self._determine_winner(probabilities)
            
            # Calculate confidence
            confidence = max(probabilities.values())
            
            return {
                'probabilities': probabilities,
                'predicted_winner': predicted_winner,
                'confidence': confidence
            }
        except Exception as e:
            print(f"Error in prediction: {e}")
            # Return default probabilities if error
            return {
                'probabilities': {
                    'home_win': 0.33,
                    'draw': 0.34,
                    'away_win': 0.33
                },
                'predicted_winner': 'draw',
                'confidence': 0.34
            }
    
    def _extract_features(self, match):
        """Extract features from match for prediction"""
        # Get team stats from database
        home_team = match.home_team
        away_team = match.away_team
        
        # In production, fetch actual team stats from database
        # For now, returning placeholder features
        features = {
            'home_team': home_team,
            'away_team': away_team,
            'league': match.league,
            'home_rank': 1,
            'away_rank': 5,
            'home_recent_form': 0.65,
            'away_recent_form': 0.45,
            'home_goals_for': 2.1,
            'away_goals_for': 1.8
        }
        return features
    
    def _calculate_probabilities(self, features):
        """Calculate win/draw/loss probabilities"""
        # Simple heuristic model for demonstration
        home_strength = features.get('home_recent_form', 0.5)
        away_strength = features.get('away_recent_form', 0.5)
        
        # Adjust based on rankings
        home_rank_factor = 1 / (features.get('home_rank', 10))
        away_rank_factor = 1 / (features.get('away_rank', 10))
        
        home_win_prob = (home_strength * 0.7 + home_rank_factor * 0.3)
        away_win_prob = (away_strength * 0.7 + away_rank_factor * 0.3)
        
        # Normalize
        total = home_win_prob + away_win_prob + 0.3
        
        return {
            'home_win': round(home_win_prob / total, 3),
            'draw': round(0.3 / total, 3),
            'away_win': round(away_win_prob / total, 3)
        }
    
    def _determine_winner(self, probabilities):
        """Determine predicted winner from probabilities"""
        outcomes = {
            'home_win': probabilities['home_win'],
            'draw': probabilities['draw'],
            'away_win': probabilities['away_win']
        }
        return max(outcomes, key=outcomes.get)