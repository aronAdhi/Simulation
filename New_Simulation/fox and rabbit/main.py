# main.py

import pygame
import matplotlib.pyplot as plt
import numpy as np
from config import *
from dot import Dot
from box import Box
import manager
import dot_logic
import box_logic
import graph
import sys


# Boilerplate Pygame setup with custom size
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(name)
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 24)
frame = 0

# Creating elements
dots = [Dot(radius, dot_color, dot_speed, max_dot_age) for _ in range(num_dots)]
boxes = [Box(width, color=box_color, speed=box_speed) for _ in range(num_boxes)]
dots_count = []
boxes_count = []
bounce_sound = pygame.mixer.Sound('sound_effects//hit.wav')
kill_sound = pygame.mixer.Sound('sound_effects//kill.wav')
split_sound = pygame.mixer.Sound('sound_effects//split.wav')


running = True
while running:
    frame += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND)

    # Run the simulation step
    manager.run_simulation_step(screen, dots, boxes, dot_logic, box_logic, max_dot_age, max_box_age, hunger_threshold, 
    bounce_sound, kill_sound, split_sound)

    # Record the number of dots and boxes
    dots_count.append(len(dots))
    boxes_count.append(len(boxes))
    dots_text = font.render(f'Rabbits: {len(dots)}', True, (255, 255, 255))
    boxes_text = font.render(f'Foxes: {len(boxes)}', True, (255, 255, 255))
    frames_text = font.render(f'Frames: {frame}', True, (255, 255, 255))

    r_dots_text = pygame.transform.rotate(dots_text, 90)
    r_boxes_text = pygame.transform.rotate(boxes_text, 90)
    r_frames_text = pygame.transform.rotate(frames_text, 90)

    if(show_frame):
        screen.blit(r_frames_text, (10, 790))
    if(show_dot):
        screen.blit(r_dots_text, (50, 790))
    if(show_box):    
        screen.blit(r_boxes_text, (90, 790))

    pygame.display.flip()
    clock.tick(FPS)

if(Graph):
    graph.plot_graph(dots_count, boxes_count)
pygame.quit()
sys.exit()


