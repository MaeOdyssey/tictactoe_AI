from effects import show_message
from ai_logic import AI
import random

def activate_glitches(game):
    """Triggers game distortions when AI 'gets frustrated'."""
    print("DEBUG: 🌀 Glitch function activated!")  
    game.glitches_active = True
    show_message(game.screen, "WARNING: Reality Distorting... Symbols Reconfiguring...")

    swap_symbols(game)  # ✅ Swap AI and Player symbols
    apply_random_glitch(game)  # ✅ Pick a random game-changing effect

    game.draw_streak = 0  # ✅ Reset draw count

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
