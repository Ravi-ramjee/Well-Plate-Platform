# -*- coding: utf-8 -*-

# Hwang Lab, University of Pennsylvania School of Dental Medicine
# Author: Ravikiran Ramjee, University of Pennsylvania SEAS

import pH_Meter_Comm as ph
from tkinter import *
from tkinter import ttk


def setintendedextractioninterval():
    if ExtractionEvent.get() != '':
        temp1 = int(ExtractionEvent.get())
    else:
        temp1 = 0
    ph.setextractioninterval(temp1)


def getintendedextractioninterval():
    if ExtractionEvent.get() != '':
        return str(0)
    else:
        return str(ExtractionEvent.get())


root = Tk(className="Operable GUI")
frm = ttk.Frame(root, padding=10)
frm.grid()
root.geometry("500x500")

QuitButton = ttk.Button(frm, text="Quit", command=root.destroy)

ExtractionLabel = ttk.Label(frm, text="Extraction Interval - pH Meter", borderwidth=1, relief="solid")
ExtractionEvent = ttk.Entry(frm)
SetExtractionButton = ttk.Button(frm, text="Set", command=setintendedextractioninterval)

BeginDataExtraction = ttk.Button(frm, text="Begin Extraction", command=ph.startdataextraction)
StopDataExtraction = ttk.Button(frm, text="Stop Extraction", command=ph.stopdataextraction)

ExtractionLabel.grid(row=0, column=0)
ExtractionEvent.grid(row=0, column=1)
SetExtractionButton.grid(row=0, column=3)
BeginDataExtraction.grid(row=2, column=0)
StopDataExtraction.grid(row=2, column=1)
QuitButton.grid(row=3, column=0)

if __name__ == '__main__':
    root.mainloop()
