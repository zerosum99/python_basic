# -*- coding: utf-8 -*-
"""
Created on Tue Dec 01 11:11:44 2015

@author: 06411
"""

import time
 
def elapsed_time(functor):
    
    def decorated(*args, **kwargs):
        start = time.time()
        functor(args, kwargs)
        end = time.time()
        
        print "Elasped time : %f" %(end - start)
        
    return decorated
 
@elapsed_time
def print_hello(*args, **kwargs):
    print "hello" 
    
    
print_hello()