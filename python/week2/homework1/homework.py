from bs4 import BeautifulSoup
import requests
import time
import pymongo
url_home ='http://sh.xiaozhu.com/search-duanzufang-p1-0/'
client = pymongo.MongoClient('localhost',27017)
rent_house = client['rent_house']
sheet_line = rent_house['sheet_line']


def start(end):
    end = int(end)
    for i in range(1,end+1):
        url='http://sh.xiaozhu.com/search-duanzufang-p{}-0/'.format(i)
        home_page(url)

def home_page(url,data=None):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    titles = soup.select('span.result_title')
    links = soup.select('a.resule_img_a ')
    i=1
    if data == None:
        for title,link in zip (titles,links):
            data ={
                'title' : title.get_text(),
                'link':link.get('href')
            }
            page(data['link'])
            print(i)
            i = i + 1

def page(url,data=None):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    titles = soup.select('  h4 > em')
    prices = soup.select('  div.day_l > span')
    if data == None:
        for title, price in zip(titles, prices):
            time.sleep(1)
            data={
                'title': title.get_text(),
                'price': int(price.get_text())
            }
            sheet_line.insert_one(data)


def find_sheet_line():
    for item in sheet_line.find():
        if item['price'] >=  500 :
            print(item)

#start(1)
find_sheet_line()

