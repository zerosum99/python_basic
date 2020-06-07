# -*- coding: utf-8 -*-
"""
Created on Wed Mar 02 10:27:43 2016

@author: 06411
"""

import sys
reload(sys)
sys.setdefaultencoding('utf-8')



s = 'abc'
su = s.encode('ascii')
print type(su),su
sus = su.decode('utf-8')
print type(sus), sus
u = u'abc'
print type(u)
us = u.encode('utf-8')
print type(us)
usu = us.decode('utf-8')
print type(usu)


sa = 'abc'
aa = sa.encode('ascii')
print type(aa), aa
aas = aa.decode('utf-8')
print type(aas), aas
aass = aas.encode('utf-8')
print type(aass), aass


b = b'abc'
s = str(b)
print type(b), b, type(s), s

bb = bytes(b)
print type(bb),bb

sh = '한글'
shu = unicode(sh)
print type(shu), shu
print type(sh.decode('utf-8'))
print type(sh.encode('utf-8'))
print type(sh.decode('utf-8').encode('utf-8'))