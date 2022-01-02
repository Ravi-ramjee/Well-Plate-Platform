# -*- coding: utf-8 -*-

# Hwang Lab, University of Pennsylvania School of Dental Medicine
# Author: Ravikiran Ramjee, University of Pennsylvania Department of Bioengineering

# Imports
import pH_Meter_Comm as ph
from tkinter import *
from tkinter import ttk


# pH Meter: Used to set the interval that the meter takes measurements using the GUI
# The default interval is one second if left blank
def setintendedextractioninterval():
    if ExtractionEvent.get() != '':
        temp1 = int(ExtractionEvent.get())
    else:
        temp1 = 1
    ph.setextractioninterval(temp1)


def getintendedextractioninterval():
    if ExtractionEvent.get() != '':
        return str(1)
    else:
        return str(ExtractionEvent.get())


# The tkinter GUI library commands to create the simple GUI below:

# Establishes the main window used for the interface
root = Tk(className=" Operable GUI")

# Frame that the main buttons are packed into. This helps put the quit button at the bottom
frm = ttk.Frame(root, relief=RAISED, borderwidth=1)
frm.pack(fill=BOTH, expand=True)

# root.geometry("500x500")

# Quit button with the command that exits the application
QuitButton = ttk.Button(root, text="Quit", command=root.destroy)
# Packs the quit button into the main root interface
QuitButton.pack()

# Grouped items that set the extraction interval for the pH meter
ExtractionLabel = ttk.Label(frm, text="Extraction Interval - pH Meter (seconds)", borderwidth=1, relief="solid")
ExtractionEvent = ttk.Entry(frm)
SetExtractionButton = ttk.Button(frm, text="Set Interval", command=setintendedextractioninterval)

# Items that start and stop the extraction of data from the meter
BeginDataExtraction = ttk.Button(frm, text="Begin Extraction", command=ph.startdataextraction)
StopDataExtraction = ttk.Button(frm, text="Stop Extraction", command=ph.stopdataextraction)

# Grouped items that set the speed of the peristaltic pump
MotorLabel = ttk.Label(frm, text="Speed - Peristaltic Pump", borderwidth=1, relief="solid")
SpeedEvent = ttk.Entry(frm)
SetSpeedButton = ttk.Button(frm, text="Set Speed")

# Items that start and stop the motor operation
BeginMotor = ttk.Button(frm, text="Begin Motor")
StopMotor = ttk.Button(frm, text="Stop Motor")

# Packs the pH and motor GUI items to the frame
ExtractionLabel.pack(side=TOP)
ExtractionEvent.pack(side=TOP)
SetExtractionButton.pack(side=TOP)

MotorLabel.pack(side=TOP)
SpeedEvent.pack(side=TOP)
SetSpeedButton.pack(side=TOP)

BeginDataExtraction.pack(side=LEFT)
BeginMotor.pack(side=LEFT)
StopDataExtraction.pack(side=RIGHT)
StopMotor.pack(side=RIGHT)

# Main root loop to start the GUI
if __name__ == '__main__':
    root.mainloop()
