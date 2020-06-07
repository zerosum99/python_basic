# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 11:28:29 2016

@author: 06411
"""

class A() :
    name = " class variable"
    A_name = " A_name class variable "
    
    
    def __init__(self, name=None) :
        self.name = name
        

a = A("instanc variable")
print " instance variable ", a.name
print " class variable ",A.name
print " class variable ",a.A_name
print A.__dict__
print a.__dict__


class B() :
    name = "class variable "
    def __init__(self) :
        self.name =   B.name
        
b = B()
print b.name

print " C class processing "
class C() :
    __name = "class variable "
    def __init__(self) :
        self.name = self.__name
        
c = C()

print c.name 
print c._C__name
print C.__dict__
print c.__dict__
#print c.__name
        
