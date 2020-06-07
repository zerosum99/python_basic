# -*- coding: utf-8 -*-
"""
Created on Tue May 03 10:43:13 2016

@author: 06411
"""

class Other(object):

    def override(self):
        print "OTHER override()"

    def implicit(self):
        print "OTHER implicit()"

    def altered(self):
        print "OTHER altered()"

class Child(object):

    def __init__(self):
        self.other = Other()
        self.types = type

    def implicit(self):
        self.other.implicit()

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE OTHER altered()"
        self.other.altered()
        print "CHILD, AFTER OTHER altered()"
        
    def type_s(self, ty_val=None) :
        if ty_val == None :
            ty_val = self
        return self.types(ty_val)

son = Child()

son.implicit()
son.override()
son.altered()
print(son.__str__())

print(son.type_s(1))
print(son.type_s())



print(object.__class__.__base__)

print(Other.__dict__)
print(Child.__dict__)
print(son.__dict__)
print(son.other.__dict__)
print(object.__dict__)

import inspect

print(type(inspect))
print(inspect.__dict__)

'''
class A(object) :
    def __init__(self,name) :
        self.name = name
    def get_name(self) :
        return self.name
        
a = A('dahl')
print(" instance namespace ", a.__dict__)
print(" class namespace  ", A.__dict__)
print(" base namespace  ", object.__dict__)

'''

def a(x, *args):
    return sum(args)
def b(x, args, y, **kwargs):
    pass

print a(1,*(1,2,3,4))