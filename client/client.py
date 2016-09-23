#!/usr/bin/python3
import socket
import sys

from argparse import ArgumentParser

def main(opt_args):
    self.question = opt_args.question
    self.host = opt_args.host

def createSocket():
    print ("in Client")
    s = socket.socket() #create a socket object
    host = '172.30.47.95' #Host i.p
    port = 12397 #Reserve a port for your service

    s.connect((host,port))
    print (s.recv(1024))
    s.close


if __name__ == "__main__":
    parser = ArgumentParser(description='Parse options for the Otexta')
    parser.add_argument('question')
    parser.add_argument('host')
    opt_args = parser.parse_args()

    # execute only if run as a script
    main(opt_args)
