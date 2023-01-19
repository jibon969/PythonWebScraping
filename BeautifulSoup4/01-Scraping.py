
"""
Resources urls : https://www.freecodecamp.org/news/web-scraping-python-tutorial-how-to-scrape-data-from-a-website/
8:42 PM 1/18/2023
"""
import csv

import requests
from bs4 import BeautifulSoup


# 1. Loading Web Pages with 'request'
# res = requests.get('https://www.shajgoj.com/')
# print(res.text)
# print(res.status_code)


# 2. Extracting title with BeautifulSoup

# Make a request to https://www.google.com/
# page = requests.get("https://www.google.com/")
# soup = BeautifulSoup(page.content, 'html.parser')
#
# # Extract title of page
# page_title = soup.title.text
#
# # print the result
# print(page_title)


# 3. Soup-ed body and head

# # Make a request
# page = requests.get("https://www.google.com")
# soup = BeautifulSoup(page.content, 'html.parser')
#
#
# # Extract title of page
# page_title = soup.title.text    # with tag
# # page_title = soup.title.text    # without tag
# print("Page title ========== \n\n", page_title)
#
# # Extract head of page
# page_head = soup.head
# print("Page Head ========== \n\n", page_head)
#
#
# # Extract body of page
# page_body = soup.body
# print("Page Body ========== \n\n", page_body)


# 4. select with BeautifulSoup

# Make a request
# page = requests.get("https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
# soup = BeautifulSoup(page.content, 'html.parser')
# print("select with BeautifulSoup : ======= \n")
#
# # Create all_h1_tags as empty list
# all_h1_tags = []
#
# # Set all_h1_tags to all h1 tags of the soup
# for element in soup.select('h1'):
#     all_h1_tags.append(element.text)
#
# print("h1 tag ======= : ", all_h1_tags)
#
#
# # Create seventh_p_text and set it to 7th p element text of the page
# seventh_p_text = soup.select('p')[6].text
# print("seventh_p_text : ", seventh_p_text)


# 5. Top items being scraped right no

# Make a request
# page = requests.get("https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
# soup = BeautifulSoup(page.content, 'html.parser')
#
# # Create top_items as empty list
# top_items = []
#
# # Extract and store in top_items according to instructions on the left
# products = soup.select('div.thumbnail')
# for elem in products:
#     title = elem.select('h4 > a.title')[0].text
#     review_label = elem.select('div.ratings')[0].text
#     info = {
#         "title": title.strip(),
#         "review": review_label.strip()
#     }
#     top_items.append(info)
#
# print(top_items)


# 6. Extracting Links

# Make a request
# page = requests.get("https://shop.shajgoj.com/")
# soup = BeautifulSoup(page.content, 'html.parser')
#
# # Create top_items as empty list
# image_data = []
#
# # Extract and store in top_items according to instructions on the left
# images = soup.select('img')
# for image in images:
#     src = image.get('src')
#     alt = image.get('alt')
#     image_data.append({"src": src, "alt": alt})
#
# print(image_data)


# Make a request
# page = requests.get("https://shop.shajgoj.com/")
# soup = BeautifulSoup(page.content, 'html.parser')
#
# # Create top_items as empty list
# all_links = []
#
# # Extract and store in top_items according to instructions on the left
# links = soup.select('a')
# for ahref in links:
#     text = ahref.text
#     text = text.strip() if text is not None else ''
#
#     href = ahref.get('href')
#     href = href.strip() if href is not None else ''
#     all_links.append({"href": href, "text": text})
#
# print(all_links)


# Make a request

import requests
from bs4 import BeautifulSoup
import csv
# Make a request
page = requests.get("https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')

# Create top_items as empty list
all_products = []

# Extract and store in top_items according to instructions on the left
products = soup.select('div.thumbnail')
for product in products:
    name = product.select('h4 > a')[0].text.strip()
    description = product.select('p.description')[0].text.strip()
    price = product.select('h4.price')[0].text.strip()
    reviews = product.select('div.ratings')[0].text.strip()
    image = product.select('img')[0].get('src')

    all_products.append({
        "name": name,
        "description": description,
        "price": price,
        "reviews": reviews,
        "image": image
    })


keys = all_products[0].keys()

with open('products.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(all_products)