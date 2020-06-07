# -*- coding: utf-8 -*-
"""
Created on Thu Mar 03 15:46:28 2016

@author: 06411
"""



class A(object) :
    def __init__(self,name) :
        self.name = name
        
a = A('dahl')
print a.name


print(type.mro(A))
print(type(a),type(a).mro())


def int2binary(n, nbits=32) :
    if n <0 :
        return [1 if bit==0 else 0 for bit in int2binary(-n-1,nbits)]
        
    bits = [0]* nbits
    for i in range(nbits) :
        n, bits[i] = divmod(n,2)
        
    if n : 
        raise OverflowError
    return bits
    
print int2binary(1)
print [1 if bit==0 else 0 for bit in int2binary(-1)  ]

class L(list) :
    def __init(self) :
        self = []
        
l = L()
l.append(1)
print l

        