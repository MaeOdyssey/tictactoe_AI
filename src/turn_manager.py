from effects import show_message
from glitch_manager import activate_glitches

def process_turn(game):
    """Handles AI response after player move."""
    print(f"DEBUG: Checking win condition...")
    winner = game.rules.check_winner()
    if winner:
        print(f"DEBUG: {winner} wins. Ending game.")
        show_message(game.screen, f"{winner} WINS!")
        game.game_over = True
        return True  

    print(f"DEBUG: Checking draw condition...")
    if game.rules.is_draw():
        game.draw_streak += 1
        if game.draw_streak >= 2 and not game.glitches_active:
            show_message(game.screen, "WARNING: Reality Distorting...")
            activate_glitches(game)
        else:
            show_message(game.screen, "It's a DRAW!")

        game.game_over = True
        print(f"DEBUG: Game marked as over due to draw.")
        return True  

    print(f"DEBUG: No win/draw detected. AI is moving...")
    game.current_player = game.ai_symbol
    ai_move = game.ai.get_best_move()
    if ai_move:
        game.board.make_move(ai_move[0], ai_move[1], game.ai_symbol)

    print(f"DEBUG: Checking AI's win condition...")
    winner = game.rules.check_winner()
    if winner:
        print(f"DEBUG: AI wins. Ending game.")
        show_message(game.screen, f"{winner} WINS!")
        game.game_over = True
        return True  
    elif game.rules.is_draw():
        game.draw_streak += 1
        if game.draw_streak >= 2 and not game.glitches_active:
            show_message(game.screen, "WARNING: Reality Distorting...")
            activate_glitches(game)
        else:
            show_message(game.screen, "It's a DRAW!")
        
        game.game_over = True
        print(f"DEBUG: AI caused a draw. Ending game.")
        return True  

    print(f"DEBUG: Switching back to player turn.")
    game.current_player = game.player_symbol
    return False  # ✅ Game continues normally
