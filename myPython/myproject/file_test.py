# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 09:47:43 2016

@author: 06411
"""

f = open("newfile.txt", 'w') 

for i in range(1, 11): 
    # 파일 라인에 출력
    line = "%d 번째 줄입니다.\n" % i 
    f.write(line) 

f.close()


f = open("newfile.txt", 'r') 
line = f.readline() 
print(line)
f.close()

f = open("newfile.txt", 'r')

while True: 
    line = f.readline()
    if not line: break 
    print(line)

f.close()

f = open("newfile.txt", 'r') 
lines = f.readlines()

for line in lines: 
    print(line)

f.close()


f = open("newfile.txt", 'r') 
data = f.read()

print(data) 

f.close()

f = open("newfile.txt",'a')

for i in range(11, 21): 
    data = "%d번째 줄입니다.\n" % i 
    f.write(data) 

f.close()