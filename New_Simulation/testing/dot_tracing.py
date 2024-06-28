import pygame
import sys

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

    # Move the dot using arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        dot_position[0] -= dot_speed
    if keys[pygame.K_RIGHT]:
        dot_position[0] += dot_speed
    if keys[pygame.K_UP]:
        dot_position[1] -= dot_speed
    if keys[pygame.K_DOWN]:
        dot_position[1] += dot_speed

    # Append the new position to the path
    path.append(dot_position.copy())

    # Clear the screen
    screen.fill(background_color)

    # Draw the path
    if len(path) > 1:
        pygame.draw.lines(screen, path_color, False, path, 2)

    # Draw the dot
    pygame.draw.circle(screen, dot_color, dot_position, dot_radius)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
