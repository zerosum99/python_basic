# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 13:41:09 2016

@author: 06411
"""

class Vector(object): 
    def __init__(self, a, b): 
        self.a = a 
        self.b = b 
    def __str__(self): 
        return 'Vector (%d, %d)' % (self.a, self.b)
    def __add__(self,other):
        return Vector(self.a + other.a, self.b + other.b) 

# __init__ 생성자 메소드 overloading
v1 = Vector(2,10) 
v2 = Vector(5,-2) 

# __add__ 메소드 overloading 
print v1 + v2 
print v1
