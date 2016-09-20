#!/usr/bin/python
import RPi.GPIO as GPIO  
import time  

def initGPIO():
	# pin 21 = blue, pin 20 = green, pin 16 = red
	GPIO.setmode( GPIO.BOARD )
	GPIO.setup(16, GPIO.OUT)
	#GPIO.setup(20, GPIO.OUT)
	GPIO.setup(21, GPIO.OUT)
	return

def waitingForClient( status ):
	#Red
	if status == True:
		GPIO.output(16, True)
		print("penis")
		time.sleep(3)
	elif status == False:
		GPIO.output(16,  False) 
	else:
		print("Invalid Argument")
		return
	return


def recieveFromClient( status ):
	#Yellow
	if status == true:
		GPIO.output(16, GPIO.HIGH)
		GPIO.output(20, GPIO.HIGH)
		time.sleep(3)
	elif status == false:
		GPIO.output(16,  GPIO.LOW) 
		GPIO.output(20, GPIO.LOW)
	else:
		print("Invalid Argument")
		return
	return

def wolfSend( status ):
	#Cyan 
	if status == true:
		GPIO.output(21, GPIO.HIGH)
		GPIO.output(20, GPIO.HIGH)
		time.sleep(3)
	elif status == false:
		GPIO.output(21,  GPIO.LOW) 
		GPIO.output(20, GPIO.LOW)
	else:
		print("Invalid Argument")
		return
	return

def wolfRecieve( status ):
	#magenta
	if status == true:
		GPIO.output(16, GPIO.HIGH)
		GPIO.output(21, GPIO.HIGH)
		time.sleep(3)
	elif status == false:
		GPIO.output(16,  GPIO.LOW) 
		GPIO.output(21, GPIO.LOW)
	else:
		print("Invalid Argument")
		return
	return

def sendToClient( status ):
	#White
	if status == true:
		GPIO.output(16, GPIO.HIGH)
		GPIO.output(21, GPIO.HIGH)
		GPIO.output(20, GPIO.HIGH)
		time.sleep(3)
	elif status == false:
		GPIO.output(16,  GPIO.LOW) 
		GPIO.output(21, GPIO.LOW)
		GPIO.output(20, GPIO.LOW)
	else:
		print("Invalid Argument")
		return
	return

initGPIO()
waitingForClient(True)