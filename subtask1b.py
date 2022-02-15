
""" Code for completion of subtask1b """

from pybricks.tools import wait

def task_1b(ev3, robot, gyro_sensor, laps, distance):

    final_position = 0

    forward = True

    for i in range(1, 1 + (2 * laps)):

        if forward:
            final_position = final_position + (distance)
            forward = False
        else:
            final_position = final_position - (distance)
            forward = True

    ev3.screen.print('{0} cm'.format(final_position))
    #
    # wait(100)
    #
    # gyro_sensor.angle()
    # gyro_sensor.speed()
    
    while gyro_sensor.angle() != 0:
        gyro_sensor.reset_angle(0)

    for i in range(1, 1 + (2 * laps)):
        gyro_sensor.reset_angle(0)

        robot.straight(distance * 10)
        # robot.turn(180)
        while gyro_sensor.angle() < 180:
            robot.drive(0, 80)
            print(gyro_sensor.angle())
        