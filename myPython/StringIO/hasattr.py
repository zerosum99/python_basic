# -*- coding: utf-8 -*-
"""
Created on Thu Mar 03 09:14:27 2016

@author: 06411
"""

class A(object) :
    def __init__(self,name) :
        self.name = name
        
    def hasattr(self, attrname):
                   
        
        if hasattr(self,attrname) :
            val = "B"
            if attrname in A.__dict__ :
                val = "A"
            if attrname in self.__dict__ :
                val = "S"
        else :
            val = "N"
        return val
        
         
        
    
a = A("dahl")

print hasattr(a,"name")
print hasattr(a,"__str__")
print hasattr(object,"__str__")
print a.hasattr("__str__")
print a.hasattr("name")
print a.hasattr("__init__")
print A.__dict__
