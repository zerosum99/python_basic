# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 15:37:51 2016

@author: 06411
"""

class A:
   def __init__(self ):
       print 'a'
       self.b = B()
   
    
class B:
    
     def __init__(self ):
       self.c = C()
       print 'b'
      
     def bbb(self):
         print "B instance method "
         return self.c
         
class C:
    
     def __init__(self ):
       print 'c'
      
     def ccc(self):
         print "C instance method "   
     
     
a = A()

print a.b.bbb().ccc()
