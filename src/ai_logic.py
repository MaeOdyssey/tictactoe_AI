from ai_base import AIBase
from ai_dialogue import AIDialogue

class AI:
    def __init__(self, ai_symbol, player_symbol, board):
        """Combines AI move logic and AI dialogue."""
        self.ai_core = AIBase(ai_symbol, player_symbol, board)
        self.ai_dialogue = AIDialogue()

    def get_best_move(self):
        """Delegates move decision to AIBase."""
        return self.ai_core.get_best_move()

    def get_ai_response(self, game_state):
        """Gets AI's sassy response."""
        return self.ai_dialogue.get_response(game_state)
