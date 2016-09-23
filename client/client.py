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
    print(type(ciphertext))
    checksum = hashlib.md5(ciphertext).hexdigest()

    # build the payload tuple
    payload = (key, ciphertext, checksum, host)
    # pickle up the payload
    pickle_payload = pickle.dumps(payload)

    # create socket and send
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    s.send(pickle_payload)

    # recieve the response and close the socket
    data = s.recv(size)
    s.close()

    response_payload = pickle.loads(data)
    response_ciphertext = response_payload[0]
    response_md5 = response_payload[1]

    # verify checksum    
    if response_md5 != hashlib.md5(response_ciphertext).hexdigest():
        print("MD5 checksum does not match calculated checksum")
        sys.exit(1)

    #decrypt response
    plainTextByte = f.decrypt(response_ciphertext)
    
    print(plainTextByte)

#    answer = str.decode(plainTextByte)

#    print(answer)

if __name__ == "__main__":
    parser = ArgumentParser(description='Parse options for the Otexta')
    parser.add_argument('question')
    parser.add_argument('host')
    opt_args = parser.parse_args()

    # execute only if run as a script
    main(opt_args)
