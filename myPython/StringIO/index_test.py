# -*- coding: utf-8 -*-
"""
Created on Mon May 02 13:38:32 2016

@author: 06411
"""

s = "Hello World"
print(type(s[0]),s[0])
print(type(s[0:1]), s[0:1])

l = [1,2,3,4]
print(type(l[0]), l[0])
print(type(l[0:1]), l[0:1])

t = (1,2,3,4)
print(type(t[0]), t[0])
print(type(t[0:1]), t[0:1])

sl = slice(0,3)

print(s[sl])
print(l[sl])
print(t[sl])


import array
ar1 = array.array('c','abcdef')

ar2 = array.array('c','helloworld')
print(ar1)
print(type(ar1[0]), ar1[0])
print(type(ar1[0:3]), ar1[0:3])

l = [1,2,3]
sl1 = slice(0,2)
print l.__getitem__(0)
print l.__getitem__(sl1)
l.__setitem__(2,4)
print l


import numpy as np
import pandas as pd
s = pd.Series([0,1,2,3,4])
sv = s[0:1]
sv[:] = 999
print(" sv ", sv)
print("  s ", s)

l = [1,2,3]
ls = l[0:1]
print(" ls ", ls)
ls[0] = 999
print(" ls ", ls)
print(" l ", l)


s = pd.Series([0,1,2,3,4])
sv = s[[0,1]]
print("indexing ")
print(" sv ", sv)
print(s.__getitem__([0,1]))
print("  s ", s)




# Create dataframe
df = pd.DataFrame(np.arange(10).reshape(2,5))
i = ['a','b']
df.index = i
print(df)
print(df.index)
print("column",df[0])
print(df.loc['a'])
print("row + column ",df.ix[['a'],0:1])


