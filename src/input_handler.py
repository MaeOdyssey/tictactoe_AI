from turn_handler import process_turn
from game_manager import prepare_new_game

def handle_click(game, pos):
    """Handles user clicks and game flow."""
    if game.game_over:
        print("DEBUG: Click ignored because game is over.")  
        return

    print(f"DEBUG: Click registered at {pos}")  

    row, col = pos[1] // 200, pos[0] // 200

    if process_turn(game, pos):  # Uses new turn handler
        print("DEBUG: Game ended, preparing new game...")
        prepare_new_game(game)  
