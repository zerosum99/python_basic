# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 10:19:21 2016

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

class A(object) :
    v = " get method descriptor "
    def __get__(self,instance,cls) :
        return A.v
        
class B(A) :
    pass
        
aa = A()
bb = B()
cc = TypedProperty('name',str,'dahl')

print ("inspect Method Descripter", inspect.ismethoddescriptor(aa))
print (" direct call",aa.__get__(None,A))
#type(a).__dict__[‘x’].__get__(a, type(a)).
print(" Instance Binding ", type(aa).__dict__['v'])
print A.__get__(aa,None,A)
print super(B,bb), B.mro() 
print super(B,bb).__get__(bb,B) # self를 자동으로 인식
print type(aa).__get__(aa,None,A)

class C(object) :
    def __init__(self, x) :
        self.x = x
        
    def __get__(self,instance=None,cls=None) :
        return self.x

c = C(1)

print c.__dict__
print c.x
print C.__get__(c)
print type(c).__get__(c)

class D(object) :
    def __init__(self, x) :
        self.x = x
        
    def __get__(self,instance=None,cls=None) :
        return self.x
        
class D1(D) :
    
    def __init__(self, x) :
        D.__init__(self,x)
    
  
d = D(1)
print " d"
print d.__dict__
print d.x
print " direct call",d.__get__()
print " Class binding call ",D.__get__(d,d)
print "instance binding",type(d).__get__(d,d)
d1 = D1(2)
print " d1"
print d1.__dict__
print d1.x
print " direct call",d1.__get__()
print " Class binding call ", D1.__get__(d1,d1)
print "instance binding",type(d1).__get__(d1,d1)
print D1.mro()
print "super binding",super(D1,d1).__get__(d1,d1)

