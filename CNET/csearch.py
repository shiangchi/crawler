#-*- coding:utf-8 -*-

import sys
import os
import requests
from bs4 import BeautifulSoup
def getSearch(url):

	res = requests.get(url)
	soup = BeautifulSoup(res.text, "lxml") #fixed
	dir_name = "silicon"
	if not os.path.exists(dir_name):
		os.mkdir(dir_name)
	addr=''
	try:
		searcharticle = soup.find("section" , {"class" : "items"})
		for i in searcharticle.select('section'):
			addr +='https://www.cnet.com'+i.a['href']+'\n'
			#print (i.a['href'])
		fileout = open("try"+'_url.txt','w',encoding='utf-8')
		fileout.write(addr)
		fileout.close()

	except:
		print("can't find")
getSearch("https://www.cnet.com/search/?query="+"silicon")




