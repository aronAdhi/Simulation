# box.py

import pygame
import random
import math

class Box:
    def __init__(self, width, color, speed):
        self.width = width
        self.color = color
        self.speed = speed
        self.position = [random.randint(0, 800), random.randint(0, 600)]
        self.direction = random.uniform(0, 2 * math.pi)
        self.hunger = 0  # Initialize hunger attribute
        self.fov_radius = 100  # Field of view radius

    def move(self):
        # Move the box in its current direction
        self.position[0] += self.speed * math.cos(self.direction)
        self.position[1] += self.speed * math.sin(self.direction)
        self.bounce_on_edges()

    def bounce_on_edges(self):
        # Bounce off the edges of the screen
        if self.position[0] < 0 or self.position[0] > 800:
            self.direction = math.pi - self.direction
        if self.position[1] < 0 or self.position[1] > 600:
            self.direction = -self.direction

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.position[0], self.position[1], self.width, self.width))
        # Draw the field of view
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position[0]), int(self.position[1])), self.fov_radius, 1)

    def update_hunger_and_check(self, hunger_threshold):
        self.hunger += 1
        return self.hunger > hunger_threshold  # Returns True if hunger exceeds threshold

    def reset_hunger(self):
        self.hunger = 0  # Resets hunger when a dot is eaten

    def chase_dot(self, dots):
        nearest_dot = None
        min_distance = float('inf')

        for dot in dots:
            distance = math.sqrt((self.position[0] - dot.position[0]) ** 2 + (self.position[1] - dot.position[1]) ** 2)
            if distance < min_distance and distance < self.fov_radius:
                nearest_dot = dot
                min_distance = distance

        if nearest_dot:
            angle_to_dot = math.atan2(nearest_dot.position[1] - self.position[1], nearest_dot.position[0] - self.position[0])
            self.direction = angle_to_dot  # Chase towards the nearest dot
