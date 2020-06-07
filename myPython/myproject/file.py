# -*- coding: utf-8 -*-
"""
Created on Thu Dec 03 16:15:57 2015

@author: 06411
"""

f = open("aaa.txt", 'w')

for i in range(1, 11):
    data = "%d is line.\n" % i
    f.write(data)


f.close()

f = open("aaa.txt", 'r')
print f.tell()

for line in f.readline() :
    print line
    print f.tell()
f.close()
