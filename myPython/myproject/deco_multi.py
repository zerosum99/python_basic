# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 15:07:01 2016

@author: 06411
"""

def f1(func) :
    def wrap_1(*args) :
        return func(*args)
    print " f1 call"
    return wrap_1
    
def f2(func) :
    def wrap_2(*args) :
        return func(*args)
    print "f2 call"
    return wrap_2
    
@f1
@f2
def add(x,y) : 
    print " add call "
    return x +y
    
print add(5,5)

print f2(add)
print f1(f2(add))

print f1(f2(add))(5,5)