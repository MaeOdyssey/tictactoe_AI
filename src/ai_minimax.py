import math

class Minimax:
    def __init__(self, board, ai_symbol, player_symbol):
        """Initialize Minimax with board and player symbols."""
        self.board = board
        self.ai_symbol = ai_symbol
        self.player_symbol = player_symbol

    def find_best_move(self):
        """Finds the best possible move."""
        return max(
            [(r, c) for r in range(3) for c in range(3) if self.board.grid[r][c] == " "],
            key=lambda move: self._simulate_move(*move, 0, False),
            default=None
        )

    def _simulate_move(self, row, col, depth, is_maximizing):
        """Simulates a move and evaluates its Minimax score."""
        self.board.grid[row][col] = self.ai_symbol if is_maximizing else self.player_symbol
        score = self._minimax(depth + 1, not is_maximizing)
        self.board.grid[row][col] = " "
        return score

    def _minimax(self, depth, is_maximizing):
        """Minimax algorithm for optimal move calculation."""
        winner = self._check_winner()
        if winner or self._is_draw():
            return 10 - depth if winner == self.ai_symbol else depth - 10 if winner == self.player_symbol else 0

        return max(
            (self._simulate_move(r, c, depth, is_maximizing) for r in range(3) for c in range(3) if self.board.grid[r][c] == " "),
            default=-math.inf if is_maximizing else math.inf
        )

    def _check_winner(self):
        """Checks if there is a winner."""
        grid = self.board.grid
        for i in range(3):
            if grid[i][0] == grid[i][1] == grid[i][2] != " " or grid[0][i] == grid[1][i] == grid[2][i] != " ":
                return grid[i][0] if grid[i][0] != " " else grid[0][i]

        if grid[0][0] == grid[1][1] == grid[2][2] != " " or grid[0][2] == grid[1][1] == grid[2][0] != " ":
            return grid[1][1]  

        return None

    def _is_draw(self):
        """Checks if the game is a draw."""
        return all(cell != " " for row in self.board.grid for cell in row)
