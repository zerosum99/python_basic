# -*- coding: utf-8 -*-
"""
Created on Tue Dec 01 12:38:17 2015

@author: 06411
"""


import add 
import sys

import account.account


print('import add.py')
print(add.add(5,5))

a = account.account.account()
a.print_A()

while True:
    
    s = raw_input('Enter something : ')
    if s == 'quit':
        break
    print 'Length of the string is', len(s)
    print 'string ', s
    
print 'Done'


while True:
  # output to stdout:
  print "Yet another iteration ..."
  try:
    # reading from sys.stdin (stop with Ctrl-D):
    number = raw_input("Enter a number: ")
  except EOFError:
    print "\nciao"
    break
  else:
    number = int(number)
    if number == 0:
      print >> sys.stderr, "0 has no inverse"
    else:
      print "inverse of %d is %f" % (number, 1.0/number) 


