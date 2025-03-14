from board import Board

def prepare_new_game(game):
    """Resets the game properly after a win/draw."""
    print("DEBUG: Resetting board and clearing game state...")  # ✅ Add debug to check if reset is working
    game.board = Board()  # Reset board
    game.rules.board = game.board  # ✅ Ensure rules are also pointing to the new board
    game.current_player = "X"  # Ensure the player starts first
    game.game_over = False  # ✅ Allow clicks again
    game.draw_streak = 0  # Reset draw count
    game.glitches_active = False  # Reset glitch state
