def run_simulation_step(screen, dots, boxes, dot_logic, box_logic, max_dot_age, max_box_age, hunger_threshold, bounce_sound, kill_sound, split_sound):
    
    dot_logic.move_dots(screen, dots, boxes, 30, bounce_sound, split_sound)

    dot_logic.draw_dots(screen, dots)

    dot_logic.kill(dots, kill_sound)



    box_logic.move_boxes(boxes, dots, split_sound, kill_sound)

    box_logic.draw_boxes(screen, boxes)

    box_logic.kill(boxes, kill_sound)

    

