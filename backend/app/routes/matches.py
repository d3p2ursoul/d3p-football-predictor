"""Match endpoints"""
from flask import Blueprint, jsonify, request
from app import db
from app.models.match import Match

bp = Blueprint('matches', __name__, url_prefix='/api/matches')

@bp.route('', methods=['GET'])
def get_matches():
    """Get all matches"""
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 20, type=int)
        league = request.args.get('league')
        status = request.args.get('status')
        
        query = Match.query
        
        if league:
            query = query.filter_by(league=league)
        if status:
            query = query.filter_by(status=status)
        
        matches = query.paginate(page=page, per_page=per_page)
        
        return jsonify({
            'success': True,
            'data': [m.to_dict() for m in matches.items],
            'pagination': {
                'page': page,
                'per_page': per_page,
                'total': matches.total,
                'pages': matches.pages
            }
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@bp.route('/<int:match_id>', methods=['GET'])
def get_match(match_id):
    """Get specific match"""
    try:
        match = Match.query.get(match_id)
        if not match:
            return jsonify({'success': False, 'error': 'Match not found'}), 404
        
        return jsonify({
            'success': True,
            'data': match.to_dict()
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@bp.route('', methods=['POST'])
def create_match():
    """Create new match"""
    try:
        data = request.get_json()
        
        # Validate required fields
        required = ['match_id', 'home_team', 'away_team', 'league', 'match_date']
        if not all(field in data for field in required):
            return jsonify({'success': False, 'error': 'Missing required fields'}), 400
        
        match = Match(
            match_id=data['match_id'],
            home_team=data['home_team'],
            away_team=data['away_team'],
            league=data['league'],
            match_date=data['match_date'],
            home_odds=data.get('home_odds'),
            draw_odds=data.get('draw_odds'),
            away_odds=data.get('away_odds')
        )
        
        db.session.add(match)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'data': match.to_dict()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500