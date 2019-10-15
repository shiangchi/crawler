
# coding: utf-8
import sys
import os
import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.cnet.com/search/?query="+sys.argv[1])
soup = BeautifulSoup(res.text, "lxml") #fixed

addr=''
searcharticle = soup.find("section" , {"class" : "items"})
for i in searcharticle.select('section'):
	addr +='https://www.cnet.com'+i.a['href']+'\n'
	#print (i.a['href'])
fileout = open(sys.argv[1]+'_url.txt','w')
fileout.write(addr)
fileout.close()

filein = open(sys.argv[1]+'_url.txt','r')
resaddr=list()
for line in open(sys.argv[1]+'_url.txt'):
	line = filein.readline()
	if "news" in line :
		line = line.strip()
		resaddr.append(line)
	elif "how-to" in line :
		line = line.strip()
		resaddr.append(line)
	elif "roadshow" in line:
		line = line.strip()
		resaddr.append(line)
	elif "products" in line :
		line = line.strip()
		resaddr.append(line)
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
	title = list() 
	for i in soup.find_all(['h1'], {"class": ["headline","speakableText"]}):
		title.append(i.text)
		if soup.find('h2', {'class':'productTitle'}):
			for j in soup.find('h2', {'class':'productTitle'}):
				title.append(j.strip())

	for i in title:
		print (str(i))
		fileout.write(str(i))
	fileout.write('\n')

	result=list()
	tagname=list()
	extraarticle = list()
	if soup.find('div' , {'class':'quickInfo'}):
		extraarticle = soup.find('div' , {'class':'quickInfo'})
		for i in extraarticle.find_all('p'):
			print (i.text)
			extraarticle.append(i.text)
			fileout.write("".join(i.text).strip())
			fileout.write('\n')
	#for j in extraarticle:
		#print (tagname)
		#print (result)
		#fileout.write("".join(j))
		#fileout.write('\n')

	article =  soup.find("div" , itemprop=["articleBody","reviewBody"])
	for i in article.find_all(['p','ul > li','h3','aside','div > div > p'],recursive = False ) :
		tagname.append(i.name)
		result.append(i.text)


	for j in result:
		#print (tagname)
		#print (result)
		fileout.write("".join(j).strip())
		fileout.write('\n')
	nextpage = soup.find("nav" , section='paginate')
	if nextpage:
		for i in nextpage.select('span'):
			nextpageurl = 'https://www.cnet.com'+i.a['href']
			res = requests.get(nextpageurl)
			soup = BeautifulSoup(res.text, "lxml")
			tagname2=list()
			extraarticle = list()
			result2=list()
			if soup.find('div' , {'class' : 'quickInfo'}):

				extraarticle = soup.find('div' , {'class' : 'quickInfo'})
				for i in extraarticle.find_all('p'):
					extraarticle.append(i)
					print (i.text)
				for j in extraarticle:

					fileout.write("".join(j).strip())
					fileout.write('\n')

			if soup.find("div" , itemprop=["articleBody","reviewBody"]):
				article2 =  soup.find("div" , itemprop=["articleBody","reviewBody"])
				for i in article2.find_all(['p','ul > li','h3','aside','div > div > p'],recursive = False ) :
					tagname2.append(i.name)
					result2.append(i.text)



			for j in result2:

				fileout.write("".join(j).strip())
				fileout.write('\n')

fileout.close()