# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 16:40:57 2016

@author: 06411
"""


import inspect

def func(*args,**kargs) :
    print "locals() ", locals()
    func_args = inspect.getcallargs(func,*args,**kargs)
    print " func_args ", func_args
    print " inspect get call args ", inspect.getcallargs(func,*args,**kargs)
    value = 0
    for i in func_args['args'] :
        value += i
        
    items = func_args['kargs'] 
    for k,v in items.items() :
        value += v
    
    return value
    
    
print func(1,2,3,x=1)
