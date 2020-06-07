# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

x = [1,2,3]
for i in x :
    print(i)
    
print("Hello World")
print "2 + 2 is", 2 + 2
print "3 * 4 is", 3 * 4
print "100 - 1 is", 100 - 1
print "(33 + 2) / 5 + 11.5 is", (33 + 2) / 5 + 11.5

print "First Grade"
print "1 + 1 =", 1 + 1
print "2 + 4 =", 2 + 4
print "5 - 2 =", 5 - 2
print
print "Third Grade"
print "243 - 23 =", 243 - 23
print "12 * 4 =", 12 * 4
print "12 / 3 =", 12 / 3
print "13 / 3 =", 13 / 3, "R", 13 % 3
print
print "Junior High"
print "123.56 - 62.12 =", 123.56 - 62.12
print "(4 + 3) * 2 =", (4 + 3) * 2
print "4 + 3 * 2 =", 4 + 3 * 2
print "3 ** 2 =", 3 ** 2
print

print "Halt!"
user_reply = raw_input("Who goes there? ")
print "You may pass,", user_reply

print "This" + " " + "is" + " joined."
print "Ha, " * 5
print "Ha, " * 5 + "ha!"

print "Input a rate and a distance"
rate = input("Rate: ")
distance = input("Distance: ")
print "Time:", (distance / rate)