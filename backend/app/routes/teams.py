"""Team endpoints"""
from flask import Blueprint, jsonify, request
from app.models.team import Team

bp = Blueprint('teams', __name__, url_prefix='/api/teams')

@bp.route('', methods=['GET'])
def get_teams():
    """Get all teams"""
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 30, type=int)
        league = request.args.get('league')
        
        query = Team.query
        if league:
            query = query.filter_by(league=league)
        
        teams = query.paginate(page=page, per_page=per_page)
        
        return jsonify({
            'success': True,
            'data': [t.to_dict() for t in teams.items],
            'pagination': {
                'page': page,
                'per_page': per_page,
                'total': teams.total,
                'pages': teams.pages
            }
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@bp.route('/<int:team_id>', methods=['GET'])
def get_team(team_id):
    """Get specific team"""
    try:
        team = Team.query.get(team_id)
        if not team:
            return jsonify({'success': False, 'error': 'Team not found'}), 404
        
        return jsonify({
            'success': True,
            'data': team.to_dict()
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@bp.route('/by-name/<name>', methods=['GET'])
def get_team_by_name(name):
    """Get team by name"""
    try:
        team = Team.query.filter_by(name=name).first()
        if not team:
            return jsonify({'success': False, 'error': 'Team not found'}), 404
        
        return jsonify({
            'success': True,
            'data': team.to_dict()
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500