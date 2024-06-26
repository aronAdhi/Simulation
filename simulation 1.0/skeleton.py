# main.py

import pygame
import matplotlib.pyplot as plt
from screen_config import *
from dot import Dot
from box import Box
import dot_logic
import box_logic
import utility

# Initialize Pygame
pygame.init()

# Setup the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Dots and Boxes Simulation')

# Create dots and boxes
dots = [Dot(radius, color=dot_color, speed=dot_speed) for _ in range(num_dots)]
boxes = [Box(width, color=box_color, speed=box_speed) for _ in range(num_boxes)]

# Trackers for the number of dots and boxes per frame
dots_count = []
boxes_count = []

font = pygame.font.SysFont('Arial', 24)

# Simulation loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(BLACK)

    # Run the simulation step
    utility.run_simulation_step(screen, dots, boxes, dot_logic, box_logic, max_dot_age, max_box_age, hunger_threshold)

    # Record the number of dots and boxes
    dots_count.append(len(dots))
    boxes_count.append(len(boxes))

    # Render the text for counts
    dots_text = font.render(f'Dots: {len(dots)}', True, (255, 255, 255))
    boxes_text = font.render(f'Boxes: {len(boxes)}', True, (255, 255, 255))

    # Blit the text on the screen
    screen.blit(dots_text, (10, 10))
    screen.blit(boxes_text, (10, 40))

    # Update display
    pygame.display.flip()
    clock.tick(FPS)  # Limit to 30 frames per second

# Quit Pygame
pygame.quit()

# Plotting the number of dots and boxes over time
plt.figure(figsize=(10, 5))
plt.plot(dots_count, label='Number of Dots', color='red')
plt.plot(boxes_count, label='Number of Boxes', color='green')
plt.xlabel('Frames')
plt.ylabel('Count')
plt.title('Number of Dots and Boxes Over Time')
plt.legend()
plt.grid(True)
plt.show()


