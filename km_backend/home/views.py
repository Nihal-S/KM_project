from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import codecs
import os
from django.http import HttpResponse
def getdata():
    url = "https://simple.wikipedia.org/wiki/Apple_Inc."
    rPage = requests.get(url)
    soup = BeautifulSoup(rPage.content, "html.parser")
    tables = soup.find("div", {"class": "mw-parser-output"})
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
    return tables.prettify()

def get_economy():
    url = "https://www.investopedia.com/news/apple-now-bigger-these-5-things/"
    rPage = requests.get(url)
    soup = BeautifulSoup(rPage.content, "html.parser")
    soup = soup.find("div", {"class": "comp article-body-content mntl-sc-page mntl-block"})
    for iframe in soup.find_all("iframe"):
        iframe.decompose()
    return soup

def home(request):
    return render(request,'home.html',{'data': str(getdata()),"economy" : get_economy()},content_type="text/html")
    # return HttpResponse(getdata())