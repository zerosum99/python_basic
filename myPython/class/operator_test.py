# -*- coding: utf-8 -*-
"""
Created on Wed Apr 06 09:53:58 2016

@author: 06411
"""

import operator as op

i = 10
print(" operator module ")
print(" add : ",op.add(i,1))
print(" sub : ",op.sub(i,1))
print(" mul : ",op.mul(i,10))
print(" div : ",op.div(i,10))
print(" div : ",op.floordiv(i,3))
print(" true div : ", op.truediv(i,3))
print(" mod div : ",op.mod(i,3))
print("  divmod : ", "N/A")
print(" power   : ",op.pow(i,3))

print(" special method   ")
print(" add : ",i.__add__(1))
print(" sub : ",i.__sub__(1))
print(" mul : ",i.__mul__(10))
print(" div : ",i.__div__(10))
print(" floor div : ",i.__floordiv__(3))
print(" true div : ", i.__truediv__(3))
print(" mod div : ",i.__mod__(3))
print("  divmod : ", i.__divmod__(3))
print(" power   : ", i.__pow__(3))

print(" operator   ")
print(" add : ",i + 1)
print(" sub : ",i - 1)
print(" mul : ",i * 10)
print(" div : ",i / 10)
print(" floor div : ",i // 3)
print(" true div : ", i / 3.0)
print(" mod div : ",i % 3)
print("  divmod : ", divmod(i, 3))
print(" power   : ", i ** 3 )


print(" lshift x * (2**y)  ")
print(" <<         : ", 10 << 2)
print(" lshift     : ", op.lshift(10,2))
print(" __lshift__ : ", (10).__lshift__(2))
print(" rshift x // (2**y)  ")
print(" >>         : ", 10 >> 2)
print(" rshift     : ", op.rshift(10,2))
print(" __rshift__ : ", (10).__rshift__(2))
print(" bit and ", oct(10), oct(2))
print(" &           : ", 10 & 2)
print(" and_(a, b)  : ", op.and_(10,2))
print("x.__and__(y) : ", (10).__and__(2))
print(" bit or ", oct(10), oct(4))
print(" |           : ", 10 | 4)
print(" or_(a, b)   : ", op.or_(10,4))
print("x.__or__(y)  : ", (10).__or__(4))
print(" bit xor ", oct(10), oct(6))
print(" ^            : ", 10 ^ 6)
print(" xor(a, b)    : ", op.xor(10,6))
print("x.__xor__(y)  : ", (10).__xor__(6))

print(" bit inversion ", oct(10))
print(" ~           : ", ~(10) )
print(" invert(a)   : ", op.invert(10))
print("x.__invert__(y)  : ", (10).__invert__())

print(" negative : ", -(10))
print(" neg(a)   : ", op.neg((10)))
print("a.__neg__   : ", (10).__neg__())
print(" positive : ", -(-10), +(10))
print(" pos(a)   : ", op.pos((10)))
print("a.__pos__   : ", (10).__pos__())

print(" right hand operator ")
print(" x + y ", (8).__radd__(2))
print(" x + y ", (2).__add__(8))

print(" x ** y ", (3).__rpow__(2))
print(" x ** y ", (2).__pow__(3))

x = True
y = False
print('x and y is',x and y)
print('x or y is',x or y)
print('not x is',not x)


print(" sequence operator ")
print(" +  ", "Hello" + "World")
print(" concat ", op.concat("Hello", "World"))
print(" __add__ ", "Hello".__add__("World"))
print(" *  ", "Hello" * 3)
print(" __mul__ ", "Hello".__mul__(3))
print(" repeat ", op.repeat("Hello", 3))

print(" is ", "abc" is "abc")
print(" is_", op.is_("abc","abc"))
print(" is not ", "abc" is not "abcd")
print(" is_", op.is_not("abc","abcd"))

print(" in ", "a" in "abc")
print(" __contains__", "abc".__contains__('a'))
print(" contains", op.contains("abc",'a'))

print(" in ", "a" not in "abc")
print(" __contains__", not("abc".__contains__('a')))
print(" contains", op.not_(op.contains("abc",'a')))


print(" __getslice__ :", [0,1,2,3].__getslice__(0,2))
print("  getslice    :", op.getslice([0,1,2,3],0,2))
l=[0,1,2,3]
print(" __setslice__ :", l.__setslice__(0,2,[99,99]),l)
print(" __delslice__ :", l.__delslice__(0,2),l)
l=[0,1,2,3]
print("  setslice    :", op.setslice(l,0,2,[99,99]),l)
print("  delslice    :", op.delslice(l,0,2),l)

print(" __getitem__  : ", [0,1,2,3].__getitem__(slice(0,2)))
print(" getitem      : ", op.getitem([0,1,2,3],slice(0,2)))
l=[0,1,2,3]
print(" __setitem__ :", l.__setitem__(slice(0,2),[99,99]),l)
print(" __delitem__ :", l.__delitem__(slice(0,2)),l)
l=[0,1,2,3]
print("  setitem    :", op.setitem(l,slice(0,2),[99,99]),l)
print("  delitem    :", op.delitem(l,slice(0,2)),l)