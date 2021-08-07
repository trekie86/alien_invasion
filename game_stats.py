from settings import Settings


class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, settings: Settings):
        """Initialize statistics."""
        self.settings: Settings = settings
        self.ships_left: int = self.settings.ship_limit
        self.score: int = 0

        # Start Alien Invasion in an inactive state.
        self.game_active: bool = False

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left: int = self.settings.ship_limit
        self.score: int = 0
