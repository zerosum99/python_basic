# -*- coding: utf-8 -*-
"""
Created on Tue Feb 02 11:01:13 2016

@author: 06411
"""

import socket
import sys

TCP_IP = '127.0.0.1'
TCP_PORT = 51874
BUFFER_SIZE = 1024

def test_socket_modes() :
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setblocking(1)
    s.settimeout(0.5)
   
    s.bind((TCP_IP,TCP_PORT))
    
    socket_address = s.getsockname()
    print " socket : ", str(socket_address)
    s.listen(1)
    while 1 :
         client, address = s.accept()
         while 1 : 
             data = client.recv(1024)
             if not data: break
             client.send(data)
         client.close()
         break
    s.close()
        
if __name__ == "__main__" :
    try :
       test_socket_modes()
    except socket.timeout, e :
        print " timeout :", e
        sys.exit()