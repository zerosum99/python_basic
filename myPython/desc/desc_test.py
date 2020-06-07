# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 10:03:42 2016

@author: 06411
"""

import inspect

class TypedProperty(object):

    def __init__(self, name, type, default=None):
        self.name = "_" + name
        self.type = type
        self.default = default if default else type()
    
    def __get__(self, instance, cls):
        return getattr(instance, self.name, self.default)
    
    def __set__(self,instance,value):
        if not isinstance(value,self.type):
            raise TypeError("Must be a %s" % self.type) 
        setattr(instance,self.name,value)

    def __delete__(self,instance):
        raise AttributeError("Can't delete attribute")


class Person(object):
    name = TypedProperty("name",str) 
    age = TypedProperty("age",int,42)
    
    
acct = Person()
print " ========================================================="
print " acct __dict__ ", acct.__dict__
print " Person __dict __ ", Person.__dict__
print " ========================================================="


print('method descriptor', inspect.isdatadescriptor(TypedProperty))
acct.name = "obi"
acct.age = 1234
print " ========================================================="
print " acct __dict__ ", acct.__dict__
print " Person __dict __ ", Person.__dict__
print " ========================================================="
print " acct age ",Person.__dict__["age"].__get__(acct,Person)
print Person.__dict__["age"].__dict__
print " acct name ",Person.__dict__["name"].__get__(acct,Person)
print Person.__dict__["name"].__dict__

print " ========================================================="
print " descriptor ", TypedProperty.__get__(TypedProperty("name",str),acct,Person)
print('data descriptor', inspect.isdatadescriptor(TypedProperty))
print acct.age #1234
print acct.name #obi
# trying to assign a string to number fails
#acct.age = '1234'   
   
    