# Biofilm-Platform-Communication-Protocol-HwangLab
Python software to communicate with a peristaltic pump and pH meter to help investigate dynamic biofilm formation via a simple Windows GUI (Hwang Lab: Center for Innovation &amp; Precision Dentistry, School of Dental Medicine, School of Engineering and Applied Sciences, University of Pennsylvania)

NOTE: The Python code provided in this repository was made for a specific pump and pH meter, the ARCUS NEMA-17 Stepper Motor DMX-J-SA-123 (https://www.arcus-technology.com/products/integrated-stepper-motors/nema-17-integrated-usb-stepper-basic/) and the Mettler Toledo SevenCompact pH Meter (https://www.mt.com/us/en/home/products/Laboratory_Analytics_Browse/pH-meter/benchtop-pH-meter/sevencompact/S220-Meter.html) respectively. Constructing the platform with different equipment will involve significant modifications to the programs provided. 

Required Packages: Tkinter, Pyserial, Datetime, Threading, Xlsxwriter, Pylablib

Instructions: 
1. From the ARCUS website, install necessary drivers for the motor found in the software section of the product page (https://www.arcus-technology.com/products/integrated-stepper-motors/nema-17-integrated-usb-stepper-basic/). The DLLs included in this repository need these drvers to work 
2. For the Mettler Toledo pH meter, change the storage destination from local memory (default) to printer and use the RS232 port on the back of the meter to connect the meter to the computer 
3. Similarly, connect the motor to power and the computer using a USB cable as outlined in the manual 
4. Using device manager, identify which serial port the pH meter is plugged into, usually "COM3" or "COM4" 
5. Download packages and repository files (Releases). Replace the port in pH_Meter_Comm.py with the one found in step 3. Refer to comments in the code itself
6. Run Operable_GUI.py 
7. Enter a measurment interval for the pH meter and speed for the motor before starting the data extraction and motor movement 
8. "Stop Extraction" button on the GUI will save the data to a spreadsheet for analysis 
9. Manufacturer constraints prevent the speed of the motor from being changed while it is moving. So, to change the speed, set the new speed and restart motor movement. The new speed will then take effect. 

Contact: 
Geelsu Hwang (Corresponding Author): geelsuh@upenn.edu
Ravikiran Ramjee: rramjee@seas.upenn.edu
