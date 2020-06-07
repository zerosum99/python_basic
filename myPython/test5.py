# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 18:53:20 2015

@author: 06411
"""

class SuperClass :
    x = 10
    def PrintX(self):
        print self.x

class SubClass(SuperClass) :
    y = 20
    def PrintY(self) :
        print self.y
        
s = SubClass()
s.a = 30
s.x = 50

print "SubClass instance ", s.__dict__
print "SuperClass ", SuperClass.__dict__