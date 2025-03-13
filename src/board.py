class Board:
    def __init__(self):
        """Initialize an empty 3x3 Tic-Tac-Toe board."""
        self.grid = [[" " for _ in range(3)] for _ in range(3)]  # 3x3 grid
    
    def display(self):
        """Prints the board to the console (for debugging)."""
        print("\n  0 1 2")
        for i, row in enumerate(self.grid):
            print(f"{i} {'|'.join(row)}")
            if i < 2:
                print("  -----")

    def is_valid_move(self, row, col):
        """Checks if a move is valid (empty space & within bounds)."""
        return 0 <= row < 3 and 0 <= col < 3 and self.grid[row][col] == " "

    def make_move(self, row, col, player_symbol):
        """Places a move on the board if it's valid."""
        if self.is_valid_move(row, col):
            self.grid[row][col] = player_symbol
            return True
        return False

    def reset(self):
        """Clears the board."""
        self.grid = [[" " for _ in range(3)] for _ in range(3)]
