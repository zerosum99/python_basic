# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 15:22:05 2016

@author: 06411
"""

def func_return(func) :
    return func
    
def x_print() :
    print(" x print ")
    
x = func_return(x_print)
x()

@func_return
def r_print() :
    print (" r print ")
    

r_print()

