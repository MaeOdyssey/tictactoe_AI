import pygame
from game_logic import Game
from graphics import draw_board
from input_handler import handle_click

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("AI-Powered Tic-Tac-Toe")

# Create Game Object
game = Game(screen)

running = True
while running:
    screen.fill((200, 200, 200))  # Grey background
    draw_board(screen)  # Draw the board
    game.board.draw_pieces(screen)  # Draw Xs and Os

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            handle_click(game, event.pos)  # Process clicks

    pygame.display.flip()  # Update screen

pygame.quit()
