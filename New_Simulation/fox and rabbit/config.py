# screen_config.py
import pygame
import sys

name = "Rabbit and Fox Simulation"

#screen
# WIDTH = 1500
# HEIGHT = 900
WIDTH = 500
HEIGHT = 500
BACKGROUND = (0, 0, 0)
FPS = 30
show_frame = True
Graph = True

#common
reproduce_every = 200
UPDATE_DIRECTION_AFTER = 50
bounce = True

#dots
num_dots = 1
radius = 10
dot_color = [255, 255, 255]
dot_speed = .4
max_dot_age = 600
DOT_REPRODUCE = True
show_dot = True
hit_sound = False

#boxs
num_boxes = 1
width = 20
box_color = (255, 0, 0)
box_speed = .5
max_box_age = 600 
hunger_threshold = 150
show_box = True
chasing = True