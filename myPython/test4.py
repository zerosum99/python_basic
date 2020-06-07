# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 17:03:18 2015

@author: 06411
"""

class Person :
    "부모 클래스 "
    def __init__(self, name, phoneNumber) :
        self.Name = name
        self.PhoneNumber = phoneNumber
        
    def PrintInfo(self):
        print self.Name, self.PhoneNumber
        
        
class Child(Person) :
    def __init__(self, name,phoneNumber,age) :
        
        Person.__init__(self,name, phoneNumber)
        #self.Name = name
        #self.PhoneNumber = phoneNumber
        self.Age = age
        
    def PrintInfo(self) :
        print " Child ", self.Name, self.PhoneNumber
        
    def PrintChildInfo(self) :
        print self.Name, self.PhoneNumber, self.Age
        

p = Person("dahl", "111111")
p.PrintInfo()

print p.__dict__

c = Child("moon", '2222222', 33)
c.PrintChildInfo()
c.PrintInfo()

print c.__dict__

print "Class Person ", Person.__dict__
print "Class Child ", Child.__dict__

