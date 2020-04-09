from bs4 import BeautifulSoup

with open('out.html') as raw_resuls:
    results = BeautifulSoup(raw_resuls, 'lxml')

for element in results.find_all("a"):
        print(element['href'][1:-1])
        # print(";" +element["title"])