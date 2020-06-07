# -*- coding: utf-8 -*-
"""
Created on Tue Dec 01 06:28:26 2015

@author: 06411
"""

def Times(a,b) :
    return a*b
    
print("time function call  %d" % Times(10,10))
print(Times)
print(type(Times))
print(id(Times))

if __name__ == "main" :
    print("Hello World")
else:
    print("Hello World no main ")