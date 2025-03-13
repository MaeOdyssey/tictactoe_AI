from ai_logic import AI
class Game:
    def __init__(self, screen):
        """Initialize the game with board, rules, and AI."""
        self.screen = screen
        self.board = Board()
        self.rules = GameRules(self.board)
        self.current_player = "X"
        self.game_over = False
        self.ai = AI("O", "X", self.board)  # AI is O, Player is X
