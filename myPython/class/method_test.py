# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 12:18:21 2016

@author: 06411
"""

class A(object) :
    #@classmethod
    def __new__(cls) :
        self = object.__new__(cls)
        return self
    
    def __init__(self,name) :
        self.name = name
        
    def __del__(self) :
        del self
    def __str__(self) :
        return object.__str__(self)
        
    def __repr__(self) :
        return object.__repr__(self) 
    

a = A.__new__(A)
print a
print A.__init__(a,"dahl")
print a.name

print a.__str__()
print a.__repr__()

print A.__weakref__


class Old(object) :
    old_a = "oldstyle"
    

o = Old()
print Old.__dict__
print o.old_a
print o.__getattribute__('old_a')
print o.__setattr__("age",50), o.__getattribute__('age')
print o.__dict__
print o.__delattr__('age')
print o.__dict__



class D(object) :
        
    def __init__(self,name) :
        self.name = '_'+name
        
    def __get__(self,instance,owner) :
        return getattr(instance,self.name,None)
    def __set__(self,instance, value) :
        setattr(instance,self.name,value)
        
class Person(object) :
    name = D('name')
    
p = Person()
p.name = 'dahl'
print p.__dict__
print "class binding ", Person.__dict__['name'].__get__(p,Person)
print "direct binding ", p.name


l = [1,2,3]
m = {'k':1,'l':2}
print l.__getitem__(0)
print m.__getitem__('k')

l.__setitem__(2,4)
m.__setitem__('m',3)
print l
print m

print l, l.__contains__(2)
print m, m.__contains__('l')

lr = l.__reversed__()
print lr, l
for i in lr.__iter__() :
    print i
print l.__len__(), m.__len__()
    
    
s = "hello world"
ls = [1,2,3,4,5]
print s.__getslice__(0,5)
print ls.__setslice__(0,2,[99,99]), ls
ls.__delslice__(0,2)
print ls
