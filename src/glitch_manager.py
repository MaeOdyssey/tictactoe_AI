from effects import show_message
from ai_logic import AI

def activate_glitches(game):
    """Triggers game distortions when AI 'gets frustrated'."""
    game.glitches_active = True
    show_message(game.screen, "WARNING: Reality Distorting... Symbols Reconfiguring...")

    # Swap AI and Player symbols
    game.ai_symbol, game.player_symbol = game.player_symbol, game.ai_symbol
    game.ai = AI(game.ai_symbol, game.player_symbol, game.board)

    # Introduce game twists
    game.board.swap_random_pieces()
    game.board.shift_board()

    game.draw_streak = 0  # Reset draw count
