# -*- coding: utf-8 -*-
"""
Created on Thu Mar 03 16:19:05 2016

@author: 06411
"""

def add(x,y) :
    return x+y
print add.__class__
print type(add.func_code)   
print add.__class__.__bases__
print add.func_code.__class__.__bases__

print add.__call__(5,5)


print object.__class__
print object.__doc__
print object.__str__("objct")
print int.__repr__(1)
print object.__new__
p = list.__new__(list)
p.__init__([1,2])

print object.__init__, p
print object.__call__
i = int.__call__(5)
print i

class A(object) :
    def __init__(self) :
        self.name = None
        self.age  = None
a = A()  
print a.__dict__        
print object.__delattr__(a,"age")
print object.__setattr__(a,"name",'dahl')
print object.__getattribute__(a,"name")
print a.__dict__
print object.__format__("1234","4.2s")
print object.__hash__(id(p))
print object.__sizeof__(p)


