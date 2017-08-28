"""
2017-08-24
try to use urlretrieve to download image
"""

from urllib.request import urlretrieve, urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://fangjia.fang.com/process/wuhan/2610296422.htm")

bsObj = BeautifulSoup(html,'lxml')
title = bsObj.find("div",{"class":"vname"}).find("a").attrs["title"]
print(title)

prince = bsObj.find("div",{"class":"village-price-info"}).attrs["span"]
print(title)

