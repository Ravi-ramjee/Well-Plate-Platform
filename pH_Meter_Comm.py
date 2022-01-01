# -*- coding: utf-8 -*-

# Hwang Lab, University of Pennsylvania School of Dental Medicine
# Author: Ravikiran Ramjee, University of Pennsylvania SEAS

import serial
import time
from threading import Thread


def setextractioninterval(x):
    # Extraction Interval. A value will be extracted in an array for analysis at the interval specified below:
    global extractioninterval
    extractioninterval = x


def dataextraction():
    # Serial port that the pH meter is connected to. Will likely be COM3/COM4
    # To find this port, connect the device and go to device manager
    port = "COM4"

    # Baudrate: 1200 for MT SevenCompact pH meter
    ser = serial.Serial(port, baudrate=1200, bytesize=8)

    # Numpy array of data extracted at the specified interval
    phdata = []

    while True:
        try:
            data = ser.readline()
            # Formatted data for the specific meter by truncating for the sole pH value
            # This format will change for different meters
            phvalue = data[0:4].decode('UTF-8')
            if phvalue != '':
                phdata.append(float(phvalue))
            print(phdata)
            time.sleep(extractioninterval)
            if extractionbreak == 1:
                break
        except ValueError:
            print("Device is off or not connected!")


def startdataextraction():
    # Assign global variable and initialize value
    global extractionbreak
    extractionbreak = 0

    # Create and launch a thread
    t1 = Thread(target=dataextraction)
    t1.start()


def stopdataextraction():
    global extractionbreak
    extractionbreak = 1


#######################################################################################################################
# Test Functions Below, Ignore
def testprintdata():
    while True:
        print([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
        time.sleep(2)
        if stop == 1:
            break  # Break while loop when stop = 1


def startprintdata():
    # Assign global variable and initialize value
    global stop
    stop = 0

    # Create and launch a thread
    t = Thread(target=testprintdata)
    t.start()


def stopprintdata():
    # Assign global variable and set value to stop
    global stop
    stop = 1
