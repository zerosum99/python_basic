# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 10:43:55 2016

@author: 06411
"""

def check_admin(func) :
    def wrapper(*args, **kargs) :
        print ' aaaa ', args[1]
        if args[1] != 'admin' :
            raise Exception('This user is not allowed to get food')
        return func(*args, **kargs)
    return wrapper

class Store(object) :
    def __init__(self) :
        self.storage = {}
        
    def get(self,food) :
        return self.storage.get(food)
        
    def put(self,food) :
        self.storage[food] = food
        
    @check_admin    
    def get_food(self, username, food) :
                
        return self.get(food)
        
    @check_admin      
    def put_food(self, username, food) :
        self.put(food)
        
s = Store()
s.put_food('admin','orange')
print s.get_food('admin','orange')