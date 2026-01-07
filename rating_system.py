from openskill.models import PlackettLuce, PlackettLuceRating
from config import Config


class RatingSystem:
    """OpenSkill rating system using Plackett-Luce model"""
    
    def __init__(self):
        """Initialize Plackett-Luce model with configuration"""
        self.model = PlackettLuce(
            mu=Config.OPENSKILL_MU,
            sigma=Config.OPENSKILL_SIGMA,
            beta=Config.OPENSKILL_BETA,
            tau=Config.OPENSKILL_TAU
        )
    
    def create_initial_rating(self):
        """Create initial rating for a new player"""
        return PlackettLuceRating(mu=Config.OPENSKILL_MU, sigma=Config.OPENSKILL_SIGMA)
    
    def calculate_new_ratings(self, mu_sigma_list, ranks):
        """
        Calculate new ratings for a match.
        
        Args:
            mu_sigma_list: List of (mu, sigma) tuples
            ranks: List of ranks
        
        Returns:
            List of (new_mu, new_sigma) tuples
        """
        teams = [[PlackettLuceRating(mu=mu, sigma=sigma)] for mu, sigma in mu_sigma_list]
        new_teams = self.model.rate(teams, ranks=ranks)
        return [(t[0].mu, t[0].sigma) for t in new_teams]
    
    def process_game_results(self, player_results):
        """
        Process game results and calculate new ratings for all players.
        
        Args:
            player_results: List of dicts with keys:
                - player: Player object
                - placement: int
                - points: int
        
        Returns:
            List of dicts with detailed changes
        """
        ranks = [r['placement'] for r in player_results]
        mu_sigmas = [(r['player'].mu, r['player'].sigma) for r in player_results]
        
        new_ratings = self.calculate_new_ratings(mu_sigmas, ranks)
        
        processed_results = []
        for i, result in enumerate(player_results):
            processed_results.append({
                'player': result['player'],
                'placement': result['placement'],
                'points': result['points'],
                'mu_before': mu_sigmas[i][0],
                'sigma_before': mu_sigmas[i][1],
                'mu_after': new_ratings[i][0],
                'sigma_after': new_ratings[i][1]
            })
            
        return processed_results


# Global rating system instance
rating_system = RatingSystem()
