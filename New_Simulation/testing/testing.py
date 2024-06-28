import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Dot with Path Recording")

# Colors
background_color = (0, 0, 0)  # Black
dot_color = (255, 0, 0)       # Red
path_color = (0, 255, 0)      # Green

# Dot properties
dot_radius = 5
dot_position = [screen_width // 2, screen_height // 2]
dot_speed = 5

# List to record the path
path = [dot_position.copy()]

# Clock to control the frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    cx = 400
    cy = 300
    direction = 30 
    r = 50       

    pygame.draw.polygon(screen, (255, 0, 0), 
                            [[cx + r * math.sin(direction) , cy + r * math.cos(direction)], 
                             [cx + r * math.sin(direction+2.5) , cy + r * math.cos(direction+2.5)],
                             [cx + r * math.sin(direction-2.5) , cy + r * math.cos(direction-2.5)]])
    # Draw the dot
    pygame.draw.circle(screen, dot_color, dot_position, dot_radius)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
