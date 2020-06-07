# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 09:37:29 2016

@author: 06411
"""

def external_bar(self,lastname):
    self.lastname = lastname
    return self.name+ " " + self.lastname
    
def ext__init__(self, name=None) :
    self.name = name
    
    

class Foo() :
    def __init__(self,name=None) :
        self.name = name
    bar = external_bar
    
class Bar() :
    def __init__(self,name=None) :
        self.name = name
    bar = external_bar
    
class Car() :
    __init__ = ext__init__
    
class Car1() :
     __init__ = ext__init__
        
        
foo = Foo('Dahl')
print " Foo context  ", id(Foo), Foo.__dict__
print " foo context  ", id(foo), foo.__dict__
print foo.name

foo1 = Foo()
Foo.__init__(foo1,"Yong")
print " Foo context  ", id(Foo), Foo.__dict__
print " foo1 context ", id(foo1), foo1.__dict__
print foo1.name

print foo1.bar("Moon")
print foo1.__dict__

bar = Bar("Gi")
bar.bar("Wang")
print bar.__dict__

car = Car("BMW")
car1=Car1()
Car1.__init__(car1,'Ford')
print car.__dict__
print car1.__dict__