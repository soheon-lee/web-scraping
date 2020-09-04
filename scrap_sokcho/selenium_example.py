import csv
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

csv_filename = "sokcho_restaurants_and_tags.csv"
csv_open = open(csv_filename, "w+", encoding='utf-8')
csv_writer = csv.writer(csv_open)
csv_writer.writerow( ('title','tags' ) )

query_keyword = input("크롤링 키워드는?")

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://korean.visitkorea.or.kr/main/main.do")
time.sleep(4)

driver.find_element_by_id("btnSearch").click()

element = driver.find_element_by_id("inp_search")
element.send_keys(query_keyword)

driver.find_element_by_link_text("검색").click()


full_html = driver.page_source

soup = BeautifulSoup( full_html, 'html.parser' )

time.sleep(4)

print(soup)

titles = soup.select('#contents > div > div.box_leftType1 > ul > li > div.area_txt > div > a')
tags = soup.select('#contents > div > div.box_leftType1 > ul > li > div.area_txt > p.tag')

time.sleep(3)

title_list = [title.text for title in titles] # 동해바다 ..., [속초]깔끔하고....

tag_list = [tag_set.text.split('#')[1:] for tag_set in tags]
# [[강원도,속초,도루묵],[ㅅ속초숙소, 우수숙박, 인증숙박],[SRT매거진, 강원도]]
print(tag_list)

for i, title in enumerate(title_list):
#    i -> 인덱스 (0, 1, 2,....)
#    title -> 요소
    for j, tag in enumerate(tag_list[i]):
#        j -> 인덱스
#        tag -> 강원
        print(tag)
        if j == 0:
            csv_writer.writerow((title, tag))
        else:
            csv_writer.writerow(('', tag))
