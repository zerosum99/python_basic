# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 10:49:59 2016

@author: 06411
"""

import socket
import return_check as ret


def get_ipaddress(obj) :
    ''' 
    get ip address 
    '''
    
    print " host name :", obj

    ip_addr = socket.gethostbyname(obj)
    
    print ret.return_type(ip_addr)
    print " ip address :", ip_addr
    
    
def get_service(obj) :
    service =socket.getservbyport(obj,'tcp') 
    print " port : " + str(obj) + " service name : " + service
    

        
obj = socket.gethostname()
print ret.return_type(obj)  
get_ipaddress(obj)
obj = 'localhost'
get_ipaddress(obj)
obj = 'www.python.org'
get_ipaddress(obj)


print ' get port '
get_service(80)
get_service(53)
get_service(25)