# -*- coding: utf-8 -*-
"""
Created on Thu Feb 04 09:40:44 2016

@author: 06411
"""

from datetime import tzinfo, timedelta, datetime
from pytz import UTC

#타입존의 subclass로 정의
class MyUTCOffsetTimezone (tzinfo):

    def __init__(self, offset=19800, name=None):
        self.offset = timedelta(seconds=offset)
        self.name = name or self.__class__.__name__

    def utcoffset(self, dt):
        return self.offset

    def tzname(self, dt):
        return self.name

    def dst(self, dt):
        return timedelta(0)

#타임존을 처리하기 위한 클래스 선언
now = datetime.now(tz=UTC)
print now
# -> 2015-01-28 10:46:42.256841+00:00
#실제 타입존에 인스턴스 할당
print now.astimezone(MyUTCOffsetTimezone())
# -> 2015-01-28 16:16:42.256841+05:30
print datetime.now(MyUTCOffsetTimezone())
# -> 2015-01-28 16:16:42.256915+05:30