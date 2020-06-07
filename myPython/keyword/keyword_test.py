# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 08:42:54 2016

@author: 06411
"""

from __future__ import print_function
 
import keyword

print (1,2,3)
print (keyword)

print (keyword.kwlist)

print(keyword.iskeyword('add'))

print (keyword.main)
print (vars(keyword.main))

print(print.__name__)

#print keyword.main.func_name
#print keyword.main.func_code.co_code
import __future__
print("    ",__future__)
print("__import__          :",__import__('__future__'))
print("__future__.__file__ :",__future__.__file__)
print("__future__.__doc__  :",__future__.__doc__)


def add(x=1,y=1) :
    """ add x, y """
    print(" vars   : ",vars())
    print(" locals : ", locals())
    return x + y
    
add(5,5)

print("func __name__ : ",add.__name__)
print("func name     : ",add.func_name)
print("func __doc__  : ",add.func_doc)
print("func_default  : ",add.func_defaults)



print(" function code ")
print(add.func_code)
print(" source code convert ")
print(add.func_code.co_code)
code_c = add.func_code.co_code
print(type(code_c))
#print(code_c.decode("euc-kr"))

code_str = '''
def add(x=1,y=1) :
   """ add x, y """
   print(" vars   : ",vars())
   print(" locals : ", locals())

   return x + y
   
a = add(5,5)
print(a)
'''
code_obj = compile(code_str, '<string>', 'exec')
print(type(code_obj))
exec(code_obj)
print(dir(code_obj))

def add1(x=1,y=1) :
    """ add1 x, y """
    print(" vars   : ",vars())
    print(" locals : ", locals())
    return x + y
print(" ============================= ")
print(" add1 code type ")
print(add1.func_code.co_name)
print(add1.func_code.co_filename)
print(add1.func_code.co_argcount)
print(add1.func_code.co_code)
import dis
dis.dis(add1.func_code.co_code)
import inspect
print(inspect.getsource(add1))
print(" ============================= ")
print(add1.func_code.co_varnames)
print(add1.func_code.co_nlocals)
print(add1.func_code.co_names)
print(add1.func_code.co_lnotab)
print(add1.func_code.co_consts)

x=(1,2)
x.__init__([3,4])
print(x)

y=[1,2]
y.__init__([3,4])
print(y)

z=0
p = z.__new__(int,5)
print(p)
print(z)

pp = int.__new__(int,0)
print("data type", type(pp))
print(pp)

ss = list.__new__(list,[])
print("data type", type(ss))
ss.__init__([1,2,3])
print(ss)

class S(object) :
    pass
    
print("S type ",S)

clss = object.__new__(S)
clss.__init__()
print(type(clss), isinstance(clss,S))