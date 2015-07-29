import time
from bs4 import BeautifulSoup
from urllib import urlopen

page = urlopen('http://www.reddit.com/r/liberta/')
soup = BeautifulSoup(page.read(), "html.parser")
pnum = soup.find_all('span',class_='number')
pf = unicode(pnum[1])
hf = pf.split("~",1)[1]
f = str(hf.split("<",1)[0])
print(time.strftime("%d/%m/%Y %H:%M:%S"), f)
