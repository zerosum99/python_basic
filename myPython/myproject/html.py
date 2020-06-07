# -*- coding: utf-8 -*-
"""
Created on Mon Dec 07 16:37:42 2015

@author: 06411
"""
import urllib
import re

racingGirlUrl = 'http://gall.dcinside.com/list.php?id=racinggirl&no='

fileNo = 0
for no in range(170710, 170720):
    url = racingGirlUrl + str(no)
    f = urllib.urlopen(url)
    html = f.read()
    imageUrlList = re.findall("http://image.dcinside.com/download.php[^']+", html)
    for url in imageUrlList:
         contents = urllib.urlopen(url).read()
         file(str(fileNo)+'.jpg', 'w').write(contents)
         fileNo = fileNo + 1
         