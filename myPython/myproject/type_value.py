# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 11:51:24 2015

@author: 06411
"""




def typeof(obj) :
    return obj.__class__
    
def valueof(obj) :
    
       
    if obj.__class__ == type(obj) :
        
        
        print(eval(obj.__class__.__name__  + '(obj)'))
      
        return eval(obj.__class__.__name__  + '(obj)')
        

print(typeof(1))
print(valueof(1))

print(typeof(1.1))
print(valueof(1.1))

print(typeof([1,2]))
print(valueof([1,2]))

data = """
park a00905-1049118
kim  700905-1059119
"""

result = []
for line in data.split("\n"):
    word_result = []
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))

import re 



pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))