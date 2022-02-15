
""" Function to complete Subtask1A """

def task_1a(ev3, robot, laps, distance):
    
    forward = True
    
    final_position = 0
    
    for i in range(1, 1 + (2 * laps)):
        if forward:
            final_position = final_position + (distance)
            forward = False
        else:
            final_position = final_position + (-1 * distance)
            forward = True 

    ev3.screen.print('{0} cm'.format(final_position))

    for i in range(1, 1 + (2 * laps)):
        print(i)
        if forward:
            # robot.straight(distance * 10 * (i))
            robot.straight(distance * 10)
            forward = False
        else:
            # robot.straight(-1 * distance * 10 * (i))
            robot.straight(distance * 10 * -1)
            forward = True
    