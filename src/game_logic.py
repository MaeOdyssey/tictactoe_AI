import pygame
from board import Board
from game_rules import GameRules

class Game:
    def __init__(self, screen):
        """Initialize the game with board, rules, and game state."""
        self.screen = screen
        self.board = Board()
        self.rules = GameRules(self.board)
        self.current_player = "X"
        self.game_over = False

    def draw_board(self):
        """Draws the Tic-Tac-Toe grid and pieces."""
        self.screen.fill((255, 255, 255))  # White background
        line_color = (200, 200, 200)
        cell_size = self.screen.get_width() // 3

        # Draw grid lines
        pygame.draw.line(self.screen, line_color, (cell_size, 0), (cell_size, self.screen.get_height()), 10)
        pygame.draw.line(self.screen, line_color, (cell_size * 2, 0), (cell_size * 2, self.screen.get_height()), 10)
        pygame.draw.line(self.screen, line_color, (0, cell_size), (self.screen.get_width(), cell_size), 10)
        pygame.draw.line(self.screen, line_color, (0, cell_size * 2), (self.screen.get_width(), cell_size * 2), 10)

        # Draw X’s and O’s
        for row in range(3):
            for col in range(3):
                if self.board.grid[row][col] == "X":
                    self.draw_x(row, col)
                elif self.board.grid[row][col] == "O":
                    self.draw_o(row, col)

    def draw_x(self, row, col):
        """Draws an X in the given row and column."""
        padding = 40
        cell_size = self.screen.get_width() // 3
        start_x = col * cell_size + padding
        start_y = row * cell_size + padding
        end_x = (col + 1) * cell_size - padding
        end_y = (row + 1) * cell_size - padding

        pygame.draw.line(self.screen, (0, 0, 0), (start_x, start_y), (end_x, end_y), 10)
        pygame.draw.line(self.screen, (0, 0, 0), (start_x, end_y), (end_x, start_y), 10)

    def draw_o(self, row, col):
        """Draws an O in the given row and column."""
        cell_size = self.screen.get_width() // 3
        center_x = col * cell_size + cell_size // 2
        center_y = row * cell_size + cell_size // 2
        radius = cell_size // 3
        pygame.draw.circle(self.screen, (0, 0, 0), (center_x, center_y), radius, 10)

    def handle_click(self, pos):
        """Handles a mouse click by placing an X or O."""
        if self.game_over:
            return  # Ignore clicks after game over

        cell_size = self.screen.get_width() // 3
        col = pos[0] // cell_size
        row = pos[1] // cell_size

        if self.board.make_move(row, col, self.current_player):
            winner = self.rules.check_winner()
            if winner:
                print(f"{winner} WINS!")  # Will replace with visual text later
                self.game_over = True
            elif self.rules.is_draw():
                print("It's a DRAW!")  # Will replace with visual text later
                self.game_over = True
            else:
                # Switch turns if the game is still going
                self.current_player = "O" if self.current_player == "X" else "X"
