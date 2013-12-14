__author__ = 'kartikkumar'

'''
Copyright (c) 2013, GoUrbanGrow.
All rights reserved.
See ... for license details.

This script can be used to read out sensor data from an Arduino board.
'''

###################################################################################################
# Set up input deck
###################################################################################################

# Set up output path.
outputPath = "/Users/kartikkumar/Desktop"

###################################################################################################


'''

                            DO NOT EDIT PARAMETERS BEYOND THIS POINT!!!

'''


###################################################################################################
# Import Python packages and modules
###################################################################################################

# Import necessary external packages.
import os
import serial
import time

import calibrateMoistureSensor

###################################################################################################


###################################################################################################
# Start timer
###################################################################################################

startTime = time.time()

###################################################################################################


###################################################################################################
# Check output directory
###################################################################################################

# Check if output directory exists; if not, create it.
if not os.path.exists(outputPath):
    os.makedirs(outputPath)

###################################################################################################


###################################################################################################
# Finalize timer and print elapsed time.
###################################################################################################

ser = serial.Serial(port = '/dev/tty.usbmodem1421', baudrate=9600)

print calibrateMoistureSensor.calibrateMoistureSensor(ser)
# val = ser.readline()
# print(val)

#
ser.close()

# Finalize timer.
endTime = time.time()

# Print elapsed time for script [s].
print "This script took " + str(endTime - startTime) + "s"

###################################################################################################