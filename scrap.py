# this code written in beautifulsoup python3.5
# fetch one wikitable in html format with links from wikipedia
from bs4 import BeautifulSoup
import requests
import codecs
import os

url = "https://en.wikipedia.org/wiki/Timeline_of_Apple_Inc._products"

fullTable = '<table class="wikitable">'

rPage = requests.get(url)
soup = BeautifulSoup(rPage.content, "lxml")

tables = soup.find_all("table", {"class": "wikitable"})
# print(tables)
for table in tables:
    rows = table.findAll("tr")
    row_lengths = [len(r.findAll(['th', 'td'])) for r in rows]
    ncols = max(row_lengths)
    nrows = len(rows)

# rows and cols convert list of list
    for i in range(len(rows)):
        rows[i]=rows[i].findAll(['th', 'td'])

# print(rows)

# Header - colspan check in Header
    for i in range(len(rows[0])):
        col = rows[0][i]
        if (col.get('colspan')):
            cSpanLen = int(col.get('colspan'))
            del col['colspan']
            for k in range(1, cSpanLen):
                rows[0].insert(i,col)

# print(rows)

# rowspan check in full table
    for i in range(len(rows)):
        row = rows[i]
        for j in range(len(row)):
            col = row[j]
            del col['style']
            if (col.get('rowspan')):
                rSpanLen = int(col.get('rowspan'))
                del col['rowspan']
                for k in range(1, rSpanLen):
                    rows[i+k].insert(j,col)


# create table again
    for i in range(len(rows)):
        row = rows[i]
        fullTable += '<tr>'
        for j in range(len(row)):
            col = row[j]
            rowStr=str(col)
            fullTable += rowStr
        fullTable += '</tr>'

    fullTable += '</table>'

# table links changed
    fullTable = fullTable.replace('/wiki/', "https://en.wikipedia.org/wiki/")
    fullTable = fullTable.replace('\n', '')
    fullTable = fullTable.replace('<br/>', '')

# save file as a name of url
    page=os.path.split(url)[1]
    fname='outuput_{}.html'.format(page)
    singleTable = codecs.open(fname, 'w', 'utf-8')
    # singleTable.write(fullTable)
    # print(fullTable)



# here we can start scraping in this table there rowspan and colspan table changed to simple table
    soupTable = BeautifulSoup(fullTable, "lxml")
    urlLinks = soupTable.findAll('a')
    print(urlLinks)
