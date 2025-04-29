print(" Control + C to exit Program")

import time
import pinconfig

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)    # the pin numbers refer to the board connector not the chip
GPIO.setwarnings(False)
GPIO.setup(pinconfig.DOOR1_BUTTON, GPIO.OUT)     # sets the pin input/output setting to OUT
GPIO.output(pinconfig.DOOR1_BUTTON, GPIO.HIGH)   # sets the pin output to high
GPIO.setup(pinconfig.DOOR2_BUTTON, GPIO.OUT)
GPIO.output(pinconfig.DOOR2_BUTTON, GPIO.HIGH)
GPIO.setup(pinconfig.DOOR3_BUTTON, GPIO.OUT)
GPIO.output(pinconfig.DOOR3_BUTTON, GPIO.HIGH)

try:
  while 1 >=0:
    GPIO.output(pinconfig.DOOR1_BUTTON, GPIO.LOW)   # turns the first relay switch ON
    time.sleep(.5)             # pauses system for 1/2 second
    GPIO.output(pinconfig.DOOR1_BUTTON, GPIO.HIGH)  # turns the first relay switch OFF
    GPIO.output(pinconfig.DOOR2_BUTTON, GPIO.LOW)  # turns the second relay switch ON
    time.sleep(.5)
    GPIO.output(pinconfig.DOOR2_BUTTON, GPIO.HIGH)
    GPIO.output(pinconfig.DOOR3_BUTTON, GPIO.LOW)
    time.sleep(.5)
    GPIO.output(pinconfig.DOOR3_BUTTON, GPIO.HIGH)


except KeyboardInterrupt:     # Stops program when "Control + C" is entered
  GPIO.cleanup()               # Turns OFF all relay switches
