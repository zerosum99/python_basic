# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 11:24:42 2016

@author: 06411
"""

# Import all libraries needed for the tutorial

# General syntax to import specific functions in a library: 
##from (library) import (specific library function)
from pandas import DataFrame, read_csv

# General syntax to import a library but no functions: 
##import (library) as (give the library a nickname/alias)
import matplotlib.pyplot as plt
import pandas as pd #this is how I usually import pandas
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number

print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)


# The inital set of baby names and bith rates
names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]
BabyDataSet = list(zip(names,births))
print(BabyDataSet)

df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])
print(df)

df.to_csv('births1880.csv',index=False,header=False)
# header 인식
df1 = pd.read_csv('births1880.csv')
print(df1)
#  header  제거
df2 = pd.read_csv('births1880.csv',header=None)
print(df2)
# header 부여
df3 = pd.read_csv('births1880.csv', names=['Names','Births'])
print(df3)

print(df3.dtypes)
print(df3.Names.dtype)