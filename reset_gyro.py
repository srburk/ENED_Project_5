
from pybricks.tools import wait

def calibrate_gyro(gyro_sensor):
    wait(1000)
    
    gyro_sensor.speed()
    gyro_sensor.angle()
    
    gyro_sensor.reset_angle(0)
    
    wait(1000)