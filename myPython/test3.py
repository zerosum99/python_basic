# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 18:40:56 2015

@author: 06411
"""

str = " not " 

class GString :
    str = ""
    def __init__(self,msg) :
        self.str = msg
        
    def Set(self,msg) :
        self.str = msg
        
    def Get(self) :
        print self.str
        
    def Print(self) :
        print(str)
        
    def __del__(self) :
        print("class delete ")
        
    def StaticMethod() :
        print  "Static Method "
        
    SM = staticmethod(StaticMethod)
    
    def ClassMethod(cls) :
        print "Class Method "
        
    CM = classmethod(ClassMethod)
    
        

g = GString("bbb")
g.Set(" First ")
g.Print()
g.Get()

print isinstance(g, GString)
print type(g)
print type(g) == GString

GString.SM()

def Add(x,y) : 
    return x+y
    
    
d = {"ADD": Add}

print "Add Call", d["ADD"](1,2)

def Foo() :
    f = GString("aaa")
    f.Get()
    
   # GString.StaticMethod()
    f.CM()
    GString.CM()
    
    
Foo()