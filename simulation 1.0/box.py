# box.py

import random
import math
import pygame
from screen_config import *

class Box:
    def __init__(self, width, color, speed, cooldown_frames=60):
        self.width = width
        self.color = color
        self.speed = speed
        self.position = [random.randint(0, WIDTH), random.randint(0, HEIGHT)]
        self.direction = random.uniform(0, 2 * math.pi)
        self.hunger = 0  # Initialize hunger attribute
        self.age = 0  # Initialize age attribute
        self.reproduction_count = 0  # Initialize reproduction count
        self.fov_radius = 50  # Field of view radius
        self.cooldown_frames = cooldown_frames  # Cooldown period for random movement

    def move(self, change_interval, dots):
        if self.cooldown_frames > 0:
            # Move randomly during the cooldown period
            if random.randint(0, change_interval) == 0:
                self.direction += random.uniform(-0.2, 0.2)
            self.cooldown_frames -= 1
        else:
            # Start hunting behavior after the cooldown period
            if dots:
                closest_dot = min(dots, key=lambda d: self.distance_to(d))
                self.chase_dot(closest_dot)
            else:
                # If no dots, move randomly
                if random.randint(0, change_interval) == 0:
                    self.direction += random.uniform(-0.2, 0.2)

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
        # pygame.draw.rect(screen, self.color, (int(self.position[0]), int(self.position[1]), self.width, self.width))
        
        # angle = math.atan2(self.velocity[1], self.velocity[0])
        angle = self.direction
        
        # Length of each side of the triangle
        size = self.width
        
        # Calculate the vertices of the triangle
        tip = (
            self.position[0] + math.cos(angle) * size,
            self.position[1] + math.sin(angle) * size
        )
        left = (
            self.position[0] + math.cos(angle + 5 * math.pi / 6) * size,
            self.position[1] + math.sin(angle + 5 * math.pi / 6) * size
        )
        right = (
            self.position[0] + math.cos(angle - 2.5 * math.pi / 3) * size,
            self.position[1] + math.sin(angle - 2.5 * math.pi / 3) * size
        )
        
        # Draw the triangle
        pygame.draw.polygon(screen, self.color, [tip, left, right])


        # Draw field of view as a circle around the box
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position[0] + self.width / 2), int(self.position[1] + self.width / 2)), 100, 1)

    def age_and_check(self, max_age):
        self.age += 1
        return self.age > max_age  # Returns True if age exceeds max_age

    def reproduce(self, boxes, max_reproductions):
        if self.reproduction_count < max_reproductions:
            # Create a new box at the same position with random initial properties
            new_box = Box(width=self.width, color=self.color, speed=self.speed)
            new_box.position = self.position[:]
            boxes.append(new_box)
            self.reproduction_count += 1

    def reset_hunger(self):
        self.hunger = 0

    def update_hunger_and_check(self, hunger_threshold):
        self.hunger += 1
        return self.hunger > hunger_threshold  # Returns True if hunger exceeds threshold

    def chase_dot(self, dot):
        # Calculate the angle towards the dot
        angle_to_dot = math.atan2(dot.position[1] - self.position[1], dot.position[0] - self.position[0])
        self.direction = angle_to_dot  # Directly set direction to the angle of the dot

    def distance_to(self, dot):
        return math.sqrt((self.position[0] - dot.position[0]) ** 2 + (self.position[1] - dot.position[1]) ** 2)
