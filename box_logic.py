# box_logic.py

import math

def move_boxes(boxes, dots):
    """Move all boxes and make them chase dots within their FOV."""
    for box in boxes:
        nearest_dot = box.detect_nearest_dot(dots)
        if nearest_dot:
            # Face towards the nearest dot
            box.face_towards(nearest_dot.x, nearest_dot.y)
        else:
            # Move randomly if no dot is in FOV
            box.update_direction()
        box.move()

def draw_boxes(screen, boxes):
    """Draw all boxes on the screen."""
    for box in boxes:
        box.draw(screen)
        box.draw_fov_circle(screen)
