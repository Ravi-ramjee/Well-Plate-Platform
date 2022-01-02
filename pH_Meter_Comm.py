# -*- coding: utf-8 -*-

# Hwang Lab, University of Pennsylvania School of Dental Medicine
# Author: Ravikiran Ramjee, University of Pennsylvania Department of Bioengineering

import serial
from datetime import datetime
import time
from threading import Thread
import xlsxwriter


def setextractioninterval(x):
    # Extraction Interval. A value will be extracted in an array for analysis at the interval specified below:
    global extractioninterval
    extractioninterval = abs(x)


def dataextraction():
    # Data needs to be saved to an Excel file. So, the workbook is created
    workbook = xlsxwriter.Workbook("pH_Data_" + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ".xlsx")
    ws = workbook.add_worksheet()

    # Serial port that the pH meter is connected to. Will likely be in the form COMX for Windows
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
                ws.write(len(phdata) - 1, 0, datetime.now().strftime('%H:%M:%S.%f'))
                ws.write(len(phdata) - 1, 1, phvalue)
            print(phdata)
            time.sleep(extractioninterval)
            if extractionbreak == 1:
                workbook.close()
                break  # Break loop if stop condition is set to 1
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
    # Break the thread target loop
    global extractionbreak
    extractionbreak = 1


#######################################################################################################################
# Test Functions Below, Ignore
def testprintdata():
    workbook = xlsxwriter.Workbook("test" + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ".xlsx")
    ws = workbook.add_worksheet()
    data = []
    while True:
        data.append("hello")
        print("hello")
        ws.write(len(data) - 1, 0, datetime.now().strftime('%H:%M:%S.%f'))
        ws.write(len(data) - 1, 1, "hello")
        time.sleep(2)
        if stop == 1:
            workbook.close()
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
