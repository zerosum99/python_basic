# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 10:29:26 2016

@author: 06411
"""

class Store(object) :
    def __init__(self) :
        self.storage = {}
        
    def get(self,food) :
        return self.storage[food]
        
    def put(self,food) :
        self.storage[food] = food
        
    def get_food(self, username, food) :
        if username != 'admin' :
            raise Exception(' This user is not allowed to get food')
        
        return self.get(food)
        
    def put_food(self, username, food) :
        if username != 'admin' :
            raise Exception(' This user is not allowed to get food')
        self.put(food)
        
s = Store()
s.put_food('admin','orange')
print s.get_food('admin','orange')
