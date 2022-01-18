# -*- coding: utf-8 -*-

# Hwang Lab, University of Pennsylvania School of Dental Medicine
# Author: Ravikiran Ramjee, University of Pennsylvania Department of Bioengineering

# Simple proof of concept program that has states for a four change flow distributor
# If such a flow distributor were to be used, the operation for the valves would be placed here

class FluidChannel:
    def __init__(self, openstatus, number):
        self.openstatus = openstatus
        self.number = number

    def getOpenStatus(self):
        return self.openstatus

    def setOpenStatus(self, newopenstatus):
        self.openstatus = newopenstatus

    # Functions to open and close valves based on the established "openstatus"
    def opencloseValve(self):
        if not self.openstatus:  # Case where the valve is closed
            print("Opening Valve {}...".format(self.number))
            # Valve movement to open the valve (code goes here)
            self.setOpenStatus(not self.openstatus)  # Set valve status to be open
        else:
            print("Closing Valve {}...".format(self.number))
            # Valve movement to close the valve (code goes here)
            self.setOpenStatus(not self.openstatus)  # Set valve status to be closed


# Instantiates four channels for the microfluidic valves
Channel1 = FluidChannel(False, 1)
Channel2 = FluidChannel(False, 2)
Channel3 = FluidChannel(False, 3)
Channel4 = FluidChannel(False, 4)
