from bs4 import BeautifulSoup
import requests
import codecs
import os

url = "https://www.investopedia.com/news/apple-now-bigger-these-5-things/"
rPage = requests.get(url)
soup = BeautifulSoup(rPage.content, "html.parser")
soup = soup.find("div", {"class": "comp article-body-content mntl-sc-page mntl-block"})
# soup.iframe.decompose()
for iframe in soup.find_all("iframe"):
    iframe.decompose()
# for span in soup.find_all("div",{'class':'comp mntl-sc-block finance-sc-block-html mntl-sc-block-html'}):
    # span.decompose()
print(soup)