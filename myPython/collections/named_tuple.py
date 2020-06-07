# -*- coding: utf-8 -*-
"""
Created on Mon Mar 07 16:41:25 2016

@author: 06411
"""
 
from collections import namedtuple
import inspect

Point = namedtuple('Point', ['x', 'y'], verbose= True,rename=True)

print Point

a = Point(10,11)
print a.count(10), a.index(10)
print a.x
print a.y
print a[0]
print a[1]
print inspect.getclasstree(a.__class__.__bases__)
b = tuple(a)
print b.count(10), b.index(10)

x = tuple(["dahl",29,'010-0000-0000'])
print x

NP = namedtuple("NP",('name','age','mobilephone'))
np = NP("dahl",29,'010-0000-0000')
print np
od = np._asdict()
print od
print od['name']


t =['moon',30,'010-0000-00001']
print NP._make(t)


from abc import ABCMeta, abstractmethod
class Foo(object):
    def __getitem__(self, index):
        pass
    def __len__(self):
        pass
    def get_iterator(self):
        return iter(self)

class MyIterable:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __iter__(self):
        while False:
            yield None

    def get_iterator(self):
        return self.__iter__()

    @classmethod
    def __subclasshook__(cls, C):
        if cls is MyIterable:
            if any("__iter__" in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented

print MyIterable.register(Foo)
