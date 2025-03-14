import pygame
from graphics import draw_x, draw_o

class Board:
    def __init__(self):
        """Initialize a 3x3 empty board."""
        self.grid = [[" " for _ in range(3)] for _ in range(3)]

    def make_move(self, row, col, symbol):
        """Places a move on the board if the spot is empty."""
        if self.grid[row][col] == " ":
            self.grid[row][col] = symbol
            return True
        return False

    def draw_pieces(self, screen):
        """Draws all Xs and Os on the board."""
        for row in range(3):
            for col in range(3):
                if self.grid[row][col] == "X":
                    draw_x(screen, row, col)
                elif self.grid[row][col] == "O":
                    draw_o(screen, row, col)
