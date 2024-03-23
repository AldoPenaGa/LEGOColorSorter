#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time

# Create your objects here.
ev3 = EV3Brick()
#DECLARE THE COLOR AND TOUCH SENSORS
color_sen = ColorSensor(port = Port.S1)
#DECLARE BOTH MOTORS FOR THE PUSH BLOCK AND FOR THE CONVEYOR BELT MOVEMENT
rot = Motor(port = Port.A, positive_direction=Direction.CLOCKWISE,gears=None)
push =  Motor(port = Port.B,positive_direction=Direction.CLOCKWISE,gears=None)

# color to pos dict
color_map = {
    Color.BLUE: -30,
    Color.RED: 10,
    Color.GREEN: -10,
    Color.YELLOW: 30,
    Color.BROWN: 30
}   


def main():
    # do this 6 times, once per piece
    for _ in range(6):
        if Button.CENTER in ev3.buttons.pressed():
            break

        if color_sen.color() != Color.BLACK:
            time.sleep(0.1)
            # get color to rotate 
            rotation = color_map[color_sen.color()]
            # rotate to target
            rot.run_target(100, rotation, then=Stop.HOLD, wait=True)
            # push the piece 
            push.run_target(100, 90, then=Stop.HOLD, wait=True)
            push.run_target(200, 0, then=Stop.HOLD, wait=True)
            # return to 0 position
            rot.run_target(50, -rotation-10, then=Stop.HOLD, wait=True)
            # wait for all engines to stop
            time.sleep(0.1)


main()