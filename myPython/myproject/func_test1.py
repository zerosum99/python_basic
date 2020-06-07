# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 09:53:01 2016

@author: 06411
"""

# 함수를 변수에 할당
def greet(name):
    return "hello "+name

greet_someone = greet
print greet_someone("John")


# 내부 함수 처리

def greet(name):
    def get_message():
        return "Hello "

    result = get_message()+name
    return result

print greet("Dahl")

# Outputs: Hello John

#함수를 함수의 인자로 전달
def greet(name):
   return "Hello " + name 

def call_func(func):
    other_name = "John"
    return func(other_name)  

print call_func(greet)

# Outputs: Hello John

#함수를 return 결과로 전달
def compose_greet_func():
    def get_message():
        return "Hello there!"

    return get_message

greet = compose_greet_func()
print greet()

# Outputs: Hello there!

#자유변수에 대한 스코핑
def compose_greet_func(name):
    def get_message():
        return "Hello there "+name+"!"

    return get_message

greet = compose_greet_func("John")
print greet()

#함수 컴포지트
def get_text(name):
   return "Hello {0} !!!".format(name)


def p_decorate(func):
   def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
   return func_wrapper

my_get_text = p_decorate(get_text)

print my_get_text("Dahl")



def p_decorate(func):
   def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
   return func_wrapper

@p_decorate
def get_text(name):
   return "lorem ipsum, {0} dolor sit amet".format(name)

print get_text("Dahl")

# Outputs <p>lorem ipsum, John dolor sit amet</p>
# <p>Outputs lorem ipsum, John dolor sit amet</p>

def tags(tag_name):
    def tags_decorator(func):
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator

@tags("p")
def get_text(name):
    return "Hello "+name
    
#tags("p")
#tags_decorator(get_text)
#func_wrapper("Dahl")
print get_text("Dahl")

# Outputs <p>Hello John</p>

