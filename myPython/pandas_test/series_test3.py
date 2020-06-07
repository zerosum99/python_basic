# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 15:16:57 2016

@author: 06411
"""

import pandas as pd
import numpy as np

obj = pd.Series(data=[1,2,3,4],index=['a','b','c','d'],name="something")

print(obj.index)
print(obj.values)
print(obj.name)
print(obj.dtype)



obj1 = pd.DataFrame(data=np.arange(16).reshape(4,4),index=['a','b','c','d'],
                    columns=['a','b','c','d'])

print(obj1.index)
print(obj1.columns)
print(obj1.values)
print(obj1.dtypes)

print(obj1['a'])
print(obj1['a'] > 5)
print(obj1[obj1['a'] >5])

print(obj1.replace(to_replace=0,value=999,inplace=True))
print(obj1)
print(obj1.replace(to_replace=2,value=888,inplace=True))
print(obj1)
print(obj1['d'].replace(3,777,inplace=True))
print(obj1)


obj1 = pd.DataFrame(data=np.arange(16).reshape(4,4),index=['a','b','c','d'],
                    columns=['a','b','c','d'])
print(obj1.sort_values('a',inplace=True))
print(obj1)

obj3 = obj1.reindex(['d','c','a','b'])
print(obj3)
obj3.index = [0,1,2,3]
print(obj3)

d = {'a' : { 0 : 1, 1 : 2},
     'b' : { 0 : 1, 1 : 2},}

obj7 = pd.DataFrame(d)
print(obj7)
print("add ",obj7 + obj7)
print("sub ",obj7 - obj7)
print("mul ",obj7 * obj7)
print("div ",obj7 / obj7)
print("//  ",obj7 // obj7)
print(" %  ",obj7 % obj7)



