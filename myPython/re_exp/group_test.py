# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 15:16:54 2016

@author: 06411
"""

import re
m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
print m.group(0)       # The entire match 

print m.group(1)       # The first parenthesized subgroup.

print m.group(2)       # The second parenthesized subgroup.

print m.group(3)       # The third parenthesized subgroup.

print m.group(1,2,3)   # Multiple arguments give us a tuple.

m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
print m.groups()

m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
print m.groupdict()
print m.span()


m = re.search(r'\d+','1234')
print m.end()
print m.start()
print m.span()

#Squaring numbers
def square(match):
    number = int(match.group(0))
    return str(number**2)

print re.sub(r"\d+", square, "1 2 3 4 5 6 7 8 9")


