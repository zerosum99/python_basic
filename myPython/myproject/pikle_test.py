# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 12:48:04 2016

@author: 06411
"""

import pickle

# 객체 저장장소 이름 정의
shoplistfile = 'shoplist.data'
#저장대상 객체 생성
shoplist = ['apple', 'mango', 'carrot']

print " shoplist file", type(shoplistfile)

# 객체 저장장소 파일로 생성
f = open(shoplistfile, 'wb')

print f
print type(f)

#파일저장소에 저장
pickle.dump(shoplist, f)
f.close()

# 객체 삭제
del shoplist

# 객제 저장 파일 읽기
f = open(shoplistfile, 'rb')

# 저장된 파일을 로드
storedlist = pickle.load(f)

print storedlist