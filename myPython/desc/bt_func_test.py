# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 17:30:04 2016

@author: 06411
"""


class A():
    def __init__(self, name,age) :
        self.name = name
        self.age = age
        
    def in_set(self,name,default) :
        self.__dict__[name] = default
        print self.__dict__[name]


a = A('dahl',50)

if hasattr(a,"name") :
    print getattr(a,"name")
    setattr(a,"name","Moon")
    print getattr(a,"name")
else : 
    pass

if hasattr(a,"age") :
    print getattr(a,"age")
else : 
    pass

def add(x,y) :
    return x+y
    
if callable(add) :
    add(5,6)
else :
    pass

if callable(a.in_set) :
    a.in_set('age',20)
else:
    pass
