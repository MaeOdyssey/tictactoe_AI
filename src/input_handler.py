from turn_manager import process_turn
from game_manager import prepare_new_game

def handle_click(game, pos):
    """Handles user clicks and game flow."""
    if game.game_over:
        print("DEBUG: Click ignored because game is over.")  # ✅ Check if game is stopping clicks
        return

    print(f"DEBUG: Click registered at {pos}")  # ✅ Ensure clicks are detected

    row, col = pos[1] // 200, pos[0] // 200
    if game.board.make_move(row, col, game.current_player):
        print(f"DEBUG: {game.current_player} made a move at ({row}, {col})")  # ✅ Move is happening

        if process_turn(game):  # If game is over, reset it
            print("DEBUG: Game ended, preparing new game...")  # ✅ Should only appear when game should reset
            prepare_new_game(game)
