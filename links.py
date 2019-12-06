import json
import requests
from bs4 import BeautifulSoup
import re 
from os.path import join
from urllib.parse import urljoin

import sys

URL=sys.argv[1]



   #input("Enter a URL :")#"https://www.geeksforgeeks.org/data-structures/"
r = requests.get(URL) 

soup = BeautifulSoup(r.content, 'html5lib') 
#print(soup.prettify()) 

ls=[]
for link in soup.find_all('a', href=True): 
	ls.append(urljoin(URL,link['href']))

#print(ls)
website={}
website["site"]=URL

website["links"]=ls
#print(website)
jsonfile=json.dumps(website)
print(jsonfile)