#!/usr/bin/python3
import servSocket
import pickle
import hashlib
import sys
import wolfram

from cryptography.fernet import Fernet

server_payload = servSocket.createServSocket()
myData = pickle.loads(server_payload)

print(myData)
key, ciphertext, md5, servAddr = myData

if md5 != hashlib.md5(ciphertext).hexdigest():
    print("MD5 checksum does not match calculated checksum")
    sys.exit(1)

f = Fernet(key)
question = f.decrypt(ciphertext)

app_id = "T72KQ9-LE373U33UW"
result = wolfram.askWolfram(app_id, question)

print(result)
