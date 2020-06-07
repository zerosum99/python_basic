# -*- coding: utf-8 -*-
"""
Created on Tue Mar 08 12:30:41 2016

@author: 06411
"""

from collections import Counter

s = Counter("abceabde")
s2 = Counter("defabc")
print "s  : ",s
print "s2 :",s2

# counter 더하기 

sadd = s+s2
print " s + s2 :",sadd

#counter  빼기

ssub = s - s2
print " s - s2 :",ssub

ssub2 = s2 - s
print " s2 - s :",ssub2

# 교집합
sadd = s &s2
print " s & s2 :",sadd
# 합집합
ssub = s | s2
print " s | s2 :",ssub


#접근

for i in "abcedf" :
    print i," : ", s[i]
    
print " s element ", [ x for x in s.elements()]
#counter update하기

s.update("abcd")
print s

