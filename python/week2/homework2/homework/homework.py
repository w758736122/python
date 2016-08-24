import requests
from bs4 import BeautifulSoup
import pymongo

client =pymongo.MongoClient('localhost',27017)
twoWeek_twoHomewor = client['twoWeek_twoHomewor']
homeWork = twoWeek_twoHomewor['homeWork']
level_TWO = twoWeek_twoHomewor['level_TWO']

def home_page(url,data = None):
    wb_data=requests.get(url)
    soup =BeautifulSoup(wb_data.text,'lxml')
    if soup.find_all('div','boxlist'):
        tittles=soup.select(' a.t > strong')
        links=soup.select('li > a.t')
        if data == None:
            for tittle,link in zip (tittles,links):
                homeWork.insert_one({'tittle': tittle.get_text(),'link' : link.get('href').split('?')[0]})
                print({'tittle': tittle.get_text(),'link' : link.get('href').split('?')[0]})
        print('DB导入已经完成')
        print('----------------------------------------------------------')
        for url_item in homeWork.find():
            url_in = url_item['link']
            item_page(url_in)
    else:
        pass

def item_page(url):
    wb_data=requests.get(url)
    soup =BeautifulSoup(wb_data.text,'lxml')
    price =soup.select(' div.su_con > span')[0].get_text().strip()#去掉空格
    title=soup.select('div.col_sub > h1')[0].get_text().replace('\n','').replace('\t','').replace(' ','').strip()
    level_TWO.insert_one({'price':price,'title':title})
    print({'price':price,'title':title})



home_page('http://bj.58.com/shoujihao/pn2/')
#item_page('http://bj.58.com/shoujihao/26611500896971x.shtml')