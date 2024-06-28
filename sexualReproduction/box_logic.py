# box_logic.py

def move_boxes(boxes, dots, split_sound, kill_sound):
    for box in boxes:
        #box.chase_dot(dots)  # Boxes chase dots in their FOV
        box.move(30, dots, boxes, split_sound, kill_sound)
        print()

def draw_boxes(screen, boxes):
    for box in boxes:
        box.draw(screen)

def kill(boxes, kill_sound):
    for box in boxes:
        if(not box.alive):
            boxes.remove(box)
            kill_sound.play()

