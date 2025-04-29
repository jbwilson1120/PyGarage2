import RPi.GPIO as GPIO
import time
from config import (
	PORT,
	ENABLE_PASSWORD,
	PASSWORD,
	ENABLE_SIRI,
	SIRI_PASSWORD,
	BG_COLOR_QUESTION,
	BG_COLOR_OPEN,
	BG_COLOR_CLOSED,
	IMAGE_QUESTION,
	IMAGE_OPEN,
	IMAGE_CLOSED,
	NUMBER_OF_DOORS,
	DOOR_1_NAME,
	DOOR_2_NAME,
	DOOR_3_NAME,
	SENSORS_PER_DOOR,
	ADMIN,
	ADMIN_PASS,
)
class clsDoor(object):
    status = ""
    name = ""
    visible = "none"
    PinOpener = 0
    PinSensorOpen = 0
    PinSensorClosed = 0
    SensorCount = 2

    GPIO.setmode(GPIO.BOARD)  # the pin numbers refer to the board connector not the chip
    GPIO.setwarnings(False)

    from config import (
	    PORT,
	    ENABLE_PASSWORD,
	    PASSWORD,
	    ENABLE_SIRI,
	    SIRI_PASSWORD,
	    BG_COLOR_QUESTION,
	    BG_COLOR_OPEN,
	    BG_COLOR_CLOSED,
	    IMAGE_QUESTION,
	    IMAGE_OPEN,
	    IMAGE_CLOSED,
	    NUMBER_OF_DOORS,
	    DOOR_1_NAME,
	    DOOR_2_NAME,
	    DOOR_3_NAME,
	    SENSORS_PER_DOOR,
	    ADMIN,
	    ADMIN_PASS,
    )
    
    def __init__(self, name, visible, PinSensorOpen, PinSensorClosed, PinOpener, SensorCount):
        #global GPIO
        self.name = name
        self.status = "Unknown"
        self.PinSensorOpen = PinSensorOpen
        self.PinSensorClosed = PinSensorClosed
        self.PinOpener = PinOpener
        self.SensorCount = SensorCount
        if visible == True:
            self.visible = "inline-block"
        else:
            self.visible = "none"
        GPIO.setup(self.PinSensorClosed, GPIO.IN, GPIO.PUD_DOWN)  # Door is Closed sensor
        GPIO.setup(self.PinSensorOpen, GPIO.IN, GPIO.PUD_DOWN)    # Door is Open sensor
        GPIO.setup(self.PinOpener, GPIO.OUT)			        # Door Relay to Open/Close Door
        GPIO.output(self.PinOpener, GPIO.HIGH)

    def PushButton(self):
        GPIO.output(self.PinOpener, GPIO.LOW)
        time.sleep(1)
        GPIO.output(self.PinOpener, GPIO.HIGH)
        time.sleep(2)
        return ""


    def GetStatus(self):

        #print(self.name + " PinSensorOpen = " + str(GPIO.input(self.PinSensorOpen)))
        #print(self.name + " PinSensorClosed = " + str(GPIO.input(self.PinSensorClosed)))
        if GPIO.input(self.PinSensorClosed)==False:
            return "closed"
        elif GPIO.input(self.PinSensorOpen)==False:
            return "open"
        else:
            return "unknown"

    def GetImage(self):
        if self.GetStatus() == "open":
            return IMAGE_OPEN
        if self.GetStatus() == "closed":
            return IMAGE_CLOSED
        if self.GetStatus() == "unknown":
            return IMAGE_QUESTION

    def name(self):
        return self.name

    def visible(self):
        return self.visible

    def __str__(self):
        return f"{self.name}({self.status})"