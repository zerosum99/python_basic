# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 09:52:10 2016

@author: 06411
"""

def identity(f) :
    return f
    
_functions = {}

def register(f) :
    global _functions
    _functions[f.__name__] = f
    return f
    
@identity
@register
def foo() :
    return 'bar'
    

print foo()

print _functions['foo']()


#common function 처리하기
import inspect

