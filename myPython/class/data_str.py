# -*- coding: utf-8 -*-
"""
Created on Fri Mar 04 09:57:34 2016

@author: 06411
"""

class L(list) :
    def __init__(self,obj) :
        self.append(list(obj))
        
 
    
 
        
l = L([1,2,3])
#l = [1,2,3]
print type(l), l
l.append(1)
print type(l), l

print " dictionary "
class D(dict) :
        
    def __init__(self,obj) :
        self.update(obj)
    
    def __getattr__(self,name) : 
        return self[name]
    def __setattr__(self,name, value) : 
        self[name] = value

        
d = D(dict(k=5))

#d = {1:1}
d.l =1
print d
print d.has_key('l'), d['l']

print type(d)





class Test1(dict) :
    def __getattr__(self,name) : 
        return self[name]
    def __setattr__(self,name, value) : 
        self[name] = value

t1 = Test1()

t1.a= 10
t1.b =20
t1['btest'] = 100

print t1.a
print t1['btest']
print t1.__dict__
print t1

