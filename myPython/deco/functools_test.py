# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 17:57:00 2016

@author: 06411
"""
import functools
from functools import wraps
def my_decorator(f):
     @wraps(f)
     def wrapper(*args, **kwds):
         print 'Calling decorated function'
         return f(*args, **kwds)
         
     print "my ", locals()
     return wrapper

@my_decorator
def example():
     """Docstring"""
     
     print 'example ',locals()
     print " func tools ", functools.__dict__['WRAPPER_ASSIGNMENTS']
     print 'Called example function'



example()

def my_decorator0(x) :
    print x   
    def my_decorator1(f):
         @wraps(f)
         def wrapper(*args, **kwds):
             print 'Calling decorated function'
             return f(*args, **kwds)
         print "wraps func ",wrapper
         return wrapper
    return my_decorator1
     

@my_decorator0('xxx')
def example1():
     """Docstring"""
     print 'Called example function'
     
example1()