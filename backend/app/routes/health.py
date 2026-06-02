"""Health check endpoints"""
from flask import Blueprint, jsonify

bp = Blueprint('health', __name__, url_prefix='/api')

@bp.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'Football Predictor API',
        'version': '1.0.0'
    }), 200