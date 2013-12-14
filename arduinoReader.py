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

# Set name of Arduino port.
portName = "COM3"

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
# import os
import serial
import time
import matplotlib.pyplot as plt

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
# if not os.path.exists(outputPath):
#     os.makedirs(outputPath)

###################################################################################################


###################################################################################################
# Finalize timer and print elapsed time.
###################################################################################################

# Open serial buffer connected to Arduino board.
ser = serial.Serial(port = portName, baudrate=9600)

# Create empty array to store data.
readings = []

# Take readings and store in array.
for i in xrange(0,10):
	readings.append(ser.readline())

print readings

# Close serial buffer.
ser.close()

# Plot readings.
plt.plot(range(0,10),readings)

# Finalize timer.
endTime = time.time()

# Print elapsed time for script [s].
print "This script took " + str(endTime - startTime) + "s"

###################################################################################################