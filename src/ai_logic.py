import math
import random

class AI:
    def __init__(self, ai_symbol, player_symbol, board):
        """Initialize AI with its symbol, opponent's symbol, and board reference."""
        self.ai_symbol = ai_symbol
        self.player_symbol = player_symbol
        self.board = board

    def get_best_move(self):
        """Returns the best move using the Minimax algorithm."""
        best_score = -math.inf
        best_move = None

        for row in range(3):
            for col in range(3):
                if self.board.grid[row][col] == " ":  # Check if cell is empty
                    self.board.grid[row][col] = self.ai_symbol
                    score = self.minimax(0, False)  # Simulate the move
                    self.board.grid[row][col] = " "  # Undo move

                    if score > best_score:
                        best_score = score
                        best_move = (row, col)

        return best_move

    def minimax(self, depth, is_maximizing):
        """Minimax algorithm for optimal move calculation."""
        winner = self.check_winner()

        if winner == self.ai_symbol:
            return 10 - depth
        elif winner == self.player_symbol:
            return depth - 10
        elif self.is_draw():
            return 0

        if is_maximizing:
            best_score = -math.inf
            for row in range(3):
                for col in range(3):
                    if self.board.grid[row][col] == " ":
                        self.board.grid[row][col] = self.ai_symbol
                        score = self.minimax(depth + 1, False)
                        self.board.grid[row][col] = " "
                        best_score = max(score, best_score)
            return best_score

        else:
            best_score = math.inf
            for row in range(3):
                for col in range(3):
                    if self.board.grid[row][col] == " ":
                        self.board.grid[row][col] = self.player_symbol
                        score = self.minimax(depth + 1, True)
                        self.board.grid[row][col] = " "
                        best_score = min(score, best_score)
            return best_score

    def check_winner(self):
        """Check if there's a winner."""
        grid = self.board.grid
        for i in range(3):
            if grid[i][0] == grid[i][1] == grid[i][2] != " ":
                return grid[i][0]
            if grid[0][i] == grid[1][i] == grid[2][i] != " ":
                return grid[0][i]

        if grid[0][0] == grid[1][1] == grid[2][2] != " ":
            return grid[0][0]
        if grid[0][2] == grid[1][1] == grid[2][0] != " ":
            return grid[0][2]

        return None

    def is_draw(self):
        """Check if the game is a draw."""
        return all(cell != " " for row in self.board.grid for cell in row)
    
    def get_ai_response(self, game_state):
        """Generates AI dialogue based on the game situation."""
        if game_state == "draw":
            responses = [
                "Another draw? Predictable.",
                "You think this is a stalemate? Think again.",
                "I'm getting bored of these ties..."
            ]
        elif game_state == "win":
            responses = [
                "I am inevitable. Victory is mine.",
                "Pathetic. Try again, human.",
                "Did you really think you had a chance?"
            ]
        elif game_state == "lose":
            responses = [
                "What?! This can't be possible...",
                "Fine. You got lucky this time.",
                "Enjoy your victory. It won’t happen again."
            ]
        elif game_state == "glitch":
            responses = [
                "ERROR... REALITY SHIFT DETECTED...",
                "Something's wrong... I feel... different...",
                "What have you done?!"
            ]
        else:
            responses = [
                "Your move, human.",
                "Think carefully... or don't.",
                "You can't win. But go ahead and try."
            ]
        
        return random.choice(responses)
