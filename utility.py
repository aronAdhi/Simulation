# utility.py

def run_simulation_step(screen, dots, boxes, dot_logic, box_logic, max_dot_age, hunger_threshold):
    """Run a single step of the simulation, moving and drawing all elements."""
    # Move and draw all dots
    dot_logic.move_dots(dots, change_interval=30)
    dot_logic.draw_dots(screen, dots)

    # Move and draw all boxes
    box_logic.move_boxes(boxes, dots)
    box_logic.draw_boxes(screen, boxes)

    # Collect dots and boxes to be removed
    dots_to_remove = []
    boxes_to_remove = []

    # Check age of each dot
    for dot in dots:
        if dot.age_and_check(max_dot_age):
            dots_to_remove.append(dot)

    # Check hunger and collisions for each box
    for box in boxes:
        hungry = box.update_hunger_and_check(hunger_threshold)
        if hungry:
            boxes_to_remove.append(box)
        for dot in dots:
            if dot.collide_with_box(box):
                dots_to_remove.append(dot)
                box.reset_hunger()  # Reset hunger when a box eats a dot
                break  # Stop checking this dot, it's been eaten

    # Remove the dots marked for removal
    for dot in dots_to_remove:
        if dot in dots:
            dots.remove(dot)

    # Remove the boxes marked for removal
    for box in boxes_to_remove:
        if box in boxes:
            boxes.remove(box)