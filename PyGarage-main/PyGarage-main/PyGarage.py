import os
import time
from datetime import datetime
from flask import Flask, render_template, request
import socket
from clsDoor import clsDoor
import RPi.GPIO as GPIO

hostname = socket.gethostname()
ip_address = socket.gethostbyname(socket.gethostname() + ".local")

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
	APIKEY,
	ADMIN,
	ADMIN_PASS,
)
import pinconfig

directory = os.getcwd()
APP_PATH = os.path.abspath(__file__)
LOG_FILE = directory + '/log.py'

global No_Refresh
No_Refresh = int(datetime.now().strftime("%d%m"))
Refresher = int(datetime.now().strftime("%d%m"))
BadPassword = 0

Any_Door_Open = 0			#Default Status, If any door is Not Closed, this will be greater than 0
bgcolor = BG_COLOR_QUESTION		#Default Status, Door is questionable, so background yellow

# Setup the doors
door1 = clsDoor(DOOR_1_NAME, True, pinconfig.DOOR1_OPEN_SENSOR, pinconfig.DOOR1_CLOSED_SENSOR, pinconfig.DOOR1_BUTTON, SENSORS_PER_DOOR)
door2 = clsDoor(DOOR_2_NAME, (NUMBER_OF_DOORS >= 2), pinconfig.DOOR2_OPEN_SENSOR, pinconfig.DOOR2_CLOSED_SENSOR, pinconfig.DOOR2_BUTTON, SENSORS_PER_DOOR)
door3 = clsDoor(DOOR_3_NAME, (NUMBER_OF_DOORS == 3), pinconfig.DOOR3_OPEN_SENSOR, pinconfig.DOOR3_CLOSED_SENSOR, pinconfig.DOOR3_BUTTON, SENSORS_PER_DOOR)
imagesize = 50

app = Flask(__name__)

print('-------------------------------------------')
print('\n Hostname of your Pi: ' + hostname)
print(' IP address of Pi: ' + ip_address)
print('')
print(' Garage Door Status Found at: http://' + ip_address + ':' + str(PORT))
print(' Settings Can Be Found at: http://' + ip_address + ':' + str(PORT) + '/Settings')
print(' Siri Setup Instructions Can Be Found at: http://' + ip_address + ':' + str(PORT) + '/page/sirisetup.html')
print('')
print('-------------------------------------------')



@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		global BadPassword
		global No_Refresh
		global door1
		global door2
		global door3
		code = request.form['garagecode']
		Door_To_Open = request.form.get('garagedoorradio', "UNKNOWN")
		Password_Counter = int(request.form.get('No_Refresh', "0"))

		PASSWORD_LIST = PASSWORD.split()

		if ENABLE_PASSWORD == "YES":
			if code in PASSWORD_LIST and Password_Counter == No_Refresh and BadPassword <= 5:  # 12345678 is the Default Password that Opens Garage Door (Code if Password is Correct)
				print("Door requested to open: " + Door_To_Open)
				No_Refresh = No_Refresh + 1;
				logfile = open("static/log.txt","a")
				logfile.write("     " + datetime.now().strftime(request.environ['REMOTE_ADDR'] + "     Door opened/closed: " + Door_To_Open + " -- %Y/%m/%d -- %H:%M  \n"))
				logfile.close()
				if Door_To_Open == "door1":
					door1.PushButton()
				if Door_To_Open == "door2":
					door2.PushButton()
				if Door_To_Open == "door3":
					door3.PushButton()
				
	
			else:  		# 12345678 is the Password that Opens Garage Door (Code if Password is Incorrect)
				if code == "":
					code = "NULL"
				else:
					BadPassword += 1
					logfile = open("static/log.txt","a")
					logfile.write("     " + datetime.now().strftime(request.environ['REMOTE_ADDR'] + "     Password attempt:  -- %Y/%m/%d -- %H:%M  \n"))
					logfile.close()
					print(request.environ['REMOTE_ADDR'] + " -- " + str(BadPassword) + " wrong password(s) have been entered!")

				if BadPassword > 5:
					logfile = open("static/log.txt","a")
					logfile.write("     " + datetime.now().strftime(request.environ['REMOTE_ADDR'] + "     Too Many Wrong Passwords, System Disabled.  -- %Y/%m/%d -- %H:%M  \n"))
					logfile.close()
					print("Garage Code Entered: " + code)
		else:
			# No password required
			print("Door requested to open: " + Door_To_Open)
			No_Refresh += 1
			if Door_To_Open == "door1":
				door1.PushButton()
			if Door_To_Open == "door2":
				door2.PushButton()
			if Door_To_Open == "door3":
				door3.PushButton()
	
	print(door1.name + " is " + door1.GetStatus())

	if NUMBER_OF_DOORS >=2:
		print(door2.name + " is " + door2.GetStatus())

	if NUMBER_OF_DOORS == 3:
		print(door3.name + " is " + door3.GetStatus())
	
	Any_Door_Open = 0
	if door1.GetStatus()=="open":
		Any_Door_Open +=1
	if door2.GetStatus()=="open" and NUMBER_OF_DOORS >=2:
		Any_Door_Open +=1
	if door3.GetStatus()=="open" and NUMBER_OF_DOORS ==3:
		Any_Door_Open +=1

	if Any_Door_Open == 0:
		bgcolor = BG_COLOR_CLOSED
	if Any_Door_Open == 1:
		bgcolor = BG_COLOR_QUESTION
	if Any_Door_Open > 1:
		bgcolor = BG_COLOR_OPEN

	return render_template('doorstatus.txt',
		Refresher = No_Refresh,
		color = bgcolor, 
		door1status = door1.GetImage(), 
		door2status = door2.GetImage(), 
		door3status = door3.GetImage(), 
		doorstatussize = imagesize, 
		door1visable = door1.visible, 
		door2visable = door2.visible, 
		door3visable = door3.visible, 
		D1Name = door1.name, 
		D2Name = door2.name, 
		D3Name = door3.name)


