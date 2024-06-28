import pygame
import sys
import math

# Initialize PyGame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Gravitational constant (scaled for simulation)
G = 1.0

# Body class to encapsulate properties and behaviors
class Body:
    def __init__(self, pos, vel, mass, color):
        self.pos = pos  # Position as [x, y]
        self.vel = vel  # Velocity as [vx, vy]
        self.mass = mass
        self.color = color
        self.radius = int(mass)  # Simple scaling of radius with mass
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.pos[0]), int(self.pos[1])), self.radius)
    
    def update_position(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

# Function to calculate the gravitational force between two bodies
def calculate_gravitational_force(body1, body2):
    dx = body2.pos[0] - body1.pos[0]
    dy = body2.pos[1] - body1.pos[1]
    distance = math.sqrt(dx**2 + dy**2)
    
    if distance == 0:
        return [0, 0]
    
    force_magnitude = G * body1.mass * body2.mass / distance**2
    force_x = force_magnitude * dx / distance
    force_y = force_magnitude * dy / distance
    
    return [force_x, force_y]

# Create three bodies
bodies = [
    Body([400, 300], [0, -2], 20, RED),
    Body([300, 300], [2, 0], 15, GREEN),
    Body([500, 300], [0, 2], 10, BLUE)
]

# Setup the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Three-Body Problem Simulation")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear screen
    screen.fill(WHITE)
    
    # Compute the forces on each body
    forces = [[0, 0] for _ in bodies]
    for i in range(len(bodies)):
        for j in range(len(bodies)):
            if i != j:
                force = calculate_gravitational_force(bodies[i], bodies[j])
                forces[i][0] += force[0] / bodies[i].mass
                forces[i][1] += force[1] / bodies[i].mass
    
    # Update velocities based on the computed forces
    for i in range(len(bodies)):
        bodies[i].vel[0] += forces[i][0]
        bodies[i].vel[1] += forces[i][1]
    
    # Update positions
    for body in bodies:
        body.update_position()
    
    # Draw the bodies
    for body in bodies:
        body.draw(screen)
    
    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit PyGame
pygame.quit()
sys.exit()
