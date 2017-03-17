import requests,os
from bs4 import BeautifulSoup

request1 = requests.get("https://www.<sitename>.com")
request1_content = request1.content
soup1 = BeautifulSoup(request1_content)
for url1 in soup1.find_all(href=True):
    print "url : ", url1['href']
