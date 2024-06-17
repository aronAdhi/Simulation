# dot_logic.py
import random   


def move_dots(dots, change_interval):
    """Move all dots and change their direction periodically."""
    for dot in dots:
        if change_interval > 0 and random.randint(0, change_interval) == 0:
            dot.update_direction()
        dot.move(change_interval)

def draw_dots(screen, dots):
    """Draw all dots on the screen."""
    for dot in dots:
        dot.draw(screen)
