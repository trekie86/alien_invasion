from settings import Settings


class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, settings: Settings):
        """Initialize statistics."""
        self.settings = settings
        self.reset_stats()

        # Start Alien Invasion in an active state.
        self.game_active: bool = True

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left: int = self.settings.ship_limit
