import urllib.request
from urllib.error import URLError
from urllib.error import HTTPError

# try:
#     response = urllib.request.urlopen('https://www.shajgoj.com/')
# except HTTPError as http_error:
#     print(http_error)
# else:
#     print("fine worked")

try:
    html = urllib.request.urlopen("https://www.shajgoj.com/")
except HTTPError as e:
    print(e)
except URLError as e:
    print("Server Not Found")
else:
    print("Its worked")

