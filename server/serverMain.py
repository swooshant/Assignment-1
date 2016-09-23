#!/usr/bin/python3
import servSocket.py
import pickle
import hashlib
import sys

from cryptography.fernet import Fernet

server_payload = servSocket.createServSocket()
myData = pickle.dumps(server_payload)

print(myData)
