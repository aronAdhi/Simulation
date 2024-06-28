# # dot.py
# import pygame
# import random
# import math


# class Dot:
#     def __init__(self, radius, color, speed):
#         self.radius = radius
#         self.color = color
#         self.speed = speed
#         self.position = [random.randint(0, 800), random.randint(0, 600)]
#         self.direction = random.uniform(0, 2 * math.pi)
#         self.age = 0  # Initialize age attribute
#         self.reproduction_count = 0  # Initialize reproduction count

#     def move(self, change_interval):
#         # Randomly change direction
#         if random.randint(0, change_interval) == 0:
#             self.direction += random.uniform(-0.2, 0.2)
#         self.position[0] += self.speed * math.cos(self.direction)
#         self.position[1] += self.speed * math.sin(self.direction)
#         self.bounce_on_edges()

#     def bounce_on_edges(self):
#         # Bounce off the edges of the screen
#         if self.position[0] < 0 or self.position[0] > 800:
#             self.direction = math.pi - self.direction
#         if self.position[1] < 0 or self.position[1] > 600:
#             self.direction = -self.direction

#     def draw(self, screen):
#         pygame.draw.circle(screen, self.color, (int(self.position[0]), int(self.position[1])), self.radius)

#     def age_and_check(self, max_age):
#         self.age += 1
#         return self.age > max_age  # Returns True if age exceeds max_age

#     def collide_with_box(self, box):
#         distance = math.sqrt((self.position[0] - box.position[0]) ** 2 + (self.position[1] - box.position[1]) ** 2)
#         return distance < self.radius + box.width / 2

#     def reproduce(self, dots, max_reproductions):
#         if self.reproduction_count < max_reproductions:
#             # Create a new dot at the same position with random initial properties
#             new_dot = Dot(radius=self.radius, color=self.color, speed=self.speed)
#             new_dot.position = self.position[:]
#             dots.append(new_dot)
#             self.reproduction_count += 1


# dot.py

import random
import math
import pygame
from screen_config import *

class Dot:
    def __init__(self, radius, color, speed, fov_radius=100, max_age=300):
        self.radius = radius
        self.color = color
        self.speed = speed
        self.position = [random.randint(0, WIDTH), random.randint(0, HEIGHT)]
        self.direction = random.uniform(0, 2 * math.pi)
        self.age = 0  # Initialize age attribute
        self.reproduction_count = 0  # Initialize reproduction count
        self.fov_radius = fov_radius  # Field of view radius

    def move(self, change_interval, boxes):
        # Determine if any box is within the FOV
        box_in_fov = None
        for box in boxes:
            if self.distance_to(box) <= self.fov_radius:
                box_in_fov = box
                break
        
        if box_in_fov:
            # Move away from the box
            angle_away_from_box = math.atan2(self.position[1] - box_in_fov.position[1], self.position[0] - box_in_fov.position[0])
            # self.direction = angle_away_from_box
        else:
            # Move randomly if no box is nearby
            if random.randint(0, change_interval) == 0:
                self.direction += random.uniform(-0.2, 0.2)

        self.position[0] += self.speed * math.cos(self.direction)
        self.position[1] += self.speed * math.sin(self.direction)
        self.bounce_on_edges()

    def bounce_on_edges(self):
        # Bounce off the edges of the screen
        if self.position[0] < 0 or self.position[0] > WIDTH:
            self.direction = math.pi - self.direction
        if self.position[1] < 0 or self.position[1] > HEIGHT:
            self.direction = -self.direction

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.position[0]), int(self.position[1])), self.radius)
        
    def distance_to(self, obj):
        return math.sqrt((self.position[0] - obj.position[0]) ** 2 + (self.position[1] - obj.position[1]) ** 2)

    def age_and_check(self, max_age):
        self.age += 1
        return self.age > max_age  # Returns True if age exceeds max_age

    def reproduce(self, dots, max_reproductions):
        if self.reproduction_count < max_reproductions:
            # Create a new dot at the same position with random initial properties
            new_dot = Dot(radius=self.radius, color=self.color, speed=self.speed, fov_radius=self.fov_radius)
            new_dot.position = self.position[:]
            dots.append(new_dot)
            self.reproduction_count += 1

    def collide_with_box(self, box):
        # Check if the dot's position is within the box's bounds
        # box_x, box_y, box_width = box.position[0], box.position[1], box.width
        # dot_x, dot_y = self.position[0], self.position[1]
        # return (box_x <= dot_x <= box_x + box_width) and (box_y <= dot_y <= box_y + box_width)
        return (self.distance_to(box) <= self.radius+1)
