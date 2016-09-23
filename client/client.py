#!/usr/bin/python3
import hashlib
import pickle
import socket
import sys

from argparse import ArgumentParser
from cryptography.fernet import Fernet

def main(opt_args):
    question = opt_args.question
    host = opt_args.host
    port = 12397

    key = Fernet.generate_key()
    f = Fernet(key)
    ciphertext = f.encrypt(str.encode(question))
    checksum = hashlib.md5(ciphertext).hexdigest()

    payload = (key, ciphertext, checksum, host)
    
    pickle_payload = pickle.dumps(payload)

if __name__ == "__main__":
    parser = ArgumentParser(description='Parse options for the Otexta')
    parser.add_argument('question')
    parser.add_argument('host')
    opt_args = parser.parse_args()

    # execute only if run as a script
    main(opt_args)
