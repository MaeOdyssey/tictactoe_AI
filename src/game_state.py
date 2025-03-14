from effects import show_message

def check_game_end(game):
    """Checks for win, draw, or glitch activation."""
    winner = game.rules.check_winner()
    if winner:
        show_message(game.screen, f"{winner} WINS!")
        game.game_over = True
        return True  

    if game.rules.is_draw():
        game.draw_streak += 1
        if game.draw_streak == 2 and not game.glitches_active:
            show_message(game.screen, "WARNING: Reality Distorting...")
            import glitch_manager  # Import here to break circular dependency
            glitch_manager.activate_glitches(game)
        else:
            show_message(game.screen, "It's a DRAW!")
        
        game.game_over = True
        return True  

    return False  #  Game continues
