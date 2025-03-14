import pygame

def show_message(screen, message):
    """Displays a message on the screen."""
    font = pygame.font.Font(None, 40)
    screen.fill((255, 255, 255))  # Clear screen

    text = font.render(message, True, (255, 0, 0))
    text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    screen.blit(text, text_rect)

    pygame.display.flip()
    pygame.time.delay(2500)
