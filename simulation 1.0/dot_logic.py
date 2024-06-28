# dot_logic.py

def draw_dots(screen, dots):
    for dot in dots:
        dot.draw(screen)

# dot_logic.py

def move_dots(dots, boxes, change_interval):
    for dot in dots:
        dot.move(change_interval, boxes)
