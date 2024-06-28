# box.py

import random
import math
import pygame
import sys
from config import *

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
        self.fov_radius = 100  # Field of view radius
        self.cooldown_frames = cooldown_frames  # Cooldown period for random movement
        self.alive = True

    def move(self, change_interval, dots, boxes, split_sound, kill_sound):
        if self.cooldown_frames > 0:
            # Move randomly during the cooldown period
            if random.randint(0, change_interval) == 0:
                self.direction += random.uniform(-0.2, 0.2)
            self.cooldown_frames -= 1
        else:
            # Start hunting behavior after the cooldown period
            if chasing and dots:
                closest_dot = min(dots, key=lambda d: self.distance_to(d))
                if(self.distance_to(closest_dot)<self.fov_radius+500):
                    self.chase_dot(closest_dot)
            else:
                # If no dots, move randomly
                if random.randint(0, change_interval) == 0:
                    self.direction += random.uniform(-0.2, 0.2)

        self.position[0] += self.speed * math.cos(self.direction)
        self.position[1] += self.speed * math.sin(self.direction)
        self.bounce_on_edges()
        self.eat(dots, kill_sound)
        self.age_and_check(boxes, split_sound)
        self.update_hunger_and_check()

    def bounce_on_edges(self):
        # Bounce off the edges of the screen
        if self.position[0] < 0 or self.position[0] > WIDTH:
            self.direction = math.pi - self.direction
           
        if self.position[1] < 0 or self.position[1] > HEIGHT:
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
        if(chasing):
            pygame.draw.circle(screen, (255, 255, 255), (int(self.position[0] + self.width / 2), int(self.position[1] + self.width / 2)), 100, 1)

    def age_and_check(self, boxes, split_sound):
        self.age += 1
        if(self.age % reproduce_every == 0):
            self.reproduce(boxes, split_sound)
        if(self.age > max_box_age):
            self.alive = False  # Returns True if age exceeds max_age

    def reproduce(self, boxes, split_sound):
        
        # Create a new box at the same position with random initial properties
        new_box = Box(width=self.width, color=self.color, speed=self.speed)
        new_box.position = self.position[:]
        boxes.append(new_box)
        self.reproduction_count += 1
        split_sound.play()

    def reset_hunger(self):
        self.hunger = 0

    def update_hunger_and_check(self):
        self.hunger += 1
        if(self.hunger > hunger_threshold):
            self.alive = False  # Returns True if hunger exceeds threshold

    def chase_dot(self, dot):
        # Calculate the angle towards the dot
        angle_to_dot = math.atan2(dot.position[1] - self.position[1], dot.position[0] - self.position[0])
        self.direction = angle_to_dot  # Directly set direction to the angle of the dot

    def distance_to(self, dot):
        return math.sqrt((self.position[0] - dot.position[0]) ** 2 + (self.position[1] - dot.position[1]) ** 2)

    def eat(self, dots, kill_sound):
        for dot in dots:
            if(self.distance_to(dot) < width + radius):
                dots.remove(dot)
                self.reset_hunger()
                kill_sound.play()
                break