#!/usr/bin/python
import gpio as testGPIO
import time, sys

testGPIO.initGPIO()
while True:
	try:
		testGPIO.waitingForClient( "on" )
		testGPIO.waitingForClient( "off" )
		testGPIO.recieveFromClient( "on" )
		testGPIO.recieveFromClient( "off" )
		testGPIO.wolfSend( "on" )
		testGPIO.wolfSend( "off" )
		testGPIO.wolfRecieve( "on" )
		testGPIO.wolfRecieve( "off" )
		testGPIO.sendToClient( "on" )
		testGPIO.sendToClient( "off" )
	except KeyboardInterrupt:
		testGPIO.cleanup()
		sys.exit()