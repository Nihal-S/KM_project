#This will not run on online IDE 
from bs4 import BeautifulSoup
import requests
import codecs
import os

url = "https://simple.wikipedia.org/wiki/Apple_Inc."

fullTable = '<table class="wikitable">'

rPage = requests.get(url)
soup = BeautifulSoup(rPage.content, "html.parser")

tables = soup.find("div", {"class": "mw-parser-output"})
# for table in tables:
#     links = table.find_all("a")
#     for link in links:
#         if(link.has_attr("title")):
#             print("https://en.wikipedia.org"+link["href"]+";"+link["title"])

tables.table.decompose()
for span in tables.find_all("span",{'class':'mw-editsection'}):
    span.decompose()
for image in tables.find_all("img"):
    image.decompose()
soup.find('span', id="coordinates").decompose()
for a in soup.findAll('a'):
    if(a.has_attr("href")):
        a['href'] = a['href'].replace("/wiki", "https://simple.wikipedia.org/wiki")
        a['href'] = a['href'].replace("/w/", "https://simple.wikipedia.org/w/")

# print(tags)
print(tables)