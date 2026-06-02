"""Sports API integration service"""
import requests
import os
from typing import List, Dict

class SportsAPIService:
    """Service for integrating with external sports APIs"""
    
    def __init__(self):
        """Initialize sports API service"""
        self.thesportsdb_base = 'https://www.thesportsdb.com/api/v1/json/3'
        self.timeout = 10
    
    def get_upcoming_matches(self, league: str) -> List[Dict]:
        """Get upcoming matches for a league"""
        try:
            # Placeholder implementation
            return []
        except Exception as e:
            print(f"Error fetching matches: {e}")
            return []
    
    def get_team_stats(self, team_name: str) -> Dict:
        """Get team statistics from TheSportsDB"""
        try:
            endpoint = f"{self.thesportsdb_base}/searchteams.php"
            params = {'t': team_name}
            
            response = requests.get(endpoint, params=params, timeout=self.timeout)
            response.raise_for_status()
            
            data = response.json()
            teams = data.get('teams', [])
            
            if teams:
                return self._parse_team_stats(teams[0])
            return {}
        except Exception as e:
            print(f"Error fetching team stats: {e}")
            return {}
    
    def _parse_team_stats(self, team: Dict) -> Dict:
        """Parse team statistics from API response"""
        return {
            'team_id': team.get('idTeam'),
            'name': team.get('strTeam'),
            'league': team.get('strLeague'),
            'description': team.get('strDescriptionEN'),
            'stadium': team.get('strStadium'),
            'website': team.get('strWebsite')
        }