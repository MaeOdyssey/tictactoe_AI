import pygame
from board import Board
from ai_base import AIBase  # Import AIBase instead of AI
from game_rules import GameRules
from effects import show_message
from glitch_manager import activate_glitches
from game_manager import prepare_new_game
from input_handler import process_turn

class Game:
    def __init__(self, screen):
        """Initialize the game with board, rules, and AI."""
        self.screen = screen
        self.board = Board()
        self.rules = GameRules(self.board)
        self.current_player = "X"
        self.ai_symbol = "O"
        self.player_symbol = "X"
        self.game_over = False
        self.draw_streak = 0
        self.glitches_active = False
        self.ai_wins = 0
        self.player_wins = 0
        self.total_turns = 0
        self.ai = AIBase(self.ai_symbol, self.player_symbol, self.board)  # Initialize AI with correct symbols

    def process_click(self, pos):
        """Redirects click handling to the input handler and updates UI."""
        process_turn(self, pos)  # Process player move and AI response
        self.board.render(self.screen)  # Ensure the board updates after a move
