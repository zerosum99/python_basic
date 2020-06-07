# -*- coding: utf-8 -*-
"""
Created on Wed Apr 06 16:41:23 2016

@author: 06411
"""

import abc
def interface(*attributes):
    def decorator(Base):

        def checker(Other):
            return all(hasattr(Other, a) for a in attributes)
        def ins_checker(Other):
            if type(Other) == Base :
                return True
            return False

        def __subclasshook__(cls, Other):
            if checker(Other):
                return True
            return NotImplemented

        def __instancecheck__(cls, Other):
            return ins_checker(Other)

        Base.__subclasshook__ = classmethod(__subclasshook__)
        Base.__instancecheck__ = classmethod(__instancecheck__)
        return Base

    return decorator

@interface("x", "y")
class Foo(object):
    __metaclass__ = abc.ABCMeta
    def x(self): return 5
    def y(self): return 10

class Bar(object):
    def x(self): return "blah"
    def y(self): return "blah"

class Baz(object):
    def __init__(self):
        self.x = "blah"
        self.y = "blah"

class attrdict(dict):
    def __getattr__(self, attr):
        return self[attr]

f = Foo()
b = Bar()
z = Baz()
t = attrdict({"x":27.5, "z":37.5})

print isinstance(f, Foo)
print isinstance(b, Foo)
print isinstance(z, Foo)
print isinstance(t, Foo)
print "hook ",Foo.__subclasshook__(f),Foo.__subclasshook__(t)
print "instance ",Foo.__instancecheck__(f),Foo.__instancecheck__(b)