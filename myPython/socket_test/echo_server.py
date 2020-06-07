# -*- coding: utf-8 -*-
"""
Created on Mon Feb 01 15:16:53 2016

@author: 06411
"""

import socket

HOST = 'localhost'                  # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

# 서버 순환
while 1:
    conn, addr = s.accept()
    print 'Connected by', addr
    
    #클라이언트 순환
    while 1 : 
        data = conn.recv(1024)
        if not data: break
        conn.send(data)
    conn.close()
    break
s.close()