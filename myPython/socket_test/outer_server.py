# -*- coding: utf-8 -*-
"""
Created on Mon Feb 01 17:46:09 2016

@author: 06411
"""

import socket # for socket
import sys 

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Socket successfully created"
except socket.error as err:
    print "socket creation failed with error %s" %(err)

# default port for socket
port = 80

try:
    host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:
    # this means could not resolve the host
    print "there was an error resolving the host"
    sys.exit()

# connecting to the server
s.connect((host_ip,port))

print "the socket has successfully connected to google \
on port == %s" %(host_ip)