#!/usr/bin/python
import RPi.GPIO as GPIO  
import time  

def initGPIO():
	# pin 21 = blue, pin 20 = green, pin 16 = red
	GPIO.setmode( GPIO.BCM )
	GPIO.setup(16, GPIO.OUT)
	GPIO.setup(20, GPIO.OUT)
	GPIO.setup(21, GPIO.OUT)
	GPIO.setwarnings(False)
	return

def cleanup():
	GPIO.cleanup()
	return

def waitingForClient( status ):
	#Red
	if status == "on":
		GPIO.output(16, True)
		print("Server waiting for question payload")
		time.sleep(3)
	elif status == "off":
		GPIO.output(16,  False) 
	else:
		print("Invalid Argument: waitingForClient")
		return
	return


def recieveFromClient( status ):
	#Yellow
	if status == "on":
		GPIO.output(16, GPIO.HIGH)
		GPIO.output(20, GPIO.HIGH)
		print("Recieving Question Payload")
		time.sleep(3)
	elif status == "off":
		GPIO.output(16,  GPIO.LOW) 
		GPIO.output(20, GPIO.LOW)
	else:
		print("Invalid Argument: recieveFromClient")
		return
	return

def wolfSend( status ):
	#Cyan 
	if status == "on":
		GPIO.output(21, GPIO.HIGH)
		GPIO.output(20, GPIO.HIGH)
		print("Sending question to Wolfram")
		time.sleep(3)
	elif status == "off":
		GPIO.output(21,  GPIO.LOW) 
		GPIO.output(20, GPIO.LOW)
	else:
		print("Invalid Argument: wolfSend")
		return
	return

def wolfRecieve( status ):
	#magenta
	if status == "on":
		GPIO.output(16, GPIO.HIGH)
		GPIO.output(21, GPIO.HIGH)
		print("Recieved answer from Wolfram, constructing return payload")
		time.sleep(3)
	elif status == "off":
		GPIO.output(16,  GPIO.LOW) 
		GPIO.output(21, GPIO.LOW)
	else:
		print("Invalid Argument: wolfRecieve")
		return
	return

def sendToClient( status ):
	#White
	if status == "on":
		GPIO.output(16, GPIO.HIGH)
		GPIO.output(21, GPIO.HIGH)
		GPIO.output(20, GPIO.HIGH)
		print("Sending answer payload to client")
		time.sleep(3)
	elif status == "off":
		GPIO.output(16,  GPIO.LOW) 
		GPIO.output(21, GPIO.LOW)
		GPIO.output(20, GPIO.LOW)
	else:
		print("Invalid Argument: sendToClient")
		return
	return

