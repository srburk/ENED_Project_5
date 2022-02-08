from pybricks.ev3devices import (Motor, GyroSensor)

class GyroBase:
    
    right_motor = None
    left_motor = None
    
    def __init__(self, left_motor, right_motor):
        right_motor = self.right_motor
        left_motor = self.left_motor
        
    def drive(distance):
        right_motor.run()
        left_motor.run()