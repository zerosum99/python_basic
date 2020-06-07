# -*- coding: utf-8 -*-
"""
Created on Fri Mar 04 11:08:11 2016

@author: 06411
"""

class atomic(int) :
    
    def __init__(self,obj) :
        self = int(obj)
        
    def __add__(self,obj) :
        value = int(self) + int(obj)
        return atomic(value)

i = atomic(1)

print type(i), i
i = atomic(i +1)
print type(i), i
j = i.__add__(10)
print type(j), j