"""
2017-08-21
learn api (token)
learn json - 1
"""

import json
from urllib.request import urlopen

def getIpInfo(ip):
	html = urlopen("http://freegeoip.net/json/"+ip).read().decode("utf-8")
	result_json = json.loads(html)
	return result_json

print(getIpInfo(""))
