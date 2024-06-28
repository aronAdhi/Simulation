import pygame

def draw_dots(screen, dots):
    for dot in dots:
        dot.draw(screen)

def move_dots(screen, dots, boxes, change_interval, bounce_sound, split_sound):
    for dot in dots:
        dot.move(dots, screen, change_interval, boxes, bounce_sound, split_sound)

def kill(dots, kill_sound):
    for dot in dots:
        if(not dot.alive):
            dots.remove(dot)
            kill_sound.play()