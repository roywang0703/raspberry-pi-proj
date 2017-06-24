#!/usr/bin/python
import socket               # Import socket module
import sys

class Connector:
    def __init__(self, host='liu1ee.cs.uwindsor.ca', port=5000):
        self.host = host
        self.port = port
        self.skt = socket.socket()         # Create a socket object
        self.is_connected = False
    def connect(self):
        try:
            self.skt.connect((self.host, self.port))
            self.is_connected = True
        except socket.error, e:
            return 'error to connect server: {0}'.format(self.host)
    def getmsg(self):
        while True:
            backstr = self.skt.recv(1024)
            if backstr == 'bye!':
                print 'server terminates connection. Bye!'
                break
            else:
                print backstr
    def disconnect(self):
        self.skt.close
cli = Connector()
cli.connect()
cli.getmsg()
cli.disconnect()
