# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 08:41:00 2016

@author: 06411
"""

class Test(dict) :
           
    def __getattr__(self,name) : 
        #print " Test instance __dict__ :",self.__dict__
        return self.__dict__[name]
    def __setattr__(self,name, value) : 
        self.__dict__[name] = value
   
class Test1(dict) :
    def __getattr__(self,name) : 
        #print " Test instance __dict__ :",self.__dict__
        return self[name]
    def __setattr__(self,name, value) : 
        self[name] = value
               
class Test2(list) :
    
   
    def __getattr__(self,index) : 
        #print " Test instance __dict__ :",self.__dict__
        return self[index]
    def __setattr__(self,value) : 
        self.append(value)
        #self[len(self)] = value    #IndexError: list assignment index out of range
    
t = Test()
t.a= 10
t['btest'] = 100

print t.a
print t['btest']
print t.__dict__
print t


t1 = Test1()
t1.a= 10
t1['btest'] = 100

print t1.a
print t1['btest']
print t1.__dict__
print t1

t2 = Test2()
t2.__setattr__(100)
print t2.__dict__
print t2[0]
