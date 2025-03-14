from game_state import check_game_end
from board import Board

def process_turn(game, row=None, col=None):
    """Handles the player's move and AI response."""
    
    if row is not None and col is not None:  #  Player move
        if not game.board.make_move(row, col, game.current_player):  # Call from Board
            return False  # Invalid move

    if check_game_end(game):  # Checks for win/draw/glitches
        return True  

    handle_ai_turn(game)  #  AI's move
    return game.game_over  

def handle_ai_turn(game):
    """Handles AI's turn after player moves."""
    print(f"DEBUG: AI is moving...")
    ai_move = game.ai.get_best_move()
    
    if ai_move:
        game.board.make_move(ai_move[0], ai_move[1], game.ai_symbol)  #  Call from Board

    check_game_end(game)  # Check again after AI moves
    print(f"DEBUG: Switching back to player turn.")
    game.current_player = game.player_symbol
