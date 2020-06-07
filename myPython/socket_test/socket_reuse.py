# -*- coding: utf-8 -*-
"""
Created on Mon Feb 01 12:05:37 2016

@author: 06411
"""

import socket
#import sys

def reuse_socket_addr() :
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    old_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print "old_state :", old_state
    
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    
    new_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print "new_state :", new_state
    
    local_port = 8282
    
    print " socket id ", id(sock)
    
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    srv.bind(('',local_port))
    
    srv.listen(1)
    print " local port ", local_port
    
    while 1 :
        try :
            connection, addr = srv.accept()
            print " Connection addr ", addr[0], addr[1]
            
        except KeyboardInterrupt :
            break
        except socket.error, e :
            print " socket error ", e
            
if __name__ == "__main__" :
    reuse_socket_addr()
    