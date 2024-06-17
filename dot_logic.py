# dot_logic.py

def move_dots(dots, change_interval):
    for dot in dots:
        dot.move(change_interval)

def draw_dots(screen, dots):
    for dot in dots:
        dot.draw(screen)
