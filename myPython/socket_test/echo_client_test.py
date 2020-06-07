# -*- coding: utf-8 -*-
"""
Created on Mon Feb 01 17:17:40 2016

@author: 06411
"""

import socket
import sys

import argparse

host = 'localhost'

def echo_client(port) :
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_address = (host,port)
    
    print " connection to ", server_address
    sock.connect(server_address)
    
    try:
        message = " Test message. This will be echeed"
        print " Sending ", message
        sock.sendall(message)
        
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print " Received ", data
        
    except socket.errno,e :
        print " socket error ", str(e)
    except Exception, e :
        print " other error ", str(2)
    finally:
        print " Closing connection to the server "
        sock.close()
        
if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description='socket server example')
    parser.add_argument('--port',action="store",dest="port",type=int,required=True)
    given_args = parser.parse_args()
    port = given_args.port
    
    echo_client(port)
    
    