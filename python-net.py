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
iter_num = 0
while (len(mlist) > 0 and iter_num < 10) :
	i = 0;
	newlink = mlist[random.randint(0, len(mlist) - 1)].attrs["href"]
#	newlink = mlist[round((len(mlist) - 1)/2)].attrs["href"]
	print(newlink)
	iter_num = iter_num + 1
	mlist = getlinks(newlink)

