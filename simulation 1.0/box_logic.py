# box_logic.py

def move_boxes(boxes, dots):
    for box in boxes:
        #box.chase_dot(dots)  # Boxes chase dots in their FOV
        box.move(30, dots)

def draw_boxes(screen, boxes):
    for box in boxes:
        box.draw(screen)
