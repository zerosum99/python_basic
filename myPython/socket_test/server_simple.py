# -*- coding: utf-8 -*-
"""
Created on Mon Feb 01 12:50:31 2016

@author: 06411
"""

import socket               # Import socket module

s = socket.socket()         # Create a socket object



host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port


s.listen(1)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   c.send('Thank you for connecting')
   print c.recv(1024)
   c.send(' hi client ')
   c.close()
   break
s.close()                  # Close the connection    s.close()