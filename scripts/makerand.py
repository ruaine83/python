# /usr/bin/python
# Written by T. Cook 12/15/2021
# Free for private and educational use

# ------------------------------------------------------------

# This script creates a file with a user defined name of
# an array of random numbers
# ranging from the input upper and lower bounds
# of user defined X and Y lengths  

# Could be edited to take command or call inputs as arguments

# ------------------------------------------------------------

# Enable random number generator
import random

# -----------------------------------------------------------

# Clear screen before starting 
# FOR WINDOWS, CHANGE 'clear' TO 'cls'

# Using name, it is possible to write a function to
# check the platform the script is running on
# and use the appropriate system call to clear screen.
from os import system, name
_ = system('clear')

# -----------------------------------------------------------

# Print user directions
print "Enter the Filename, x, y, lower and upper bounds at the prompts."

# Get inputs from user
filename = raw_input("Filename: ")
x = raw_input("X: ")
y = raw_input("Y: ")
lower = raw_input("Lower Bound: ")
upper = raw_input("Upper Bound: ")

# -----------------------------------------------------------

# Open designated file as read/write,
# overwriting file if it exisits
workfile = open(filename, "w+")

# -----------------------------------------------------------

# Not 100% necessary, but this ensures that the file is
# written to from the beginning
workfile.seek(0)

# -----------------------------------------------------------

# Build output file
for i in range (0,int(y)):							# Staring at the top and incrementing line by line:
	for j in range (0,int(x)):						# At the beginning of each line and working right:
		workfile.write("%i " % random.randint(int(lower), int(upper)))	# Create as many random integers as desired
	workfile.write("\n")							# and move to the next line

# -----------------------------------------------------------

# File creation done, so close the file
workfile.close()

# -----------------------------------------------------------

# Inform user of success
print "%s has been written successfully" % (filename)

# -----------------------------------------------------------

#END
