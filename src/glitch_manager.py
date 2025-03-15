from effects import show_message
from ai_base import AIBase
import random

def activate_glitches(game):
    """Triggers game distortions when AI 'gets frustrated'."""
    print("DEBUG: 🌀 Glitch function activated!")  # ✅ Confirm function is running
    game.glitches_active = True

    # ✅ Before swap, print current symbols
    print(f"DEBUG: Before swap -> Player: {game.player_symbol}, AI: {game.ai_symbol}")

    # Ensure AI and Player always have different symbols
    if game.player_symbol == "X":
        game.player_symbol, game.ai_symbol = "O", "X"
    else:
        game.player_symbol, game.ai_symbol = "X", "O"

    # ✅ After swap, print new symbols
    print(f"DEBUG: After swap -> Player: {game.player_symbol}, AI: {game.ai_symbol}")

    # ✅ Update the AI with the correct new symbols
    game.ai = AIBase(game.ai_symbol, game.player_symbol, game.board)

    # Introduce a random glitch effect (either swap pieces OR shift board, not both)
    if random.choice([True, False]):
        print("DEBUG: AI is swapping random pieces!")  
        swap_random_pieces(game)
    else:
        print("DEBUG: The board shifts!")  
        shift_board(game)

    game.draw_streak = 0  # Reset draw count
    game.ai_wins = 0  # Reset AI win count

    show_message(game.screen, "WARNING: Reality Distorting...")  # ✅ Add visual feedback

def swap_symbols(game):
    """Swaps AI and Player symbols properly and re-initializes AI."""
    print(f"DEBUG: Before swap -> Player: {game.player_symbol}, AI: {game.ai_symbol}")

    game.player_symbol, game.ai_symbol = game.ai_symbol, game.player_symbol  # ✅ Swap them
    game.ai = AI(game.ai_symbol, game.player_symbol, game.board)  # ✅ Update AI

    print(f"DEBUG: After swap -> Player: {game.player_symbol}, AI: {game.ai_symbol}")

def apply_random_glitch(game):
    """Applies a random game glitch (either swap pieces or shift board)."""
    glitch_choice = random.choice(["swap_pieces", "shift_board"])

    if glitch_choice == "swap_pieces":
        print("DEBUG: AI is swapping random pieces!")  
        game.board.swap_random_pieces()
    else:
        print("DEBUG: The board shifts!")  
        game.board.shift_board()

def shift_board(game):
    """Shifts board pieces randomly to create a 'glitch' effect."""
    grid = game.board.grid  # Correctly reference the board's grid

    # Create an empty new grid
    new_grid = [[" " for _ in range(3)] for _ in range(3)]

    # Get all occupied positions
    positions = [(r, c) for r in range(3) for c in range(3) if grid[r][c] != " "]
    random.shuffle(positions)  # Mix up positions

    # Reassign pieces to new locations
    for (new_r, new_c), (old_r, old_c) in zip(positions, positions):
        new_grid[new_r][new_c] = grid[old_r][old_c]  

    # Apply the new shuffled board
    game.board.grid = new_grid  

    print("DEBUG: Board shifted due to glitches!")  # Debug message

def swap_random_pieces(game):
    """Swaps two random pieces on the board to simulate a glitch effect."""
    positions = [(r, c) for r in range(3) for c in range(3) if game.board.grid[r][c] != " "]
    
    if len(positions) >= 2:
        (r1, c1), (r2, c2) = random.sample(positions, 2)  # Pick two random filled positions
        game.board.grid[r1][c1], game.board.grid[r2][c2] = game.board.grid[r2][c2], game.board.grid[r1][c1]  # Swap them

        print(f"DEBUG: Swapped pieces at ({r1}, {c1}) and ({r2}, {c2})")  # Debug message