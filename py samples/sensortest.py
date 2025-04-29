print(" Control + C to exit Program")

import time
import pinconfig

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)    # the pin numbers refer to the board connector not the chip
GPIO.setwarnings(False)
GPIO.setup(pinconfig.DOOR1_CLOSED_SENSOR, GPIO.IN, GPIO.PUD_DOWN)  # Door is Closed sensor
GPIO.setup(pinconfig.DOOR1_OPEN_SENSOR, GPIO.IN, GPIO.PUD_DOWN)    # Door is Open sensor
GPIO.setup(pinconfig.DOOR2_CLOSED_SENSOR, GPIO.IN, GPIO.PUD_DOWN)  # Door is Closed sensor
GPIO.setup(pinconfig.DOOR2_OPEN_SENSOR, GPIO.IN, GPIO.PUD_DOWN)    # Door is Open sensor
GPIO.setup(pinconfig.DOOR3_CLOSED_SENSOR, GPIO.IN, GPIO.PUD_DOWN)  # Door is Closed sensor
GPIO.setup(pinconfig.DOOR3_OPEN_SENSOR, GPIO.IN, GPIO.PUD_DOWN)    # Door is Open sensor

try:
  while 1 >=0:
    print('D1_Open = '+str(GPIO.input(pinconfig.DOOR1_OPEN_SENSOR)) + 
          '\tD1_Closed = '+str(GPIO.input(pinconfig.DOOR1_CLOSED_SENSOR)) + 
          '\tD2_Open = '+str(GPIO.input(pinconfig.DOOR2_OPEN_SENSOR)) + 
          '\tD2_Closed = '+str(GPIO.input(pinconfig.DOOR2_CLOSED_SENSOR)) + 
          '\tD3_Open = '+str(GPIO.input(pinconfig.DOOR3_OPEN_SENSOR)) + 
          '\tD3_Closed = '+str(GPIO.input(pinconfig.DOOR3_CLOSED_SENSOR)))
    time.sleep(0.1)             # pauses system for 1 second

except KeyboardInterrupt:     # Stops program when "Control + C" is entered
  GPIO.cleanup()               # Turns OFF all relay switches
