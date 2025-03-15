# Remove the incorrect import
from game_state import check_game_end

def process_turn(game, pos):
    """Handles the player's move and AI response."""
    row, col = pos[1] // 200, pos[0] // 200  # Convert click position to grid coordinates

    if not game.board.make_move(row, col, game.current_player):  
        return False  # Invalid move (cell already occupied)

    game.total_turns += 1  # Track total turns
    print(f"DEBUG: Total Turns: {game.total_turns}")  # Debugging

    if check_game_end(game):  
        return True  # Game ended, no need for AI move

    handle_ai_turn(game)  # AI takes its turn
    game.board.render(game.screen)  # Ensure board updates after AI move
    return game.game_over  


def handle_ai_turn(game):
    """Handles AI's turn after player moves."""
    print(f"DEBUG: AI is moving...")
    ai_move = game.ai.get_best_move()
    
    if ai_move:
        game.board.make_move(ai_move[0], ai_move[1], game.ai_symbol)

    check_game_end(game)  # Check again after AI moves
    game.board.render(game.screen)  # Ensure AI's move is visible
    print(f"DEBUG: Switching back to player turn.")
    game.current_player = game.player_symbol
