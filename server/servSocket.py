#!/usr/bin/python
import socket #import the socket module

def createServSocket():
	host = ""
	port = 12397 # Reserve a port for your service
	backlog = 5
	size = 1024
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host, port)) #Bind to the port
	s.listen(backlog) #Wait for the client connection
	while True:
		print ("in server socket")
		client, addr = s.accept() #Establish a connection with the client
		print ('Got connection from',addr)
		data = client.recv(size)
		#extract the package in data
		#close the socket

		#client.close()
