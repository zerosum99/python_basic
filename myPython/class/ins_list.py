# -*- coding: utf-8 -*-
"""
Created on Thu Mar 03 12:44:55 2016

@author: 06411
"""

class List(list) :
    def __init__(self,value) :
        self.append(value)
      
    def pop(self) :
        self.pop()
        
l = List(1)
print l


class A:
    pass
b = A()
print(type(b))
print(type(b).__dict__)
