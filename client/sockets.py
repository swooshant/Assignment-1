#!/usr/bin/python
import socket

def createSocket():
#	host = ''
#	port = 12397
#	size = 2048
#	cliSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#	cliSocket.connect((host, port))
#	cliSocket.send(b'yo bitch you got me?')
#	dataRecv = cliSocket.recv(size)
#	cliSocket.close()
#
#	print (dataRecv)
	print ("in Client")
	s = socket.socket() #create a socket object
	host = '172.30.47.95' #Host i.p
	port = 12397 #Reserve a port for your service

	s.connect((host,port))
	print (s.recv(1024))
	s.close


createSocket()

