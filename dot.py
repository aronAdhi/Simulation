# dot.py

import pygame
import random
import math
from screen_config import WIDTH, HEIGHT

class Dot:
    def __init__(self, radius, color, speed):
        self.radius = radius
        self.color = color
        self.speed = speed
        self.x = random.randint(radius, WIDTH - radius)
        self.y = random.randint(radius, HEIGHT - radius)
        self.direction = random.uniform(0, 2 * math.pi)

    def move(self, change_interval):
        self.x += self.speed * math.cos(self.direction)
        self.y += self.speed * math.sin(self.direction)
        
        if self.x - self.radius < 0 or self.x + self.radius > WIDTH:
            self.direction = math.pi - self.direction
        if self.y - self.radius < 0 or self.y + self.radius > HEIGHT:
            self.direction = -self.direction


    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
    
    def age_and_check(self, max_age):
        self.age += 1
        return self.age > max_age  # Returns True if age exceeds max_age

    def collide_with_box(self, box):
        distance = math.sqrt((self.x - box.x) ** 2 + (self.y - box.y) ** 2)
        return distance < self.radius + box.width / 2
