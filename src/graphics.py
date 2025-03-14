import pygame

def draw_board(screen):
    """Draws a properly scaled Tic-Tac-Toe board."""
    screen.fill((200, 200, 200))  # Grey background

    width, height = screen.get_size()
    third_w, third_h = width // 3, height // 3

    # Vertical lines
    pygame.draw.line(screen, (0, 0, 0), (third_w, 0), (third_w, height), 5)
    pygame.draw.line(screen, (0, 0, 0), (2 * third_w, 0), (2 * third_w, height), 5)

    # Horizontal lines
    pygame.draw.line(screen, (0, 0, 0), (0, third_h), (width, third_h), 5)
    pygame.draw.line(screen, (0, 0, 0), (0, 2 * third_h), (width, 2 * third_h), 5)

def draw_pieces(screen, grid):
    """Draws Xs and Os based on the board state."""
    for row in range(3):
        for col in range(3):
            if grid[row][col] == "X":
                draw_x(screen, row, col)
            elif grid[row][col] == "O":
                draw_o(screen, row, col)

def draw_x(screen, row, col):
    """Draws an 'X' in the given board cell."""
    x, y = col * 200 + 100, row * 200 + 100
    pygame.draw.line(screen, (255, 0, 0), (x - 50, y - 50), (x + 50, y + 50), 5)
    pygame.draw.line(screen, (255, 0, 0), (x - 50, y + 50), (x + 50, y - 50), 5)

def draw_o(screen, row, col):
    """Draws an 'O' in the given board cell."""
    x, y = col * 200 + 100, row * 200 + 100
    pygame.draw.circle(screen, (0, 0, 255), (x, y), 50, 5)
