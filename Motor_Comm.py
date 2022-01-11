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
    print("Starting Motor Connection...")
    print(stage.query("CUR=700"))

def stopstage():
    print("Stopping Motor Connection...")
    stage.close()
    
def setspeed(x):
    global speed
    speed = x

def movement():

    stage.query("HSPD={}".format(abs(speed)))
    if speed < 0:
        print(stage.query("J-"))
    else:
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
    
