import pygame
from graphics import draw_board, draw_pieces  

class Board:
    def __init__(self):
        """Initialize a blank 3x3 Tic-Tac-Toe board."""
        self.grid = [[" " for _ in range(3)] for _ in range(3)]

    def render(self, screen):
        """Draws the board and pieces using graphics module."""
        draw_board(screen)  # Draw the grid
        draw_pieces(screen, self.grid)  # Draw Xs and Os
        pygame.display.flip()  # Ensure the screen updates

    def make_move(self, row, col, symbol):
        """Places a move on the board if the cell is empty."""
        if self.grid[row][col] == " ":
            self.grid[row][col] = symbol
            return True  # Move was successful
        return False  # Move was invalid
