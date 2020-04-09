#This will not run on online IDE 
from bs4 import BeautifulSoup
import requests
import codecs
import os

url = "https://en.wikipedia.org/wiki/Timeline_of_Apple_Inc._products"

fullTable = '<table class="wikitable">'

rPage = requests.get(url)
soup = BeautifulSoup(rPage.content, "lxml")

tables = soup.find_all("table", {"class": "wikitable"})
for table in tables:
    links = table.find_all("a")
    for link in links:
        if(link.has_attr("title")):
            print("https://en.wikipedia.org"+link["href"]+";"+link["title"])