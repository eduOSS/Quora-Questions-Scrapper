#!/usr/bin/python
from bs4 import BeautifulSoup
import requests
import sys, urllib, re
import webbrowser
session = requests.session()
print "Enter what topics questions you want to search on Quora"
topic=raw_input()
url="http://www.quora.com/"+topic+"/rss"
#req = session.get('http://www.quora.com/Big-Data/rss')
req = session.get(url)
doc = BeautifulSoup(req.content)

print doc.title
abc = doc.findAll('body')
#abc = doc.findAll('span',{ "base" : "http://www.quora.com/Big-Data/rss" })

#print abc
print len(abc)
a=0
total = abc[0].text
#print total
test = re.findall(r"([^.]*?span[^.]*\.)",total)
for i in range(0,len(test)):
        #test[i].replace("*-*"," ")
        #print test[i]
        one = re.compile('com/(.*?)<div').findall(test[i])
        str1 = ''.join(one)
        str2 = str1.replace("-"," ")
        print i," ",str2,"\n"

        #print i," ",test[i],"\n"
#print re.findall(r"(u'com(.?)<div>)",total)
print "\n Enter Question no you want me to search"
quest=int(raw_input())
q = re.compile('com/(.*?)<div').findall(test[quest])
str1=''.join(q)
url="http://www.quora.com/"+str1
new =2
webbrowser.open(url,new=new)
