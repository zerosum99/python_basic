# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 14:31:18 2016

@author: 06411
"""

def generate_power_func(n):
    print "id(n): %X" % id(n)
    print ' outer ', locals()
    out_v = 10.0
    def nth_power(x):
        print ' inner ', locals()
        #n = x
        #return x**n
        v = x**n + out_v
       # n = v + n   #UnboundLocalError: local variable 'n' referenced before assignment
        return v
    print "id(nth_power): %X" % id(nth_power)
    return nth_power
    

clo = generate_power_func(4)

print clo(5)

print clo.__closure__
print clo.__closure__[0]
print type(clo.__closure__[0])
print clo.__closure__[0].cell_contents
print clo.__closure__[1]
print clo.__closure__[1].cell_contents



funcs = []
for i in range(4):
    def f():
        print i
    # 함수 인스턴스를 추가
    funcs.append(f)
    
print funcs
i =0
for f in funcs:
    i += 1
    print id(f), f()
    