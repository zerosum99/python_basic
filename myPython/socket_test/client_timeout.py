# -*- coding: utf-8 -*-
"""
Created on Tue Feb 02 11:09:29 2016

@author: 06411
"""

import socket
TCP_IP = '127.0.0.1'
TCP_PORT = 51874
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

print "received data:", data