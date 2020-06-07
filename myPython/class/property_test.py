# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 15:10:16 2016

@author: 06411
"""

class Person(object) :
    def __init__(self,name,age) :
        self._name = name
        self.age = age
        
    @property
    def name(self) :
        return self._name
        
    @name.setter
    def name(self,name) :
        self._name = name
        
        
p = Person('dahl',24)

print p.__dict__
print Person.__dict__

p.name = "moon"
print p.__dict__
