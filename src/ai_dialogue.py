import random

class AIDialogue:
    """Handles AI responses based on game state."""

    response_map = {
        "draw": [
            "Another draw? Predictable.",
            "You think this is a stalemate? Think again.",
            "I'm getting bored of these ties..."
        ],
        "win": [
            "I am inevitable. Victory is mine.",
            "Pathetic. Try again, human.",
            "Did you really think you had a chance?"
        ],
        "lose": [
            "What?! This can't be possible...",
            "Fine. You got lucky this time.",
            "Enjoy your victory. It won’t happen again."
        ],
        "glitch": [
            "ERROR... REALITY SHIFT DETECTED...",
            "Something's wrong... I feel... different...",
            "What have you done?!"
        ],
        "default": [
            "Your move, human.",
            "Think carefully... or don't.",
            "You can't win. But go ahead and try."
        ]
    }

    @staticmethod
    def get_ai_response(game_state, personality="normal"):
        """Generates AI dialogue based on the game state and personality."""
        response_map = {
            "draw": [
                "Another draw? Predictable.",
                "You think this is a stalemate? Think again.",
                "I'm getting bored of these ties..."
            ],
            "win": [
                "I am inevitable. Victory is mine.",
                "Pathetic. Try again, human.",
                "Did you really think you had a chance?"
            ],
            "lose": [
                "What?! This can't be possible...",
                "Fine. You got lucky this time.",
                "Enjoy your victory. It won’t happen again."
            ],
            "glitch": [
                "ERROR... REALITY SHIFT DETECTED...",
                "Something's wrong... I feel... different...",
                "What have you done?!"
            ],
            "default": [
                "Your move, human.",
                "Think carefully... or don't.",
                "You can't win. But go ahead and try."
            ]
        }

        # If AI is glitchy, responses get weirder
        if personality == "glitchy":
            response_map["default"] = [
                "YOU... CANNOT... ESCAPE...",
                "REALITY... COLLAPSING...",
                "I SEE... EVERYTHING..."
            ]

        return random.choice(response_map.get(game_state, response_map["default"]))
