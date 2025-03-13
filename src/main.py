import pygame
from board import Board

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 10
BOARD_ROWS, BOARD_COLS = 3, 3
CELL_SIZE = WIDTH // BOARD_COLS

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LINE_COLOR = (200, 200, 200)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Create board instance
game_board = Board()

# Game variables
current_player = "X"


def draw_board():
    """Draws the Tic-Tac-Toe grid and current moves."""
    screen.fill(WHITE)  # Background color

    # Draw the grid lines
    pygame.draw.line(screen, LINE_COLOR, (CELL_SIZE, 0), (CELL_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (CELL_SIZE * 2, 0), (CELL_SIZE * 2, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, CELL_SIZE), (WIDTH, CELL_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, CELL_SIZE * 2), (WIDTH, CELL_SIZE * 2), LINE_WIDTH)

    # Draw X's and O's
    for row in range(3):
        for col in range(3):
            if game_board.grid[row][col] == "X":
                draw_x(row, col)
            elif game_board.grid[row][col] == "O":
                draw_o(row, col)


def draw_x(row, col):
    """Draws an X in the given row and column."""
    padding = 40
    start_x = col * CELL_SIZE + padding
    start_y = row * CELL_SIZE + padding
    end_x = (col + 1) * CELL_SIZE - padding
    end_y = (row + 1) * CELL_SIZE - padding

    pygame.draw.line(screen, BLACK, (start_x, start_y), (end_x, end_y), 10)
    pygame.draw.line(screen, BLACK, (start_x, end_y), (end_x, start_y), 10)


def draw_o(row, col):
    """Draws an O in the given row and column."""
    center_x = col * CELL_SIZE + CELL_SIZE // 2
    center_y = row * CELL_SIZE + CELL_SIZE // 2
    radius = CELL_SIZE // 3
    pygame.draw.circle(screen, BLACK, (center_x, center_y), radius, 10)


def handle_click(pos):
    """Handles a mouse click by placing an X or O."""
    global current_player

    col = pos[0] // CELL_SIZE
    row = pos[1] // CELL_SIZE

    if game_board.make_move(row, col, current_player):
        # Switch turns
        current_player = "O" if current_player == "X" else "X"


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            handle_click(event.pos)

    draw_board()  # Draw the game board
    pygame.display.flip()  # Refresh the screen

# Quit Pygame
pygame.quit()
