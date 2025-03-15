class GameRules:
    def __init__(self, board):
        """Initialize with the game board."""
        self.board = board

    def check_winner(self):
        """Checks for a winner and returns 'X', 'O', or None if no winner yet."""
        grid = self.board.grid
        lines = (
            [grid[i] for i in range(3)] +                # Rows
            [[grid[0][i], grid[1][i], grid[2][i]] for i in range(3)] +  # Columns
            [[grid[0][0], grid[1][1], grid[2][2]],       # Main diagonal
            [grid[0][2], grid[1][1], grid[2][0]]]       # Anti-diagonal
        )

        for line in lines:
            if line[0] == line[1] == line[2] != " ":
                return line[0]  # Return the winning symbol

        return None  # No winner yet


    def is_draw(self):
        """Checks if the board is full (no empty spaces) and there's no winner."""
        if self.check_winner():
            return False  # If there's a winner, it's not a draw
        return all(cell != " " for row in self.board.grid for cell in row)
