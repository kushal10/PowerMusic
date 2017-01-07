import os
import requests
import urllib2
import sys
import codecs
from bs4 import BeautifulSoup
string = ""
string = sys.argv[1]
query = string
name  = query
query += "metrolyrics"
query.replace("_","+")
url = "http://www.google.com/search?q="+query
a = requests.get(url)
b = a.content
f = open(".poppi.html","w")
f.write(b)
f.close()
soup = BeautifulSoup(b)
b  = soup.find("cite")
link = b.text
#print link
final_link = "http://"+link
a = urllib2.urlopen(final_link)
soup2 =  BeautifulSoup(a.read())
lyrics = ""
for i in soup2.findAll("p",{"class":"verse"}):
    lyrics += i.text
    lyrics += "\n"
print lyrics
name.replace(" ","_")
f = codecs.open(name+".txt",'w+', "utf-8-sig")
f.write(lyrics)
f.close()
