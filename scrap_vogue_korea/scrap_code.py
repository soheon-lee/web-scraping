from bs4 import BeautifulSoup
import requests
import re
import csv
csv_filename = "vogue_fashion.csv"
csv_open = open(csv_filename, "w+", encoding='utf-8')
csv_writer = csv.writer(csv_open)
csv_writer.writerow( ('title','image_url' ) )
crawling_url = "http://www.vogue.co.kr/category/fashion/page/1"
response = requests.get(crawling_url)


#print("response.html=", end =""), print(response.text)  
bs = BeautifulSoup(response.text, 'html.parser' )
article_list = bs.find_all('article', {'id': re.compile('post-*')})

print(article_list)
print("article_list=",end=""), print(article_list)
for article in article_list:    
    h2_title = article.find_all('h2')
    #print("h2_title=", end=""), print(h2_title)
    real_title = h2_title[0].text
    print("real h2 = ",end=""), print(real_title)
    img = article.find('img')
    #print("type img=",end=""),print(type(img))
    image_url = img['src']
    print(image_url)
    csv_writer.writerow( (real_title, image_url) )
csv_open.close()
