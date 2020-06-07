# -*- coding: utf-8 -*-
"""
Created on Wed Apr 06 15:18:04 2016

@author: 06411
"""

class A(object):
    a1 = "A"
class B(object): 
    a2 = "B"
class C(A,B):   
    a3 = "C(A,B)"
class D(C):     
    a4 = "D(C)"

d = D()
d.a5 = "instance d of D"

print issubclass(D,C)

print issubclass(D,A), A.__subclasshook__(D)

print issubclass(A,B), B.__subclasshook__(A)

print isinstance(d,D)


class M(type):
    def __init__(cls, *args):
        cls.a = 'M.a'

class C(B): 
    __metaclass__=M

print C.a, C().a
print M.__subclasshook__(C)

class Base(object):
    def foo(self):
        raise NotImplementedError("foo")

    def bar(self):
        raise NotImplementedError("bar")

class Concrete(Base):
    
    def foo(self):
        return "foo() called" 
    def bar(self):
        return "bar() called" 
        
print dir(Base)
print Base.__subclasshook__(Concrete)

from abc import ABCMeta, abstractmethod
class Base1(object):
    __metaclass__=ABCMeta
    @abstractmethod
    def foo(self):
        pass 
    @abstractmethod
    def bar(self):
        pass
class Concrete1(Base1):
    def foo(self): 
         return " concrete foo "
    def bar(self): 
         return " concrete bar "

print Base1.__subclasshook__(Concrete1)
c = Concrete1()
print issubclass(Concrete1, Base1)

class Foo(object):
    def foo(self): 
         return " concrete foo "
    def bar(self): 
         return " concrete bar "

def class_factory():
    
    return Foo

F = class_factory()
f = F()
print(type(f))
print(f.foo())

def instance_factory():
    
    return Foo()

f = instance_factory()

print(type(f))
print(f.foo())




