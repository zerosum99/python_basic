# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 08:38:36 2016

@author: 06411
"""

import pytz
import datetime

dt = datetime.datetime.now()
print dt

# datetime class UTC 타임산출
utc_dt = datetime.datetime(2002, 10, 27, 6, 0, 0, tzinfo=pytz.utc)
print " utc datetime ", utc_dt
#datetime.now() 메소드 utc 타임 산출
utc_dt2 = datetime.datetime.now(tz=pytz.utc)
print " utc datetime  ", utc_dt2



# local time 구하기
# 서울 date time 구하기
seoul_tz = pytz.timezone('Asia/Seoul')
print " seoul time zone ",seoul_tz
seoul_dt = seoul_tz.localize(datetime.datetime.now())
print " seoul datetime ", seoul_dt

# 평양 date time으로  구하기
pyongyang_tz = pytz.timezone('Asia/Pyongyang')
print " pyongyang time zone ", pyongyang_tz
pyongyang_dt = pyongyang_tz.localize(datetime.datetime.now())

print " pyongyang datetime ", pyongyang_dt

before = pyongyang_tz.normalize(pyongyang_dt - datetime.timedelta(minutes=30))
print " 실제 평양 시간 조정 ", before
# 평양 date time를 UTC로 구하기
after = pyongyang_tz.normalize(datetime.datetime.now(tz=pytz.utc))
print " 실제 평양시간 조정", after
after2 = pyongyang_tz.localize(datetime.datetime.now())
print " 실제 평양시간 조정", after2

tz = pytz.timezone('America/St_Johns')

st_johns_dt = tz.normalize(datetime.datetime.now(tz=pytz.utc))
print " ameria / st_johns ", st_johns_dt

print " utc offset ",st_johns_dt.utcoffset()
st_tmdt = st_johns_dt.utcoffset()
print int(st_tmdt.total_seconds()/3600) 
print int((st_tmdt.total_seconds()%3600)/60) 

print " total second ", st_tmdt.total_seconds()

print " dst        ",st_johns_dt.dst()


