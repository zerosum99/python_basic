# -*- coding: utf-8 -*-
"""
Created on Thu Mar 03 10:11:37 2016

@author: 06411
"""
import inspect
import dis

class Foobar:
    pass

print type(Foobar)   # <type 'classobj'>
print Foobar         #__main__.Foobar

foo = Foobar()
print type(foo)       #<type 'instance'>


print " meta class "


class Meta():
    __metaclass__= type
    pass

class Complex(Meta):
   pass


print type(Complex), type(Meta)
print issubclass(Complex,Meta)

a = []
print dir(a)
print type(a)
print inspect.getmembers(a)
print inspect.getargspec(a)



def check(obj) :
    pass