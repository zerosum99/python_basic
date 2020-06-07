# -*- coding: utf-8 -*-
"""
Created on Tue Dec 01 11:40:20 2015

@author: 06411
"""

class Counter :
    insCount =0
    
    def __init__(self) :
        Counter.insCount +=1
    @staticmethod
    def S_PrintCount() :
        print(" S instance count ",Counter.insCount )
    @classmethod 
    def C_PrintCount(cls) :
        print(" C instance count ",cls.insCount )
        

a,b,c = Counter(),Counter(), Counter()

a.S_PrintCount()
b.S_PrintCount()
c.S_PrintCount()

Counter.C_PrintCount()