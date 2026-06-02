"""Football Predictor Backend Application"""
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    """Application factory pattern"""
    app = Flask(__name__)
    
    # Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'DATABASE_URL', 
        'sqlite:///football_predictor.db'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JSON_SORT_KEYS'] = False
    
    # Initialize extensions
    db.init_app(app)
    CORS(app)
    
    # Create tables
    with app.app_context():
        db.create_all()
    
    # Register blueprints
    from app.routes import health, predictions, matches, teams
    app.register_blueprint(health.bp)
    app.register_blueprint(predictions.bp)
    app.register_blueprint(matches.bp)
    app.register_blueprint(teams.bp)
    
    return app