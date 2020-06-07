# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 14:15:11 2016

@author: 06411
"""

import json
#import tempfile

data = [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]

#f = tempfile.NamedTemporaryFile(mode='w')
f = open("file_txt",'w+')
json.dump(data, f)
f.flush()

print open(f.name, 'r').read()
f.close()

f = open("file_txt1",'w+')
f.write('[{"a": "A", "c": 3.0, "b": [2, 4]}]')
f.flush()
f.seek(0)

print json.load(f)
f.close()

print type(json.dumps({'a':u'b'}, ensure_ascii=True)) # <type 'str'>
print json.dumps({'a':u'b'}, ensure_ascii=True)
print type(json.dumps({'a':'b'}, ensure_ascii=False)) # <type 'str'>
print json.dumps({'a':'b'}, ensure_ascii=False)
print type(json.dumps({'a':u'b'}, ensure_ascii=False)) #<type 'unicode'>
print json.dumps({'a':u'b'}, ensure_ascii=False)


def ascii_encode_dict(data):
    ascii_encode = lambda x: x.encode('ascii')
    return dict(map(ascii_encode, pair) for pair in data.items())
json_data = '{"foo": "bar", "bar": "baz"}'
print json.loads(json_data)  #old call gives unicode
#{u'foo': u'bar', u'bar': u'baz'}
print json.loads(json_data, object_hook=ascii_encode_dict) # new call gives str
#{'foo': 'bar', 'bar': 'baz'

print json.dumps([u'\xd0\xb2', u'\xd0\xb2'], ensure_ascii=False)
print json.dumps([u'\xd0\xb2', u'\xd0\xb2'], ensure_ascii=False)
                