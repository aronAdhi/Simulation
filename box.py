# box.py

import pygame
import random
import math
from screen_config import WIDTH, HEIGHT

class Box:
    def __init__(self, width, color, speed):
        self.width = width
        self.color = color
        self.speed = speed
        self.x = random.randint(width // 2, WIDTH - width // 2)
        self.y = random.randint(width // 2, HEIGHT - width // 2)
        self.direction = random.uniform(0, 2 * math.pi)
        self.fov_radius = 100  # Field of view radius

    def move(self):
        self.position[0] += self.speed * math.cos(self.direction)
        self.position[1] += self.speed * math.sin(self.direction)
        self.bounce_on_edges()

    def bounce_on_edges(self):
        if self.position[0] < 0 or self.position[0] > 800:
            self.direction = math.pi - self.direction
        if self.position[1] < 0 or self.position[1] > 600:
            self.direction = -self.direction

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.position[0], self.position[1], self.width, self.width))

    def update_hunger_and_check(self, hunger_threshold):
        self.hunger += 1
        return self.hunger > hunger_threshold  # Returns True if hunger exceeds threshold

    def reset_hunger(self):
        self.hunger = 0  # Resets hunger when a dot is eaten

    def detect_nearest_dot(self, dots):
        """Detect the nearest dot within the field of view."""
        min_distance = float('inf')
        nearest_dot = None

        for dot in dots:
            distance = math.sqrt((self.x - dot.x) ** 2 + (self.y - dot.y) ** 2)
            if distance <= self.fov_radius and distance < min_distance:
                min_distance = distance
                nearest_dot = dot

        return nearest_dot

    def update_direction(self):
        """Randomly change the direction by a small angle."""
        angle_change = random.uniform(-math.pi / 8, math.pi / 8)
        self.direction += angle_change