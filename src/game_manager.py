from board import Board
from ai_base import AIBase

def prepare_new_game(game):
    """Resets the game properly after a win/draw."""
    print("DEBUG: Resetting board and clearing game state...")  
    game.board = Board()  # Reset board
    game.rules.board = game.board  
    game.ai = AIBase(game.ai_symbol, game.player_symbol, game.board)

    game.current_player = "X"  
    game.game_over = False  
    game.draw_streak = 0  
    game.glitches_active = False  

    print(f"DEBUG: AI reinitialized. AI Symbol: {game.ai_symbol}, Player Symbol: {game.player_symbol}")

    # Force the screen to visually update immediately
    game.board.render(game.screen)  
