class GameRules:
    def __init__(self, board):
        """Initialize with the game board."""
        self.board = board

    def check_winner(self):
        """Checks for a winner and returns 'X', 'O', or None if no winner yet."""
        grid = self.board.grid
        # Check rows & columns
        for i in range(3):
            if grid[i][0] == grid[i][1] == grid[i][2] != " ":
                return grid[i][0]  # Row win
            if grid[0][i] == grid[1][i] == grid[2][i] != " ":
                return grid[0][i]  # Column win
        # Check diagonals
        if grid[0][0] == grid[1][1] == grid[2][2] != " ":
            return grid[0][0]  # Main diagonal
        if grid[0][2] == grid[1][1] == grid[2][0] != " ":
            return grid[0][2]  # Other diagonal

        return None  # No winner yet

    def is_draw(self):
        """Checks if the board is full (no empty spaces) and there's no winner."""
        if self.check_winner():
            return False  # If there's a winner, it's not a draw
        return all(cell != " " for row in self.board.grid for cell in row)
