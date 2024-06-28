import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Simulation parameters
num_rabbits = 20
num_foxes = 5
rabbit_size = 10
fox_size = 15
rabbit_speed = 2
fox_speed = 3
predation_distance = 20

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fox and Rabbit Simulation")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Initialize rabbit and fox positions
rabbits = [{'x': random.randint(0, SCREEN_WIDTH),
            'y': random.randint(0, SCREEN_HEIGHT)} for _ in range(num_rabbits)]

foxes = [{'x': random.randint(0, SCREEN_WIDTH),
          'y': random.randint(0, SCREEN_HEIGHT)} for _ in range(num_foxes)]

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Update positions of rabbits
    for rabbit in rabbits:
        rabbit['x'] += random.randint(-rabbit_speed, rabbit_speed)
        rabbit['y'] += random.randint(-rabbit_speed, rabbit_speed)
        # Ensure rabbits stay within bounds
        rabbit['x'] = max(0, min(SCREEN_WIDTH, rabbit['x']))
        rabbit['y'] = max(0, min(SCREEN_HEIGHT, rabbit['y']))

    # Update positions of foxes
    for fox in foxes:
        fox['x'] += random.randint(-fox_speed, fox_speed)
        fox['y'] += random.randint(-fox_speed, fox_speed)
        # Ensure foxes stay within bounds
        fox['x'] = max(0, min(SCREEN_WIDTH, fox['x']))
        fox['y'] = max(0, min(SCREEN_HEIGHT, fox['y']))

    # Check for predation
    for fox in foxes:
        for rabbit in rabbits:
            # Calculate distance between fox and rabbit
            distance = ((fox['x'] - rabbit['x'])**2 + (fox['y'] - rabbit['y'])**2)**0.5
            if distance < predation_distance:
                # Fox catches rabbit
                rabbits.remove(rabbit)
                break  # One rabbit caught per fox per frame

    # Draw rabbits
    for rabbit in rabbits:
        pygame.draw.circle(screen, WHITE, (rabbit['x'], rabbit['y']), rabbit_size)

    # Draw foxes
    for fox in foxes:
        pygame.draw.circle(screen, RED, (fox['x'], fox['y']), fox_size)

    # Display population counts
    rabbit_count = len(rabbits)
    fox_count = len(foxes)
    font = pygame.font.Font(None, 36)
    rabbit_text = font.render(f"Rabbits: {rabbit_count}", True, WHITE)
    fox_text = font.render(f"Foxes: {fox_count}", True, RED)
    screen.blit(rabbit_text, (20, 20))
    screen.blit(fox_text, (20, 60))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Quit pygame
pygame.quit()
