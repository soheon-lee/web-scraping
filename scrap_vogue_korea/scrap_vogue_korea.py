from bs4 import BeautifulSoup

import requests
import re
import csv

crawling_url = "https://www.vogue.co.kr/category/fashion/page/1"
response = requests.get(crawling_url)


print("NOW response.html=", end = ""), print(response.text)

req = requests.get(crawling_url)
html = req.text
bs = BeautifulSoup(response.text, 'html.parser' )
print(bs)
category_list = bs.select('#main > div > div > ul > li > a')

for word in category_list:
    print(word.text)
