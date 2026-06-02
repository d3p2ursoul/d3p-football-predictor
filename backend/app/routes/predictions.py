"""Prediction endpoints"""
from flask import Blueprint, jsonify, request
from app import db
from app.models.prediction import Prediction
from app.models.match import Match
from app.services.prediction_service import PredictionService

bp = Blueprint('predictions', __name__, url_prefix='/api/predictions')
prediction_service = PredictionService()

@bp.route('', methods=['GET'])
def get_predictions():
    """Get all predictions"""
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 20, type=int)
        
        predictions = Prediction.query.paginate(page=page, per_page=per_page)
        
        return jsonify({
            'success': True,
            'data': [p.to_dict() for p in predictions.items],
            'pagination': {
                'page': page,
                'per_page': per_page,
                'total': predictions.total,
                'pages': predictions.pages
            }
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@bp.route('/<int:prediction_id>', methods=['GET'])
def get_prediction(prediction_id):
    """Get specific prediction"""
    try:
        prediction = Prediction.query.get(prediction_id)
        if not prediction:
            return jsonify({'success': False, 'error': 'Prediction not found'}), 404
        
        return jsonify({
            'success': True,
            'data': prediction.to_dict()
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@bp.route('/match/<int:match_id>', methods=['POST'])
def predict_match(match_id):
    """Create prediction for a match"""
    try:
        match = Match.query.get(match_id)
        if not match:
            return jsonify({'success': False, 'error': 'Match not found'}), 404
        
        # Generate prediction using service
        prediction_data = prediction_service.predict_match(match)
        
        # Save to database
        prediction = Prediction(
            match_id=match_id,
            home_win_probability=prediction_data['probabilities']['home_win'],
            draw_probability=prediction_data['probabilities']['draw'],
            away_win_probability=prediction_data['probabilities']['away_win'],
            predicted_winner=prediction_data['predicted_winner'],
            confidence_score=prediction_data['confidence'],
            model_version='1.0.0'
        )
        
        db.session.add(prediction)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'data': prediction.to_dict()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500