@app.route('/Settings', methods=['GET', 'POST'])
def settings():
	if request.method == 'POST':
		if request.form['ADMIN'] == ADMIN and request.form['ADMIN_PASS'] == ADMIN_PASS:
			#open text file in read mode
			AutoStart = open("/etc/rc.local", "r")

			#read whole file to a string
			AutoStartFile = AutoStart.read()

			#close file
			AutoStart.close()

			if ENABLE_PASSWORD == "YES":
				ENABLE_PASSWORD_YES = " Checked"
				ENABLE_PASSWORD_NO = ""
			else:
				ENABLE_PASSWORD_YES = ""
				ENABLE_PASSWORD_NO = " Checked"

			if ENABLE_SIRI == "YES":
				ENABLE_SIRI_YES = " Checked"
				ENABLE_SIRI_NO = ""
			else:
				ENABLE_SIRI_YES = ""
				ENABLE_SIRI_NO = " Checked"

			return render_template('settings.txt',
				PORT = PORT,
				ENABLE_PASSWORD_YES = ENABLE_PASSWORD_YES,
				ENABLE_PASSWORD_NO = ENABLE_PASSWORD_NO,
				PASSWORD = PASSWORD,
				ENABLE_SIRI_YES = ENABLE_SIRI_YES,
				ENABLE_SIRI_NO = ENABLE_SIRI_NO,
				SIRI_PASSWORD = SIRI_PASSWORD,
				BG_COLOR_QUESTION = BG_COLOR_QUESTION,
				BG_COLOR_OPEN = BG_COLOR_OPEN,
				BG_COLOR_CLOSED = BG_COLOR_CLOSED,
				IMAGE_QUESTION = IMAGE_QUESTION,
				IMAGE_OPEN = IMAGE_OPEN,
				IMAGE_CLOSED = IMAGE_CLOSED,
				NUMBER_OF_DOORS = NUMBER_OF_DOORS,
				DOOR_1_NAME = DOOR_1_NAME,
				DOOR_2_NAME = DOOR_2_NAME,
				DOOR_3_NAME = DOOR_3_NAME,
				SENSORS_PER_DOOR = SENSORS_PER_DOOR,
				APIKEY = APIKEY,
				ADMIN = ADMIN,
				ADMIN_PASS = ADMIN_PASS,
				APP_PATH = APP_PATH,
				LOG_FILE = LOG_FILE,
				AutoStartFile = AutoStartFile)
		else:
			return app.send_static_file('admin_login.html')
	else:
		return app.send_static_file('admin_login.html')

