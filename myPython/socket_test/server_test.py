# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 14:19:21 2016

@author: 06411
"""

import socket
  
TCP_IP = '127.0.0.1'
TCP_PORT = 51874
BUFFER_SIZE = 20  # Normally 1024, but we want fast response
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#blocing mode
s.setblocking(1)
s.settimeout(10)

#sock bind
s.bind((TCP_IP, TCP_PORT))

print " socket info ",socket.SOL_SOCKET, socket.SO_REUSEADDR


while 1:
    s.listen(5) 
    connection_list = [s]
    conn, addr = s.accept()
    print 'Connection address:', addr
    print "connection list ",len(connection_list)
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print "received data:", data
    conn.send(data)  # echo
conn.close()