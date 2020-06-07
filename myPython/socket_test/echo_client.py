# -*- coding: utf-8 -*-
"""
Created on Mon Feb 01 15:17:17 2016

@author: 06411
"""

# Echo client program
import socket

HOST = 'localhost'              # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while 1 : 
    data = raw_input('> ') 
    if not data: break
    s.send(data)
    data = s.recv(1024)
    if not data: break
    print 'Received', repr(data)
s.close()