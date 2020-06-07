# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 13:53:14 2016

@author: 06411
"""

import inspect 

class RevealAccess(object):
    """A data descriptor that sets and returns values
       normally and prints a message logging their access.
    """

    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print 'Retrieving', self.name
        return self.val

    def __set__(self, obj, val):
        print 'Updating', self.name
        self.val = val

class MyClass(object):
    x = RevealAccess(10, 'var "x"')
    print inspect.isdatadescriptor(x)
    
    
    y = 5
    
m = MyClass()
print m.x
print inspect.isdatadescriptor(m.x)