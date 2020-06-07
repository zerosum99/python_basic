# -*- coding: utf-8 -*-
"""
Created on Wed Apr 06 17:03:36 2016

@author: 06411
"""


def interface(func) :
    
    def common(*args) :
        if args[0] == 'mul' :
            result = 1
        else :
            result = 0
        
        for i in args[1:] :
            if args[0] == 'add' :
                result += i
            if args[0] == 'mul' :
                result *= i
        return result
    
    def decorator(*args) :
        return common(func.__name__,*args)
        
    return decorator
    
@interface
def add(x,y) :
    pass

@interface
def mul(x,y) :
    pass

    
print add(5,5)
print mul(5,5)    