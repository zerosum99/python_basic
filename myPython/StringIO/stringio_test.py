# -*- coding: utf-8 -*-
"""
Created on Wed Mar 02 08:31:40 2016

@author: 06411
"""

import StringIO



'''
This implements (nearly) all stdio methods.
    
    f = StringIO()      # ready for writing
    f = StringIO(buf)   # ready for reading
    f.close()           # explicitly release resources held
    flag = f.isatty()   # always false
    pos = f.tell()      # get current position
    f.seek(pos)         # set current position
    f.seek(pos, mode)   # mode 0: absolute; 1: relative; 2: relative to EOF
    buf = f.read()      # read until EOF
    buf = f.read(n)     # read up to n bytes
    buf = f.readline()  # read until end of line ('\n') or EOF
    list = f.readlines()# list of f.readline() results until EOF
    f.truncate([size])  # truncate file at to at most size (default: current pos)
    f.write(buf)        # write at current position
    f.writelines(list)  # for line in list: f.write(line)
    f.getvalue()        # return whole file's contents as a string

'''
# ready for writing
f = StringIO.StringIO()
# write buffer
f.write("Hello,World")
# find buffer
f.seek(0)
buf = f.read()
print(buf)
print(type(buf))
print(f.getvalue())

MESSAGE = "That man is depriving a village somewhere of a computer scientist."

file = StringIO.StringIO(MESSAGE)

print file.read()

out = StringIO.StringIO()

# Print these string values in a loop.
for i in range(0, 100):
    out.write("Value = ")
    out.write(str(i))
    out.write(" ")

# Get string and display first 20 character.
data = out.getvalue()
print(data)
print(data[0:20])

out.close()

