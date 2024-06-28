import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mouse Drawing with Pygame")

# Colors
background_color = (255, 255, 255)  # White
drawing_color = (255, 0, 0)           # Black

# Initialize variables to track drawing state
drawing = False
last_pos = None
path = []  # To record the drawing path

# Clock to control the frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check if the mouse button is pressed
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            last_pos = event.pos  # Start drawing from the current mouse position

        # Check if the mouse button is released
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            last_pos = None  # Stop drawing

        # Check if the mouse is moved
        if event.type == pygame.MOUSEMOTION and drawing:
            current_pos = event.pos
            if last_pos:
                # Draw a line from the last position to the current position
                pygame.draw.line(screen, drawing_color, last_pos, current_pos, 3)
                path.append((last_pos, current_pos))  # Record the path
            last_pos = current_pos

    # Refresh the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()