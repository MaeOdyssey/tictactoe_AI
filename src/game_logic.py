import pygame
from board import Board
from ai_logic import AI
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
        self.ai = AI(self.ai_symbol, self.player_symbol, self.board)

    def process_click(self, pos):
        """Redirects click handling to the input handler."""
        handle_click(self, pos)
    
