# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 16:36:58 2016

@author: 06411
"""
import pandas as pd

# Our small data set
d = [0,1,2,3,4,5,6,7,8,9]

# Create dataframe
df = pd.DataFrame(d)
print(df)

df.columns = ['Rev']
print(df)

df['NewCol'] = 5
print(df)

df['NewCol'] = df['NewCol'] + 1
print(df)

del df['NewCol']
print(df)

df['col'] = df['Rev']
print(df)

i = ['a','b','c','d','e','f','g','h','i','j']
df.index = i
print(df)
print(df.loc['a'])
print(df.loc['a':'c'])
print(df['Rev'])
print(df[['Rev', 'col']])

print(df.ix[0:3,'Rev'])
print(df.ix[:3,['col', 'Rev']])
print(df.head())
print(df.tail())


d = {'one':[1,1,1,1,1],
     'two':[2,2,2,2,2],
     'letter':['a','a','b','b','c']}

# Create dataframe
df1 = pd.DataFrame(d)
one = df1.groupby('letter')
print(one.__dict__)
print(one.sum())

letterone = df1.groupby(['letter','one']).sum()
print(letterone)
print(letterone.index)

lettertwo = df1.groupby(['letter','one'], as_index=False).sum()
print(lettertwo)
print(lettertwo.index)
