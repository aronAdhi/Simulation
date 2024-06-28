import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display (optional, as we're focusing on sound)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Play Sound on Key Press")

# Load the sound file
try:
    sound = pygame.mixer.Sound("sound_effects//hit.wav")  # Replace with your sound file
except pygame.error as e:
    print(f"Cannot load sound: {e}")
    pygame.quit()
    sys.exit()

# Initialize the clock for controlling the frame rate
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Play the sound on key press
            sound.play()

    # Fill the screen with a color (optional)
    screen.fill((30, 30, 30))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
