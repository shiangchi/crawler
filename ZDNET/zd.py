
# coding: utf-8
import sys
import os
import requests
from bs4 import BeautifulSoup

res = requests.get("http://www.zdnet.com/search/?q="+sys.argv[1])
soup = BeautifulSoup(res.text, "lxml") #fixed

addr=''
searcharticle = soup.find("div" , {"class" : "river"})
for i in searcharticle.select('h3'):
	addr +='http://www.zdnet.com'+i.a['href']+'\n'
	#print (i.a['href'])
fileout = open(sys.argv[1]+'_url.txt','w',encoding='utf-8')
fileout.write(addr)
fileout.close()

filein = open(sys.argv[1]+'_url.txt','r')
resaddr=list()
for line in open(sys.argv[1]+'_url.txt'):
	line = filein.readline()
	if "article" in line:
		line = line.strip()
		resaddr.append(line)
		print (line)
filein.close()

dir_name = sys.argv[1]
if not os.path.exists(dir_name):
	os.mkdir(dir_name)

count= 0
for i in resaddr:
	count +=1

	res = requests.get(i)

	soup = BeautifulSoup(res.text, "lxml") #fixed
	
	fileout = open( dir_name+"/"+dir_name+"_"+str(count)+".txt","w")

	title = soup.find('h1', itemprop='headline')
	#print ("Title :"+(title).text)
	fileout.write("Title :"+(title).text)
	fileout.write('\n')

	result=list()
	tagname=list()
	article =  soup.find("div" , {"class":"storyBody"})

	for i in article.find_all(['p','ul','h3'],recursive = False ) :
		tagname.append(i.name)
		result.append(i.text)
	
	if tagname[-1] == 'ul' or tagname[-2] =="h3":
		result = result[0:-2]

	elif tagname[-1] == "ul" and tagname[-2] == 'p' :
		result = result[0:-2]

	elif tagname[-1] == 'p' and tagname[-2] =='ul' and tagname[-3]=="h3":
		result = result[0:-3]  	
	
	else :
		result = result

	for j in result:
		#print (tagname)
		#print (result)
		fileout.write("".join(j).strip())
		fileout.write('\n')

fileout.close()