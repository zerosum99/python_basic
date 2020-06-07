# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 11:22:50 2016

@author: 06411
"""

import pandas as pd
import numpy  as np

df = pd.DataFrame(np.arange(16).reshape(4,4),index=['a','b','c','d'],
                  columns=['f','g','h','i'])
                  
print(df)

df0 = df.copy()
print(df0)
print(id(df), id(df0))
print( (df0 == df).all())
print(df0 is df)

print(" index ", df.axes[0])
print(" columns ", df.axes[1])

df1 = df.astype(np.float64)
print(df1['f'])

df2 = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print(df2)
print(df2['f'].isnull())
print(df2['f'].notnull())


print(df.iteritems())
for col, val in df.iteritems() :
    print(col, val)
print(df.iterrows())
for row, val in df.iterrows() :
    print(row, val)
    
print(df.itertuples())
for row in df.itertuples() :
    print(row)
    
for row in df.itertuples(index=False) :
    print(row)
    
print(df.insert(4,'j',[99,999,999,9999]))
print(df)
print(df.pop('j'))
print(df.index, df.columns)


print(df)
df[['f','g']] = df[['g','f']]
print(df)


print("dataframe add ", df.add(df))
print("dataframe sub ", df.sub(df))
print("dataframe mul ", df.mul(df))
print("dataframe div ", df.div(df))
print("dataframe truediv ", df.truediv(df))
print("dataframe floordiv ", df.floordiv(df))
print("dataframe mod ", df.mod(df))

print("dataframe add ", df['f'].add(df['f']))
print("dataframe sub ", df['f'].sub(df['f']))
print("dataframe mul ", df['f'].mul(df['f']))
print("dataframe div ", df['f'].div(df['f']))
print("dataframe truediv ", df['f'].truediv(df['f']))
print("dataframe floordiv ", df['f'].floordiv(df['f']))
print("dataframe mod ", df['f'].mod(df['f']))

df = pd.DataFrame(np.arange(16).reshape(4,4),index=['a','b','c','d'],
                  columns=['f','g','h','i'])
df1 = pd.DataFrame(np.arange(16,32).reshape(4,4),index=['a','b','c','d'],
                  columns=['f','g','h','i'])
print(df0)
print(df1)
print("dataframe radd ", df.radd(df1))
print("dataframe rsub ", df.rsub(df1))
print("dataframe rmul ", df.rmul(df1))
print("dataframe rdiv ", df.rdiv(df1))
print("dataframe rtruediv ", df.rtruediv(df1))
print("dataframe rfloordiv ", df.rfloordiv(df1))
print("dataframe rmod ", df.rmod(df1))

print("dataframe radd ", df['f'].radd(df1['f']))
print("dataframe rsub ", df['f'].rsub(df1['f']))
print("dataframe rmul ", df['f'].rmul(df1['f']))
print("dataframe rdiv ", df['f'].rdiv(df1['f']))
print("dataframe rtruediv ", df['f'].rtruediv(df1['f']))
print("dataframe rfloordiv ", df['f'].rfloordiv(df1['f']))
print("dataframe rmod ", df['f'].rmod(df1['f']))


df = pd.DataFrame(np.arange(16).reshape(4,4),index=['a','b','c','d'],
                  columns=['f','g','h','i'])
                  
print(pd.concat([df,df]))
print(pd.concat([df,df],axis=1))
print('+++++++++++++++++++++++++++++++++++++++')
print(pd.merge(df,df1,on='f'))
print(pd.merge(df,df,left_on='f', right_on = 'f'))


raw_data = {
        'subject_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'], 
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}
df_a = pd.DataFrame(raw_data, columns = ['subject_id', 'first_name', 'last_name'])


raw_data = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'], 
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}
df_b = pd.DataFrame(raw_data, columns = ['subject_id', 'first_name', 'last_name'])
print(pd.merge(df_a, df_b, on='subject_id'))
print(pd.merge(df_a, df_b, on='subject_id', how='outer'))
print(pd.merge(df_a, df_b, on='subject_id', how='inner'))

print(df.sum(axis=0))
print(df.mean(axis=0))
print(df.std(axis=0))
print(df.var(axis=0))

print(df.sum(axis=1))
print(df.mean(axis=1))
print(df.std(axis=1))
print(df.var(axis=1))

print(df.min(axis=0))
print(df.max(axis=0))
print(df.min(axis=1))
print(df.max(axis=1))

print((df == df).all(axis=0))
print((df == df).all(axis=1))
print(df)
print((df >  5).any(axis=0))
print((df >  5).any(axis=1))

df1 = pd.DataFrame()
print(df.empty)
print(df1.empty)

print(df.equals(df))