# -*- coding: utf-8 -*-
"""
Created on Tue Jan 05 11:32:38 2016

@author: 06411
"""

import re

line = "Cats are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?) (.*)', line, re.M|re.I)

if matchObj:
   print "matchObj.group() : ", matchObj.group()
   print "matchObj.group(1) : ", matchObj.group(1)
   print "matchObj.group(2) : ", matchObj.group(2)
   print "matchObj.group(3) : ", matchObj.group(3)
else:
   print "No match!!"
   
   
phone = "010-959-559 # This is Phone Number"

# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print "Phone Num : ", num

# Remove anything other than digits
num = re.sub(r'\D', "", phone)    
print "Phone Num : ", num


s = '<html><head><title>Title</title>'
print len(s)

print(re.match('<.*>', s).span())
print(re.match('<.*>', s).group())
print(re.match('<.*?>', s).span())
print(re.match('<.*?>', s).group())