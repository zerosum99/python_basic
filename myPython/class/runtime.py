# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 09:05:10 2016

@author: 06411
"""

def __init__(self,name) :
    self.name = name
    
def getName(self) :
    return self.name
    
def add_cls(cls,x,y) :
    return x+y
    
def add(x,y):
    return x+y

class A() :
    pass

print "Before : ", A.__dict__

A.__init__ = __init__
A.getName  = getName
A.add_cls = classmethod(add_cls)
A.add = staticmethod(add)

print " After :", A.__dict__




a = A("name")

print " a.getName ", a.getName()
print " cls add_cls ", A.add_cls(5,5)
print " static add ", A.add(5,5)

A.age = 30

print " age ", a.age

class X() :
    def add(self) :
        pass
    def add(self,x) :
        return x

x = X()
print X.__dict__
print x.add(5)