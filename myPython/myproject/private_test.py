# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 17:26:23 2015

@author: 06411
"""

class Cup:
    def __init__(self):
        self.color = None
        self._content = None # protected variable

    def fill(self, beverage):
        self._content = beverage

    def empty(self):
        self._content = None
        
    def add(cls) :
        print(" class ")
        
    def add_class(cls) :
        cls.add()
        print(" class method ")
     
    """ TypeError: unbound method static_m() must be called with Cup instance as first argument (got nothing instead)  """ 
    #def static_m() :
    #    print('')
        
        
    @staticmethod    
    def static_m() :
        print('static method ')
        


cup = Cup()
cup._content = "tea"
print(cup._content)
cup.add_class()

Cup.static_m()

# cup.add()   ypeError: add() takes no arguments
# Cup.add()  TypeError: unbound method add() must be called with Cup instance as first argument (got nothing instead)