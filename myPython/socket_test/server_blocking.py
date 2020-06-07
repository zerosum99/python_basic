# -*- coding: utf-8 -*-
"""
Created on Mon Feb 01 11:44:44 2016

@author: 06411
"""

import socket

def test_socket_modes() :
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setblocking(1)
    s.settimeout(0.5)
    s.bind(("127.0.0.1",0))
    
    socket_address = s.getsockname()
    print " socket : ", str(socket_address)
    
    while 1 :
        s.listen(1)
        
if __name__ == "__main__" :
    test_socket_modes()