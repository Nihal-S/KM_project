import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Disk_II"
rPage = requests.get(url)
soup = BeautifulSoup(rPage.content, "html.parser")
tables = soup.find("div", {"class": "mw-parser-output"})
tables.table.decompose()
for span in tables.find_all("span",{'class':'mw-editsection'}):
    span.decompose()
for image in tables.find_all("img"):
    image.decompose()
# soup.find('span', id="coordinates").decompose()
for a in soup.findAll('a'):
    if(a.has_attr("href")):
        a['href'] = a['href'].replace("/wiki", "https://simple.wikipedia.org/wiki")
        a['href'] = a['href'].replace("/w/", "https://simple.wikipedia.org/w/")
print(tables.prettify())