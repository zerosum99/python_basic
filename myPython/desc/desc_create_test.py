# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 10:45:54 2016

@author: 06411
"""

class Descriptor(object):

    def __init__(self):
        self._name = ''

    def __get__(self, instance, owner):
        print "Getting: %s" % instance.__dict__['_name']
        return instance.__dict__['_name'] #self._name

    def __set__(self, instance, value):
        instance.__dict__['_name'] = value
        print "Setting: %s" % instance.__dict__['_name']

    def __delete__(self, instance):
        print "Deleting: %s" % instance.__dict__['_name']
        del instance.__dict__['_name']
   
class Descriptor1(object):
    """
    def __get__(self, instance, owner):
        print "Getting: %s" % instance.__dict__['age']
        return instance.__dict__['age'] #self._name

    def __set__(self, instance, value):
        instance.__dict__['age'] = value
        
    """

    def __init__(self):
        self._age = "_age"


    def __get__(self, instance, cls):
        return getattr(instance,self._age)
        #return instance.__dict__['age']

    def __set__(self,instance,value):
        setattr(instance, "age", value)
        #instance.__dict__['age'] = value

    def __delete__(self, instance):
        print "Deleting: %s" % instance.__dict__['age']
        delattr(instance,self._age)
        #del instance.__dict__['age'] 
             
        

class Person(object):
    name = Descriptor()
    age  = Descriptor1()
    
user = Person()

print user.__dict__
user.name = 'john smith' #Setting: john smith
print user.__dict__
print "user.name ",user.name
user.age = 20
print user.__dict__
print "user.age", user.age, " user.age"
print user.__dict__
#del user.name # Deleting: John Smit


print " descriptor call "
user1 = Person()

print " set call  ", Descriptor.__set__(Descriptor(),user1,"dahl")
print " get call  ", Descriptor.__get__(Descriptor(),user1,Descriptor)
print user1.__dict__