@app.route('/ChangeSettings', methods=['POST'])
def ChangeSettings():

	PORT = request.form['PORT']
	ENABLE_PASSWORD = request.form['ENABLE_PASSWORD']
	PASSWORD = request.form['PASSWORD']
	ENABLE_SIRI = request.form['ENABLE_SIRI']
	SIRI_PASSWORD = request.form['SIRI_PASSWORD']
	NUMBER_OF_DOORS = request.form['NUMBER_OF_DOORS']
	DOOR_1_NAME = request.form['DOOR_1_NAME']
	DOOR_2_NAME = request.form['DOOR_2_NAME']
	DOOR_3_NAME = request.form['DOOR_3_NAME']
	SENSORS_PER_DOOR = request.form['SENSORS_PER_DOOR']
	APIKEY = request.form['APIKEY']
	ADMIN = request.form['ADMIN']
	ADMIN_PASS = request.form['ADMIN_PASS']

	#open text file in write mode (this will erase current file)
	ConfigFile = open("config.py", "w")

	#writes whole string to file
	ConfigFile.write('PORT = ' + PORT + '\n')
	ConfigFile.write('ENABLE_PASSWORD  = "' + ENABLE_PASSWORD + '"\n')
	ConfigFile.write('PASSWORD = "' + PASSWORD + '"\n')
	ConfigFile.write('ENABLE_SIRI = "' + ENABLE_SIRI + '"\n')
	ConfigFile.write('SIRI_PASSWORD = "' + SIRI_PASSWORD + '"\n')
	ConfigFile.write('BG_COLOR_QUESTION = "' + BG_COLOR_QUESTION + '"\n')
	ConfigFile.write('BG_COLOR_OPEN = "' + BG_COLOR_OPEN + '"\n')
	ConfigFile.write('BG_COLOR_CLOSED = "' + BG_COLOR_CLOSED + '"\n')
	ConfigFile.write('IMAGE_QUESTION = "' + IMAGE_QUESTION + '"\n')
	ConfigFile.write('IMAGE_OPEN  = "' + IMAGE_OPEN + '"\n')
	ConfigFile.write('IMAGE_CLOSED = "' + IMAGE_CLOSED + '"\n')
	ConfigFile.write('NUMBER_OF_DOORS = ' + NUMBER_OF_DOORS + '\n')
	ConfigFile.write('DOOR_1_NAME = "' + DOOR_1_NAME + '"\n')
	ConfigFile.write('DOOR_2_NAME = "' + DOOR_2_NAME + '"\n')
	ConfigFile.write('DOOR_3_NAME = "' + DOOR_3_NAME + '"\n')
	ConfigFile.write('SENSORS_PER_DOOR = ' + SENSORS_PER_DOOR + '\n')
	ConfigFile.write('APIKEY = "' + APIKEY + '"\n')
	ConfigFile.write('ADMIN = "' + ADMIN + '"\n')
	ConfigFile.write('ADMIN_PASS = "' + ADMIN_PASS + '"\n')

	#close file
	ConfigFile.close()

	return app.send_static_file('Settings_Saved.html')


@app.route('/Settings_Save_Bootfile', methods=['POST'])
def Settings_Save_Bootfile():
	StartFile = request.form['AutoStartFile']

	#open text file in write mode (this will erase current file)
	AutoStart = open("/etc/rc.local", "w")

	#writes whole string to file
	AutoStart.write(StartFile)

	#close file
	AutoStart.close()

	return app.send_static_file('Settings_Saved.html')


@app.route('/Delete_Log_File', methods=['POST'])
def Delete_Log_File():

	#open text file in write mode (this will erase current file)
	DeleteLogFile = open("static/log.txt", "w")

	DeleteLogFile.write(datetime.now().strftime("Log File Erased -- %Y/%m/%d -- %H:%M \n"))

	#close file
	DeleteLogFile.close()

	return app.send_static_file('Settings_Saved.html')


@app.route('/Siri/GarageDoorStatus', methods=['GET'])
def GarageDoorStatus():
	global door1
	global door2
	global door3
	siri_door1_message = ""
	siri_door2_message = ""
	siri_door3_message = ""
	Any_Door_Open = 0

	siri_door1_message = door1.name + " is " + door1.GetStatus()

	if NUMBER_OF_DOORS >=2:
		siri_door2_message = door2.name + " is " + door2.GetStatus()

	if NUMBER_OF_DOORS == 3:
		siri_door3_message = door3.name + " is " + door3.GetStatus()

	Any_Door_Open = 0
	if door1.GetStatus()=="open":
		Any_Door_Open +=1
	if door2.GetStatus()=="open" and NUMBER_OF_DOORS >=2:
		Any_Door_Open +=1
	if door3.GetStatus()=="open"and NUMBER_OF_DOORS ==3:
		Any_Door_Open +=1

	siri_message = ""
	if Any_Door_Open == 0:
		return 'All Doors are Closed'
	if Any_Door_Open != 0:

		if siri_door1_message != "":
			siri_message = siri_door1_message
		if siri_door2_message != "":
			if siri_message == "":
				siri_message = siri_door2_message
			else:
				siri_message = siri_message + ', ' + siri_door2_message
		if siri_door3_message != "":
			if siri_message == "":
				siri_message = siri_door3_message
			else:
				siri_message = siri_message + ', ' + siri_door3_message

		return siri_message

