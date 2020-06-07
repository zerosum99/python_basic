# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 13:23:40 2016

@author: 06411
"""

import pandas as pd
import inspect as ins

names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]
BabyDataSet = list(zip(names,births))

df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])
print(df)

dd = {'names': names, 'births':births}
df1 = pd.DataFrame(dd)

print(df1)

'''
print(df.shape)
print(df.index)
print(df.columns)
print(df.axes)

print(df.dtypes)
print(df.at.__dict__)
print("scalar accessor ",df.at[0,'Names'])
print(df.ndim, type(df.ndim))
print("==============================")
print(df.blocks, type(df.blocks))
print(df.blocks['object'])
print(df.blocks['int64'])
print("==============================")
print(df.empty)
print(df.ftypes)
print(df.iat.__dict__)
print("scalar accessor ",df.iat[0,1])
print(df.iloc.__dict__)
print(df.iloc[0])
print(df.ix[0])
print("==============================")
print(df.T)
print(df.size)
print(df.values)
print(df.loc[0,'Births'])

print(df.ix[1,'Names'])
print(df.iloc[0,1])
'''