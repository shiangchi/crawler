#-*- coding:utf-8 -*-

import sys
import os
import requests
from bs4 import BeautifulSoup
def getSearch(url):

	res = requests.get(url)
	soup = BeautifulSoup(res.text, "lxml") #fixed
	dir_name = sys.argv[1]
	if not os.path.exists(dir_name):
		os.mkdir(dir_name)
	addr=''
	try:
		searcharticle = soup.find("div" , {"class" : "river"})
		for i in searcharticle.select('h3'):
			addr +='http://www.zdnet.com'+i.a['href']+'\n'
			#print (i.a['href'])
		fileout = open("silicon"+'_url.txt','w',encoding='utf-8')
		fileout.write(addr)
		fileout.close()

	except:
		print("can't find")
getSearch("http://www.zdnet.com/search/?q="+sys.argv[1])




