# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 11:33:29 2016

@author: 06411
"""

import pytz
import inspect

def des_f(method) :
      print "descripter " 
      return method 
      
class Base1(object):  
    def amethod(self): print "Base1"  

class Base2(Base1):  
    pass

class Base3(object):  
    def amethod(self): print "Base3"

class test(Base2,Base3) :
    A = 'aaaa'
     
    def __name__(self):
        return self.__name__
    
    @des_f
    def t_print(self) :
        ''' aaaa '''
        c = test()
        print 'c  test ', c
        print "test instance print ", self.A
    
    @classmethod
    def c_print(cls) :
        print " text class print ", cls.A
        
class test1 :
    print " test1 "
    

t = test()
t.c_print()
t.t_print()

print inspect.getmembers(t)

print inspect.isclass(test)
print inspect.isclass(t)
print inspect.ismethod(t.t_print)

print inspect.isfunction(t.t_print)
print inspect.ismethoddescriptor(test.c_print)
print inspect.ismethoddescriptor(int.__add__)

for k,v in inspect.getmembers(t) :
    if inspect.ismethoddescriptor(v) :
        pass
    else :
        print k

print inspect.getmoduleinfo('in_test.py')
print inspect.getmodulename('in_test.py')
print inspect.ismodule(pytz)

print int.__mro__

instance = test()  
instance.amethod()  
print test.__mro__  
print test.mro()
print int.mro()

# print test1.mro()