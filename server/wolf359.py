#!/usr/bin/python3
import pickle
import hashlib
import sys
import wolfram
import socket
import gpio

from cryptography.fernet import Fernet

host = ""
port = 12397 # Reserve a port for your service
backlog = 5
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port)) #Bind to the port
s.listen(backlog) #Wait for the client connection
gpio.initGPIO()
while True:
	try:
		gpio.waitingForClient("on")
		client, addr = s.accept() #Establish a connection with the client
	except KeyboardInterrupt:
		gpio.cleanup()
		s.close()
		sys.exit()
	
	print ('Got connection from', addr)
	data = client.recv(size)

	gpio.waitingForClient("off")

	gpio.recieveFromClient("on")
	if data:
		server_payload = data
		myData = pickle.loads(server_payload)
		key, ciphertext, md5, servAddr = myData

		if md5 != hashlib.md5(ciphertext).hexdigest():
		    sys.exit(1)

		f = Fernet(key)
		question = f.decrypt(ciphertext)

		app_id = "T72KQ9-LE373U33UW"

		gpio.recieveFromClient("off")
		
		gpio.wolfSend("on")
		gpio.wolfSend("off")

		gpio.wolfRecieve("on")
		result = wolfram.askWolfram(app_id, question)
		gpio.wolfRecieve("off")

		gpio.sendToClient("on")
		ciphertext = f.encrypt(str.encode(result))

		checksum = hashlib.md5(ciphertext).hexdigest()

		# build the payload tuple
		payload = (ciphertext, checksum)
		# pickle up the payload
		pickle_payload = pickle.dumps(payload)

		client.send(pickle_payload)
		gpio.sendToClient("off")

		client.close()
		
