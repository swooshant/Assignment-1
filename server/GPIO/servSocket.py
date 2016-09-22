#!/usr/bin/python
import socket #import the socket module

def createServSocket():
	s = socket.socket() #Create a socket object
	port = 12397 # Reserve a port for your service
	s.bind(('', port)) #Bind to the port

	s.listen(5) #Wait for the client connection
	while True:
		print ("in server")
		c, addr = s.accept() #Establish a connection with the client
		print ('Got connection from',addr)
		c.send(b'Wuzzup')
		c.close()

createServSocket()