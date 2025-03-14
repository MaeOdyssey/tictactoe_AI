from ai_logic import AI
from game_rules import GameRules
from board import Board
class Game:
    def __init__(self, screen):
        """Initialize the game with board, rules, and AI."""
        self.screen = screen
        self.board = Board()
        self.rules = GameRules(self.board)
        self.current_player = "X"
        self.ai_symbol = "O"  # Default AI symbol
        self.player_symbol = "X"  # Default Player symbol
        self.game_over = False
        self.draw_streak = 0
        self.glitches_active = False
        self.ai = AI(self.ai_symbol, self.player_symbol, self.board)  
