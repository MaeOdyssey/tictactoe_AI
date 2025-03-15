import math
import random

class Minimax:
    def __init__(self, board, ai_symbol, player_symbol):
        """Initialize Minimax with board and player symbols."""
        self.board = board
        self.ai_symbol = ai_symbol
        self.player_symbol = player_symbol

    def find_best_move(self):
        """Finds the best possible move, but sometimes makes a 'human-like' mistake."""
        best_move = max(
            self.get_empty_cells(),
            key=lambda move: self._simulate_move(*move, 0, False),
            default=None
        )
        
        # 20% chance of making a suboptimal move (adds personality)
        if random.random() < 0.2 and len(self.get_empty_cells()) > 1:
            print("DEBUG: AI is glitching! Choosing a random move instead.")
            return random.choice(self.get_empty_cells())

        return best_move

    def get_empty_cells(self):
        """Returns a prioritized list of empty cell positions for better Minimax efficiency."""
        priority_moves = [(1, 1),  # Center
                        (0, 0), (0, 2), (2, 0), (2, 2),  # Corners
                        (0, 1), (1, 0), (1, 2), (2, 1)]  # Edges

        return [move for move in priority_moves if self.board.grid[move[0]][move[1]] == " "]


    def _simulate_move(self, row, col, depth, is_maximizing):
        """Simulates a move and evaluates its Minimax score."""
        self.board.grid[row][col] = self.ai_symbol if is_maximizing else self.player_symbol
        score = self._minimax(depth + 1, not is_maximizing)
        self.board.grid[row][col] = " "  # Undo move

        print(f"DEBUG: Simulating move at ({row}, {col}) - Depth {depth} - Score {score}")
    
        return score


    def _minimax(self, depth, is_maximizing):
        """Minimax algorithm for optimal move calculation with depth limiting."""
        winner = self._check_winner()
        if winner or self._is_draw() or depth >= 3:  # ✅ Stop after depth 3
            final_score = 10 - depth if winner == self.ai_symbol else -10 + depth if winner == self.player_symbol else 0
            return final_score

        best_score = -math.inf if is_maximizing else math.inf
        for r, c in self.get_empty_cells():
            score = self._simulate_move(r, c, depth, is_maximizing)
            best_score = max(best_score, score) if is_maximizing else min(best_score, score)

        return best_score



    def _check_winner(self):
        """Checks if there is a winner."""
        grid = self.board.grid
        for i in range(3):
            # Check rows
            if grid[i][0] == grid[i][1] == grid[i][2] != " ":
                return grid[i][0]
            # Check columns
            if grid[0][i] == grid[1][i] == grid[2][i] != " ":
                return grid[0][i]

        # Check diagonals
        if grid[0][0] == grid[1][1] == grid[2][2] != " ":
            return grid[0][0]
        if grid[0][2] == grid[1][1] == grid[2][0] != " ":
            return grid[0][2]

        return None

    def _is_draw(self):
        """Checks if the game is a draw."""
        return all(cell != " " for row in self.board.grid for cell in row)
