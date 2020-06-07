# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 17:43:21 2016

@author: 06411
"""

class MyClass(object):
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        

class MyClass1(object):
    __slots__ = ['name', 'identifier']
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        
x = MyClass('a',1234)
print x

y = MyClass1('b',1345)
print y
