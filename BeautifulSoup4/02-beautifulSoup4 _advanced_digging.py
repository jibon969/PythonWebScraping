import urllib.request
from bs4 import BeautifulSoup

html = urllib.request.urlopen('https://www.shajgoj.com/')
soup = BeautifulSoup(html.read())
print(soup.h4)