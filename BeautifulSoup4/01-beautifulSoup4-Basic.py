
import urllib.request
request_url = urllib.request.urlopen('https://www.shajgoj.com/')
print(request_url.read())

from bs4 import BeautifulSoup
soup = BeautifulSoup(request_url.read())
print(soup.h5)
