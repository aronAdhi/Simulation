# dot.py

import random
import math
import pygame
from config import *

class Dot:
    def __init__(self, radius, color, speed, max_age, fov_radius=100 ):
        self.radius = radius
        self.color = color
        self.speed = speed
        self.position = [random.randint(0, WIDTH), random.randint(0, HEIGHT)]
        self.direction = random.uniform(0, 2 * math.pi)
        self.age = 0  # Initialize age attribute
        self.fov_radius = fov_radius  # Field of view radius
        self.max_age = max_age
        self.alive = True

    def move(self, dots, screen, change_interval, boxes, bounce_sound, split_sound):
        
        self.position[0] += self.speed * math.cos(self.direction)
        self.position[1] += self.speed * math.sin(self.direction)
        if(bounce):
            self.bounce_on_edges(bounce_sound)
        self.age_and_check(dots, split_sound)

    def bounce_on_edges(self, bounce_sound):
        # Bounce off the edges of the screen
        if self.position[0] < 0 or self.position[0] > WIDTH:
            self.direction = math.pi - self.direction
            if(hit_sound):
                bounce_sound.play()
        if self.position[1] < 0 or self.position[1] > HEIGHT:
            self.direction = -self.direction
            if(hit_sound):
                bounce_sound.play()

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.position[0]  , self.position[1] ), self.radius-self.radius/10)
        pygame.draw.polygon(screen, self.color, 
                            [[self.position[0] + self.radius * math.cos(self.direction) , self.position[1] + self.radius * math.sin(self.direction)], 
                             [self.position[0] + self.radius * math.cos(self.direction+2.5) , self.position[1] + self.radius * math.sin(self.direction+2.5)],
                             [self.position[0] + self.radius * math.cos(self.direction-2.5) , self.position[1] + self.radius * math.sin(self.direction-2.5)]])

    def distance_to(self, obj):
        return math.sqrt((self.position[0] - obj.position[0]) ** 2 + (self.position[1] - obj.position[1]) ** 2)

    def age_and_check(self, dots, split_sound):
        self.age += 1
        # if(self.age > 400):
        #     self.color = (255, 0, 0)

        if(DOT_REPRODUCE and self.age%reproduce_every == 0): 
            self.reproduce(dots, split_sound)

        if(self.age >self.max_age):
             self.alive=False    
        

    def reproduce(self, dots, split_sound):
        # Create a new dot at the same position with random initial properties
        new_dot = Dot(radius=self.radius, color=self.color, speed=self.speed, max_age=self.max_age, fov_radius=self.fov_radius)
        new_dot.position = self.position[:]
        dots.append(new_dot)
        split_sound.play()
        

    def collide_with_box(self, box):
        return (self.distance_to(box) <= self.radius+1)
  