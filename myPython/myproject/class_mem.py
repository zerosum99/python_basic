# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 12:59:58 2016

@author: 06411
"""

class Class_Member :
    cls_var = 0
 
    @classmethod   
    def cls_method(cls) :
        cls.cls_var = 1
        print("call cls_method ", cls.cls_var)
        
    @staticmethod
    def sta_method() :
        cls_var = 100
        print("call sta_method ", cls_var)
        
    def ins_method(self) :
        self.ins_var = 1
        print('call ins method ', self.ins_var)
        
    print(' ins_ method ', id(ins_method))
    
    
    
Class_Member.cls_method()
Class_Member.sta_method()

print(Class_Member.__dict__)

c = Class_Member()
print(" c.ins_method ", id(c.ins_method))
c.ins_method()
print(c.__dict__)