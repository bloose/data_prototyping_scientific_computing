# Script for the Raspberry Pi Camera Trap.

from picamera import PiCamera  # for camera



# Code for capturing image
# Create an instance of the PiCamera() object for later calling.

# Consider letting the user know the camera has been enabled with a print statement.

# Initiate the GPIO boards for interacting with the PIR sensor.
#GPIO.setwarnings(False)

# To avoid confustion, use the same numeration as the GPIO board Pinouts.  After # this command is initated, Pin 3 will correspond to GPIO 3

# Set up a GPIO pin for Input from the PIR motion sensor.


# Create your conditional code to notice a state change in the PIR motion
# sensor, which triggers an image to be recorded with a timestamp.  Don't forget
# to add some time lag so the sensor doesn't capture 1000 images every time.

