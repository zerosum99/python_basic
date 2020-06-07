# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 14:10:23 2016

@author: 06411
"""

class A() :
    __slots__ =['person_id', 'name']
    def __init__(self, person_id, name) :
        self.person_id = person_id
        self.name = name
        
    def __getattr__(self, name) :
        return self.__dict__[name]
            
    def __setattr__(self, name, value):
        if name in A.__slots__ :
            self.__dict__[name] = value
        else:
            raise Exception(" no match attribute")
          
    def __delattr__(self, name) :
        del self.__dict__[name]
 

    def __getattribute__(self, name):
        return self.__dict__[name]

a = A(1,'dahl')

print a.__getattr__('name')
print a.__getattr__('person_id')

print a.__dict__


print a.__setattr__('name','moon')
print a.__setattr__('person_id',2)

print a.__getattr__('name')
print a.__getattr__('person_id')

print a.__delattr__('name')
print a.__dict__

a.name = 'gahl'

#a.s = 1

print a.__dict__
