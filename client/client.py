#!/usr/bin/python3
import hashlib
import pickle
import socket
import sys

from argparse import ArgumentParser
from cryptography.fernet import Fernet

def main(opt_args):
    # setup our question, host, and port
    question = opt_args.question
    host = opt_args.host
    port = 12397
    size = 1024

    # do the encryption and checksumming
    key = Fernet.generate_key()
    f = Fernet(key)
    ciphertext = f.encrypt(str.encode(question))
    checksum = hashlib.md5(ciphertext).hexdigest()

    # build the payload tuple
    payload = (key, ciphertext, checksum, host)
    # pickle up the payload
    pickle_payload = pickle.dumps(payload)

    # create socket and send
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    s.send(pickle_payload)

    # recieve the response
    data = s.recv(size)
    # close the socket
    s.close()
    print ('Received:', data)

if __name__ == "__main__":
    parser = ArgumentParser(description='Parse options for the Otexta')
    parser.add_argument('question')
    parser.add_argument('host')
    opt_args = parser.parse_args()

    # execute only if run as a script
    main(opt_args)
