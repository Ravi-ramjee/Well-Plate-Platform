# -*- coding: utf-8 -*-

# Hwang Lab, University of Pennsylvania School of Dental Medicine
# Author: Ravikiran Ramjee, University of Pennsylvania Department of Bioengineering

# Pylablib allows Python to use the manufacturer provided (Arcus Technology) DLLs to control the motor using an ASCII
# command format

# Imports
import time
import pylablib as pll
from pylablib.devices import Arcus
from threading import Thread

# Pylablib Arcus functionality used to establish connection with the pump
stage = Arcus.PerformaxDMXJSAStage()


# Ensures the running current of the motor is set to 700mA when the GUI is loaded. See usage in Operable_GUI.py
def startstage():
    print("Starting Motor Connection...")
    # stage.query(ASCII COMMAND) is the format used to write commands to the motor. print(stage.query(...))
    # prints the command output to the console. Output should be 'OK' for each successful command (see manual)
    print(stage.query("CUR=700"))


# Clears resources used to run the motor at the exit of the GUI. See usage in Operable_GUI.py
def stopstage():
    print("Stopping Motor Connection...")
    stage.close()


# Sets speed to a certain value as governed by a text entry in the GUI. Set speed before moving
def setspeed(x):
    global speed
    speed = x


# Main movement function
def movement():
    # Set the speed of the motor to the text entry value. NOTE: The motor speed cannot be changed while it is moving
    # due to manufacturing constraints
    stage.query("HSPD={}".format(abs(speed)))
    if speed < 0:
        # Negative speed inputs change the direction of the motor in the GUI
        print(stage.query("J-"))
    else:
        print(stage.query("J+"))

    while True:
        if movementbreak == 1:  # Break loop if stop condition is set to 1
            print(stage.query("STOP"))  # ASCII command to decelerate and stop motor (See manual)
            break


def startmovement():
    # Assign global variable and initialize value
    global movementbreak
    movementbreak = 0

    # Create and launch a thread
    t2 = Thread(target=movement)
    t2.start()


def stopmovement():
    # Break the thread target loop
    global movementbreak
    movementbreak = 1
