# -*- coding: utf-8 -*-
"""
Created on Thu Mar 03 14:32:27 2016

@author: 06411
"""
import types

class A(object) :
    def __init__(self,name) :
        self.name = name
        
a = A('dahl')
print a.name

print(" instance type ", type(a))
print(types.ClassType == type(A))
print(type(a) is types.InstanceType)
print(" class type ", type(A))
print(" class type ", a.__class__.__bases__)
print(isinstance(a,object))
print(isinstance(a,type))
print(type.mro(A))

class B():
    def __init__(self,name) :
        self.name = name

b = B('moon')
print type(b)
print(" class type ", type(B))
print(type(b) is types.InstanceType)
print(types.ClassType == type(B))


print('====================================')
class C(object) :
   def __new__(cls) :
       return super(C, cls).__new__(cls)
       
   def __init__(self,name) :
       self.name = name

c = C.__new__(C)
print c
print type(c)
print c.__class__
print isinstance(c,C)

c.__init__('dahl')
print c.name
print('====================================')
class D: 
    def __init__(self): 
        print "init"
    def __call__(self):
        print "call" 
D()   # init     
D()() # init call

d = D()  #init
d()         # call
