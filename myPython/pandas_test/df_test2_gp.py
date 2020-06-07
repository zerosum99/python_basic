# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 14:48:54 2016

@author: 06411
"""

import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(30).reshape(5,6))
print(df.describe())
print("df mean ",df.mean())
print(df[0].describe())



df1 = df.copy()
df1[0] = ['A','B','B','C','C']
print(df1)
print(df1[1])
print(df1[1].groupby(df1[0]))
print(list(df1[1].groupby(df1[0])))
print(df1.groupby(df1[0]).mean())

df1[1] = ['1','2','2','3','3']
print(df1.groupby([0,1]).mean())

print(df1.groupby([0,1]).size())
print(df1.groupby([0,1]).obj)
print("=========================================")   
for name, group in df1.groupby([0,1]): 
    # print the name of the regiment
    print(name)
    # print the data of that regiment
    print(group)
    
    
print("=========================================")   
df = pd.DataFrame(np.arange(30).reshape(5,6))
df1[0] = ['A','B','B','C','C']
df1[1] = ['1','2','2','3','3']
print(df1.groupby([0,1]).obj)
print(df1.groupby([0,1]).mean())
print(df1.groupby([0,1]).size())

print(" series  ", type(df1[2].groupby(df1[0])))

print(df1[2].groupby(df1[0]).obj)
print(df1[2].groupby(df1[0]).mean())
print(df1[2].groupby(df1[0]).size())
print("=========================================") 
for name, group in df1[2].groupby(df1[0]): 
    # print the name of the regiment
    print(name)
    # print the data of that regiment
    print(group)
