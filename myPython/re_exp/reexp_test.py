# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 13:41:22 2016

@author: 06411
"""

import re
match = re.search('(?P<name>.*) (?P<phone>.*)', 'John 123456')
print match.group('name') 
print match.group('phone') 

match = re.search('(.*) (.*)', 'John 123456')
print match.group(0) 
print match.group(1) 
print match.group(2)
print match.groups()

p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
print p.search('Paris in the the spring').group()
s = re.compile(r'(?P<word>\b\w+)\s+')
print s.search('Paris in the the spring').group('word')
print s.search('Paris in the the spring').groups()
#'the the'

match = re.search("[abc].+(?# writing comments)","abc")
print match.group()

match = re.match(r'(a)(?(1)b|c)', 'ab')
print match.group(1)

match = re.match(r'(a)(?(1)b|c)', 'ac')
# print match.group(1) mismatching

match =re.finditer(r'\w','http://www.hackerrank.com/')
print match
for x in match :
    print x.group()
    



