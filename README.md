<p align="center">
  <h2 align="center">LEGO Mindstorms EV3 Color Sorter</h2>
  <p align="justify">
    
## Overview
  
This project consists of a color sorting system that uses the Mindstorms EV3 from LEGO and Legobrick with Python implementation in order to achieve its goal. The system detects the color of small built pieces, allowing the robot to separate them into bins based on their color.

The project aimed to use the software Bricklink in order to make easier the process and understanding, moreover, it was decided that Pybricks (a library in Python designed to manipulate the EV3) was choosen as the ideal tool.

The structure and final design underwent many changes throughout the process. The main difficulty was to fix the way the pieces were pushed into the classification system to be sorted. After some final discusions and corrections, the following design was achieved.

<img src="https://github.com/AldoPenaGa/LEGOColorSorter/blob/main/DesignIMG1.jpg" width='400'>
<img src="https://github.com/AldoPenaGa/LEGOColorSorter/blob/main/DesignIMG2.jpg"width='400'>
  </p>
</p>
<be>

## Table of contents
- [Key_Components](#Key_Components)
- [Installation_and_Setup](#Installation_and_Setup)
- [Code](#Code)
- [Usage](#Usage)
- [Results](#Results)
- [Contributors](#Contributors)


<div align= "justify">

### Key_Components

1. LEGO Mindstorms EV3 Kit:
- This kit includes essential components such as stepper motors, servomotors, and a color sensor.
- The EV3 brick is the central control unit that runs the robotic system.

2. Computer with Python Support:
-A computer capable of running a code editor that supports Python is needed.
-Visual Studio Code (VS Code) is a popular choice, but any Python-compatible editor will work.
-The Pybricks library will be essential for manipulating the EV3 using Python.

### Installation_and_Setup

The setup of the program is not challenging at all:
1. Open a Python-compatible code editor first. While Visual Studio Code (VS Code) is a widely used option, any editor that supports Python will function.
2. Write the intended code to be tested or uploaded.
3. Connect the LEGO Mindstorms EV3 brick to the PC using the provided connector. The code will be transferred via this connection.
4.  In the code editor, locate the EV3DEV DEVICE BROWSER section. This is where it will be performed the interaction with the EV3.
5. Here there will be two options available, to download it and store it in the EV3 or to just run it to test it, choose the most suitable.

### Code
Listed below is the code that was developed and tested:
```python
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
```
### Usage

Utilizing the color sorter is rather simple:
1. Switch the EV3 on.
2. Have the prototype ready by loading the parts that need to be sorted.
3. Using the EV3's navigation buttons, navigate to the path where the software was downloaded.
4. Select the Python application and watch for confirmation (a large checkmark appearing on the screen).

### Results

Click this link to see an example of how the color sorter functions: https://youtu.be/N7xULEUeYis

### Contributors

| Name                          | Github                               |
|-------------------------------|--------------------------------------|
| Aldo Oziel Peña Gamboa        | https://github.com/AldoPenaGa        |
| Charbel Breydy Torres         | https://github.com/Buly1601          |
| Joan Carlos Monfil Huitle     |     |
| Enrique Rocha Espinoza        | https://github.com/Enrique-Rocha-Espinoza|

