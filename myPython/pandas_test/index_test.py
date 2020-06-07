# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 11:52:12 2016

@author: 06411
"""

import pandas as pd
import inspect as ins
import numpy as np


for k, v in pd.Index.__dict__.items() :
    if  ins.isroutine(v) :
        print(k)
    else :
        continue
        
print("==================================")        
data = {'a':1,'b':2}
sr = pd.Series(data)

inx = sr.index

print(inx)

print(inx.values)
inx.name = 'dahl'
print(inx.name, inx.names, sr.index.name)
print(inx.nlevels)
print(inx.ndim)
print(inx.dtype, inx.dtype_str)
print(inx.hasnans)
print(inx.has_duplicates)
print(inx.inferred_type)
print(inx.is_unique)


inx1 = pd.Index([1, 2, 3,'a', 4])
print(inx1)
print(inx1.name, inx1.names)
print(inx1.nlevels)
print(inx1.ndim)
print(inx1.dtype, inx1.dtype_str)
print(inx1.hasnans)
print(inx1.has_duplicates)
print(inx1.inferred_type)
print(inx1.is_unique)

print("2222222222222222222222222222222222")
inx2 = pd.Index([1, 2, 3,3, 4])
print(inx2.sort_values())
print(inx2.order())
print(inx2.duplicated())

inx3 = pd.Index([1,2,3,4,5])
print(inx3[inx3[:] > 3])
print("all ", inx3[3>0].all())
print("any ", inx3.any())

inx4 = pd.Index([1,2])
inx5 = inx4.union(pd.Index([3]))
print(inx5)


inx6 = inx3.intersection(inx4)
print(inx6)

print pd.Index([1,2,3,4]).append(pd.Index([5,6]))
ia = pd.Index([1,2,3,4])
ib = pd.Index([5,6])
ic = ia.append(ib)
print ic
idc =ic.drop(6)
print idc

idd = idc.delete(4)
print idd

ide = idd.insert(4,5)
print ide


print ide.get_value(pd.Series(['a','b','c','d','e']),1)
ide.set_value(ide,5,6)
print ide
print ide.get_values()

print("3333333333333333333333333333333333333")

inx = pd.Index(['a','b','c','d'])
data = [1,2,3,4]

sr = pd.Series(data,index=inx)
print(sr.values)
print(sr.index)
print(sr.describe())