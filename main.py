#!/usr/bin/env pybricks-micropython

""" This is the main robot code that handles the initialize and primary loop protocols """

from pybricks.ev3devices import GyroSensor, Motor

from pybricks.hubs import EV3Brick
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Custom imports

# Create your objects here.
ev3 = EV3Brick()

# Constants
right_motor = Motor(Port.D)
left_motor = Motor(Port.A)

gyro_sensor = GyroSensor(Port.S1)

# Initialize drive base
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

wait(10)
robot.straight(1000)
