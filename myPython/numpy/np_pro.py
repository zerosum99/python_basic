# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 15:30:46 2016

@author: 06411
"""

class Person(object) :
    def __init__(self,name) :
        self._name = name
        
    @property
    def name(self) :
        return self._name
        
    @name.setter
    def name(self,name) :
        self._name = name
        
a = Person("moon")
a.name = "dahl"
print a.name

print a.__dict__
print Person.__dict__['name']
print Person.__dict__['name'].__get__(a)
print Person.__dict__['name'].__set__(a,"xxx")
print Person.__dict__['name'].__get__(a)
print Person.__dict__['name'].__get__
print Person.__dict__['name'].__set__
swg = object.__getattribute__
sws = object.__setattr__
print swg
print sws
print a.__setattr__('name',"1"), a.__setattr__
print a.__getattribute__('name')