@app.route('/api/GetStatus', methods=['GET'])
def GetStatus():
	# Returns the status of a single door. The 'door' argument must be supplied in the url as an integer
	global door1
	global door2
	global door3
	resp = ""
	api_key = request.headers.get('apikey')
	door_to_check = request.args.get('door')

	if api_key != APIKEY:
		resp = "Invalid API key"
	else:
		if door_to_check =="":
			resp = "Argument 'door' is required"
		if door_to_check=="1":
			resp = door1.GetStatus()
		if door_to_check=="2":
			resp = door2.GetStatus()
		if door_to_check=="3":
			resp = door3.GetStatus()
	return resp

@app.route('/api/OpenDoor', methods=['GET'])
def OpenDoor():
	# Returns the status of a single door. The 'door' argument must be supplied in the url as an integer
	global door1
	global door2
	global door3
	resp = ""
	api_key = request.headers.get('apikey')
	door_to_check = request.args.get('door')

	if api_key != APIKEY:
		resp = "Invalid API key"
	else:
		if door_to_check =="":
			resp = "Argument 'door' is required"
		if door_to_check=="1":
			door1.PushButton()
			resp = "door 1 opened"
		if door_to_check=="2":
			door2.PushButton()
			resp = "door 2 opened"
		if door_to_check=="3":
			door3.PushButton()
			resp = "door 3 opened"
	return resp

@app.route('/api/CloseDoor', methods=['GET'])
def CloseDoor():
	# Returns the status of a single door. The 'door' argument must be supplied in the url as an integer
	global door1
	global door2
	global door3
	resp = ""
	api_key = request.headers.get('apikey')
	door_to_check = request.args.get('door')

	if api_key != APIKEY:
		resp = "Invalid API key"
	else:
		if door_to_check =="":
			resp = "Argument 'door' is required"
		if door_to_check=="1":
			door1.PushButton()
			resp = "door 1 closed"
		if door_to_check=="2":
			door2.PushButton()
			resp = "door 2 closed"
		if door_to_check=="3":
			door3.PushButton()
			resp = "door 3 closed"
	return resp

@app.route('/Siri/Garage', methods=['POST'])
def GarageSiri():
	ps = request.form['ps']
	what_door = request.form['door']
	dowhat = request.form['dowhat']
	global door1
	global door2
	global door3

	if ps == SIRI_PASSWORD:
		logfile = open("static/log.txt","a")
		logfile.write(datetime.now().strftime("%Y/%m/%d -- %H:%M:%S  -- " + request.environ['REMOTE_ADDR'] + " -- Garage Door Operated via Siri  \n"))
		logfile.close()

		if what_door == "Door1" and dowhat == "Open" and door1.GetStatus()!="open":
			print("Door 1 is currently Closed, let's open it.")
			door1.PushButton()
			return 'Garage Door Opening'
		if what_door == "Door1" and dowhat == "Close" and door1.GetStatus()!="closed":
			print("Garage is currently Open, let's close it.")
			door1.PushButton()
			return 'Garage Door Closing'
		
		if what_door == "Door2" and dowhat == "Open" and door2.GetStatus()!="open":
			print("Door 2 is currently Closed, let's open it.")
			door2.PushButton()
			return 'Garage Door Opening'
		if what_door == "Door2" and dowhat == "Close" and door2.GetStatus()!="closed":
			print("Garage is currently Open, let's close it.")
			door2.PushButton()
			return 'Garage Door Closing'

		if what_door == "Door3" and dowhat == "Open" and door3.GetStatus()!="open":
			print("Door 3 is currently Closed, let's open it.")
			door3.PushButton()
			return 'Garage Door Opening'
		if what_door == "Door3" and dowhat == "Close" and door3.GetStatus()!="closed":
			print("Door 3 is currently Open, let's close it.")
			door3.PushButton()
			return 'Garage Door Closing'
	else:
		return 'We have a problem'

@app.route('/stylesheet.css')
def stylesheet():
	return app.send_static_file('stylesheet.css')

@app.route('/Log')
def logfile():
	return app.send_static_file('log.txt')

@app.route('/images/<path:subpath>')
def SiriPics(subpath):
	return app.send_static_file('images/' + subpath)

@app.route('/page/<sendpage>')
def page(sendpage):
	return app.send_static_file(sendpage)

if __name__ == '__main__':
	app.run(debug=True, host=ip_address, port=PORT)
