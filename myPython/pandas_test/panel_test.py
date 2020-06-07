# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 12:59:59 2016

@author: 06411
"""

import numpy as np
import pandas as pd

A = np.array(['one', 'one', 'two', 'two', 'three', 'three'])
B = np.array(['start', 'end']*3)
C = [np.random.randint(10, 99, 6)]*6
df = pd.DataFrame(zip(A, B, C), columns=['A', 'B', 'C'])


print(df)
print(df.index)
print(df.columns)
print(df["A"])
print(df[["A","C"]])
print(".....",df.ix[0:1])
print(".....", df[0:1])

print("============================================")
#print(df['one'])
print(df.ix[0])
print(df.ix[0:2])
print("============================================")
df.set_index(['A', 'B'], inplace=True)
print(df)
print(" index ", df.index)
#print(" value ", df.values)
#print(df['C'])
print("df.loc",df.loc['one'])
print("df.loc[one,start]", df.loc['one','start'])
print("df.iloc[0:3]", df.iloc[0:3])

#print(df['one','start'])
#print(df.blocks)

print('===========================================')
area_dict = {'California': 423967, 'Texas': 695662, 'New York': 141297, 'Florida': 170312, 'Illinois': 149995}
area = pd.Series(area_dict)

pop_dict = {'California': 1423967, 'Texas': 1695662, 'New York': 1141297, 'Florida': 1170312, 'Illinois': 1149995}
population = pd.Series(pop_dict)

states = pd.DataFrame({'population': population,
                       'area': area})
                       
print(states)   
print(states.index)
print(states.values)
print('===========================================')

           