"""
2017-08-21 20:35 
Get the link of website again and again.
Abandon the same link.
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError
import datetime
import random
import re

random.seed(datetime.datetime.now())

def getlinks(articleUrl):
	html = urlopen(articleUrl)
	bsObj = BeautifulSoup(html.read(),'lxml')
	linklist = bsObj.findAll("a"or"link", href=re.compile("(http\:\/\/)+"))
	return linklist
	
mlist = getlinks("http://nanjing.fang.com/")
page = set()
iter_num = 0
while (len(mlist) > 1 and iter_num < 10) :
#	newlink = mlist[random.randint(0, len(mlist) - 1)].attrs["href"]
	for link in mlist:
		if link.attrs["href"] not in page:
			page.add(link.attrs["href"])
	iter_num = iter_num + 1
	mlist = getlinks(mlist[1].attrs["href"])
print(page)

