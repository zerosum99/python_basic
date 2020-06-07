# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 12:55:51 2016

@author: 06411
"""
import json

class MyObj(object):
    def __init__(self, s):
        self.s = s
    def __repr__(self):
        return '<MyObj(%s)>' % self.s
        
obj = MyObj('instance value goes here')

print 'First attempt'
try:
    print json.dumps(obj)
except TypeError, err:
    print 'ERROR:', err

def convert_to_builtin_type(obj_1):
    print 'default(', repr(obj), ')'
    # Convert objects to a dictionary of their representation
    d = { '__class__':obj.__class__.__name__, 
          '__module__':obj.__module__,
          }
    d.update(obj.__dict__)
    return d

print
print 'With default'
print json.dumps(obj, default=convert_to_builtin_type)



def dict_to_object(d):
    if '__class__' in d:
        class_name = d.pop('__class__')
        module_name = d.pop('__module__')
        module = __import__(module_name)
        #클래스 타입을 넣고
        class_ = getattr(module, class_name)
        print 'CLASS:', class_
        #클래스 아키먼트를 가져오고
        kargs = dict( (key, value) for key, value in d.items())
        print 'INSTANCE ARGS:', kargs
        #instance 생성
        inst = class_(**kargs)
    else:
        inst = d
    return inst

encoded_object = '[{"s": "instance value goes here", "__module__": "json_myobj", "__class__": "MyObj"}]'

myobj_instance = json.loads(encoded_object, object_hook=dict_to_object)
print type(myobj_instance), myobj_instance[0].__dict__


encoder = json.JSONEncoder()
data = [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]

print encoder.encode(data)
for part in encoder.iterencode(data):
    print 'PART:', part