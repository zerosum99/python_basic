# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 17:07:37 2016

@author: 06411
"""

import time

# Method.
def square1(n):
    return n ** 2

# Lambda method.
square2 = lambda n: n ** 2

print(time.time())

# Use def method.
i = 0
while i < 10000000:
    square1(i)
    i += 1

print(time.time())

# Use lambda method.
i = 0
while i < 10000000:
    square2(i)
    i += 1

print(time.time())