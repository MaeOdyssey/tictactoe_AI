from effects import show_message
from glitch_manager import activate_glitches

def check_game_end(game):
    """Checks if the game has ended and triggers glitches if needed."""
    winner = game.rules.check_winner()

    if winner:
        print(f"DEBUG: {winner} wins. Ending game.")  
        
        if winner == game.ai_symbol:
            game.ai_wins += 1  # Count AI wins
            game.player_wins = 0  # Reset Player win streak
        else:
            game.player_wins += 1  # Count Player wins
            game.ai_wins = 0  # Reset AI win streak

        game.total_turns = 0  # Reset turn counter on win
        print(f"DEBUG: AI Wins: {game.ai_wins}, Player Wins: {game.player_wins}, Total Turns: {game.total_turns}")  
        show_message(game.screen, f"{winner} WINS!")
        game.game_over = True

        # Glitch triggers when either wins TWICE IN A ROW
        if game.ai_wins >= 2 or game.player_wins >= 2:
            print(f"DEBUG: AI is FRUSTRATED! Activating glitches...")  
            activate_glitches(game)  
            game.ai_wins = 0  # Reset AI frustration counter
            game.player_wins = 0  # Reset Player win counter

        return True  

    if game.rules.is_draw():
        game.draw_streak += 1
        print(f"DEBUG: Draw streak is now {game.draw_streak}")  

        # Glitch triggers when TWO DRAWS happen in a row
        if game.draw_streak >= 2:
            print(f"DEBUG: TOO MANY DRAWS! AI is altering reality!")  
            activate_glitches(game)  
            game.draw_streak = 0  # Reset draw counter

        show_message(game.screen, "It's a DRAW!")
        game.game_over = True
        return True  

    return False  # Continue game normally
