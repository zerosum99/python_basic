# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 10:55:50 2016

@author: 06411
"""

class Mixin :
    def add(self,x,y) :
        return self.x + self.y
    
    def sub(self,x,y) :
        if isinstance(self, String) :
            return " String no support"
        else :
            return self.x - self.y


class Number(Mixin) :
    
    def __init__(self, x,y) :
        self.x = x
        self.y = y
        
class String(Mixin) :
    def __init__(self, x,y) :
        self.x = x
        self.y = y 

print ' Mixin reference  : ', id(Mixin)
print ' Mixin namespace  : ', Mixin.__dict__
print ' Number reference : ', id(Number)
print ' Number namespace  : ', Number.__dict__



n1 = Number(5,6)
print n1
print id(n1.add(n1.x, n1.y))
print 'Number add reference :', id(n1.add), ' add :', n1.add(n1.x,n1.y)

print 'Number sub reference :', id(n1.sub), ' sub :', n1.sub(n1.x,n1.y)

s1 = String("hello ", "world")
print s1.add(s1.x, s1.y)
print s1.sub(s1.x, s1.y)


class ComparableMixin(object):
    """This class has methods which use `<=` and `==`,
    but this class does NOT implement those methods."""
    def __ne__(self, other):
        return not (self == other)
    def __lt__(self, other):
        return self <= other and (self != other)
    def __gt__(self, other):
        return not self <= other
    def __ge__(self, other):
        return self == other or self > other

class Integer(ComparableMixin):
    def __init__(self, i):
        self.i = i
    def __le__(self, other):
        return self.i <= other.i
    def __eq__(self, other):
        return self.i == other.i

print Integer(0) <  Integer(1)
print Integer(0) != Integer(1)
print Integer(1) >  Integer(0)
print Integer(1) >= Integer(1)
