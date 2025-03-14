import math
from ai_minimax import Minimax

class AIBase:
    def __init__(self, ai_symbol, player_symbol, board):
        """Initialize AI with its symbol, opponent's symbol, and board reference."""
        self.ai_symbol = ai_symbol
        self.player_symbol = player_symbol
        self.board = board
        self.minimax = Minimax(board, ai_symbol, player_symbol)

    def get_best_move(self):
        """Returns the best move based on Minimax evaluation."""
        return self.minimax.find_best_move()
