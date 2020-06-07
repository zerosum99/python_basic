# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 11:07:13 2016

@author: 06411
"""

import socket
import time

local_t = time.localtime()

 
TCP_IP = '127.0.0.1'
TCP_PORT = 64
BUFFER_SIZE = 20  # Normally 1024, but we want fast response
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
 
conn, addr = s.accept()
print 'Connection address:', addr
while 1:
     data = conn.recv(BUFFER_SIZE)
     if not data: break
     print "received data:", data
     #conn.send(data)  # echo
     if "/version" in data:
         conn.send("Demo versionn")
         print " echo Demo versionn"
     
 
     if "/echo" in data:
         data = data.replace("/echo","")
         conn.send(str(local_t[0]) + "n")
 
conn.close()