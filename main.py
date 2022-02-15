#!/usr/bin/env pybricks-micropython

""" This is the main robot code that handles the initialize and primary loop protocols """

from pybricks.ev3devices import Motor, GyroSensor
from pybricks.hubs import EV3Brick
from pybricks.parameters import Port, Button
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# custom imports
from subtask1a import task_1a
from subtask1b import task_1b
from reset_gyro import calibrate_gyro

# Constants
right_motor = Motor(Port.D)
left_motor = Motor(Port.A)
medium_motor = Motor(Port.C)
gyro_sensor = GyroSensor(Port.S2)
ev3 = EV3Brick()

robot = DriveBase(left_motor, right_motor, wheel_diameter=70, axle_track=95)

ev3.screen.clear()
ev3.screen.print('UP for Task A')
ev3.screen.print('DOWN for Task B')

buttons_pressed = ev3.buttons.pressed()

while not ((Button.UP in buttons_pressed)) and (not (Button.DOWN in buttons_pressed)) and (not (Button.CENTER in buttons_pressed)):
    wait(100)
    buttons_pressed = ev3.buttons.pressed()

ev3.screen.clear()

if Button.UP in buttons_pressed:
    task_1a(ev3, robot, 3, 120)
elif Button.DOWN in buttons_pressed:
    task_1b(ev3, robot, gyro_sensor, 4, 90)
else:
    calibrate_gyro(gyro_sensor)

robot.stop()
    