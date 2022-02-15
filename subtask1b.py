
""" Code for completion of subtask1b """

def task_1b(ev3, robot, gyro_sensor, laps, distance):
    
    final_position = 0
    
    forward = True
    
    for i in range(1, 1 + (2 * laps)):
        
        if forward:
            final_position = final_position + (distance * (i))
            forward = False
        else:
            final_position = final_position - (distance * (i))
            forward = True
        
    ev3.screen.print('{0} cm'.format(final_position))
    
    gyro_sensor.reset_angle(0)     
    for i in range(1, 1 + (2 * laps)):      
        gyro_sensor.reset_angle(0)
        
        robot.straight(distance * 10 * (i))
        # robot.turn(180)
        while gyro_sensor.angle() < 180:
            robot.drive(0, 80)
            # print(gyro_sensor.angle())
        