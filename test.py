from bs4 import BeautifulSoup

f = open("out.md", "w")

soup = BeautifulSoup(open("sina2.html"))

tempList = soup.find_all("a")

for element in tempList:
    if len(element.contents)>0:
        print >> f,element.contents[0].encode("utf-8")
    if "href" in element.attrs:
        print >> f,element["href"].encode("utf-8")

f.close()