# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 08:39:41 2016

@author: 06411
"""

class A(object):
    
    def __init__(self) :
        self.instanceS = " static instance member"
    def whoami(self):
        return self.__class__.__name__

a = A()

print a
print a.whoami()
print dir(a)
print a.__class__.__base__.__name__
print dir(a.__class__.__base__)

print "A.__dict__",A.__dict__

print a.__getattribute__('whoami')
print a.__dict__

a.instanceR = "runtime instance member"

print " a.__dict__ ", a.__dict__


#class 정의하고 인스턴스에서 타 객체를 호출
class C:
   def __init__(self ):
       print 'a'
       self.b = B()
       
   def ccc(self, b) :
       return b.bbb()

 #object  chain을 하는 class 생성
class B:
     def __init__(self ):
       print 'b'
      
     def bbb(self):
         print "B instance method "
             
a = C()

print a.b.bbb()
print a.ccc(B())
