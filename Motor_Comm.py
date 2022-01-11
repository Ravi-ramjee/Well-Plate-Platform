# -*- coding: utf-8 -*-

# Hwang Lab, University of Pennsylvania School of Dental Medicine
# Author: Ravikiran Ramjee, University of Pennsylvania Department of Bioengineering

# Imports
import time
import pylablib as pll
from pylablib.devices import Arcus
from threading import Thread

stage = Arcus.PerformaxDMXJSAStage()

def startstage():
    print(Arcus.list_usb_performax_devices())

def stopstage():
    stage.close()
    
def setspeed(x):
    global speed
    speed = abs(x)

def movement():

    stage.query("HSPD={}".format(speed))
    print(stage.query("J+"))

    while True:
        if movementbreak == 1:
            print(stage.query("STOP"))
            break

def startmovement():
    global movementbreak
    movementbreak = 0
    t2 = Thread(target=movement)
    t2.start()

def stopmovement():
    global movementbreak
    movementbreak = 1
    
