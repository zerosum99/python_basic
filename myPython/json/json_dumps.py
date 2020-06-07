# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 10:45:25 2016

@author: 06411
"""

import json

#python --> json encoding
obj_pd = {u"answer": [42.2], u"abs": 42}
obj_jd = json.dumps(obj_pd)
print("encoding ",type(obj_jd), obj_jd)

#intent를 주어 보기좋게 하기
obj = {u"answer": [42.2], u"abs": 42}
print(repr(json.dumps(obj, indent=4)))
print(json.dumps(obj, indent=4))

class User(object):
    def __init__(self, name, password):
        self.name = name
        self.password = password
alice = User('Alice A. Adams', 'secret')

def jdefault(o):
    return o.__dict__
print(json.dumps(alice, default=jdefault))
# outputs: {"password": "secret", "name": "Alice A. Adams"}

def jdefault_set(o):
    if isinstance(o, set):
        return list(o)
    return o.__dict__

pets = set([u'Tiger', u'Panther', u'Toad'])
pets_js = json.dumps(pets, default=jdefault_set)
print( type(pets_js),json.dumps(pets, default=jdefault_set))
# outputs: ["Tiger", "Panther", "Toad"]

#json  --> python decoding
obj_jl = u'{"answer": [42.2], "abs": 42}'
obj_pl = json.loads(obj_jl)
print("decoding",type(obj_pl),obj_pl)

from json import JSONDecoder
jd = JSONDecoder()
jd_p = jd.decode("""{ "a":"b" }""")

print(type(jd_p),jd.decode("""{ "a":"b" }"""))
print(type(json.loads("""{ "a":"b" }""")), json.loads("""{ "a":"b" }"""))
#{u'a': u'b'}


data = [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]
print 'DATA:', type(data), data
print 'DATA repr:', type(repr(data)), repr(data)
data_string = json.dumps(data)
print 'JSON:', data_string
data_l = json.loads(data_string)
print "Data ",json.loads(data_string)
print( data == data_l)

data = [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]
print 'DATA:', repr(data)

unsorted = json.dumps(data)
print 'JSON:', json.dumps(data)
print 'SORT:', json.dumps(data, sort_keys=True)

first = json.dumps(data, sort_keys=True)
second = json.dumps(data, sort_keys=True)

print 'UNSORTED MATCH:', unsorted == first
print 'SORTED MATCH  :', first == second


data = [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]
print 'DATA:', repr(data)
print 'repr(data)             :', repr(data)
print 'dumps(data)            :', json.dumps(data), len(json.dumps(data))
print 'dumps(data, separators):', json.dumps(data, separators=(',',':')),len(json.dumps(data, separators=(',',':')))