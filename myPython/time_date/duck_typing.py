# -*- coding: utf-8 -*-
"""
Created on Fri Feb 05 13:43:03 2016

@author: 06411
"""

class Duck:
    def quack(self):
        print("Quaaaaaack!")
    def feathers(self):
        print("The duck has white and gray feathers.")

class Person:
    def quack(self):
        print("The person imitates a duck.")
    def feathers(self):
        print("The person takes a feather from the ground and shows it.")
    def name(self):
        print("John Smith")

def in_the_forest(duck):
    duck.quack()
    duck.feathers()
    
class InTheForest() :
    @staticmethod
    def quack(self) :
        self.quack()
    @staticmethod
    def feathers(self) :
        self.feathers()
    @classmethod
    def all(cls,self) :
        cls.quack(self)
        cls.feathers(self)
        

def game():
    donald = Duck()
    john = Person()
    in_the_forest(donald)
    in_the_forest(john)
    
def gameC():
    donald = Duck()
    john = Person()
    InTheForest.all(donald)
    InTheForest.all(john)

print "function duck typeing "
game()

print " class duck typeing "
gameC()
