#总结：nth-of-type(3) 表示同类型第三个！
#     在select 中就可以对爬取的数据进行整理
import requests
from bs4 import BeautifulSoup
import pymongo
import random
import time


client = pymongo.MongoClient('localhost',27017)
week_two_bigHW = client['week_two_bigHW']
week_two_bigHW_sheet2 = week_two_bigHW['week_two_bigHW_sheet2']
headers  = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
    'Connection':'keep-alive'
}
#proxy_list = [
     #'http://122.225.106.36:80',
     #'http://123.88.13.215:9000',
     #'http://59.44.152.110:9999',
#    ]
#proxy_ip = random.choice(proxy_list) # 随机获取代理ip
#proxies = {'http': proxy_ip}

def get_item(url):
    wb_data = requests.get(url,headers=headers)#@proxies=proxies
    wb_data.encoding = 'UTF-8'
    if wb_data.status_code == 404: pass
    else:
        soup = BeautifulSoup(wb_data.text,'lxml')
        titles = soup.select('div.content.clearfix > div.leftBox > div.col-cont.title-box > h1')
        times = soup.select(' div > ul.title-info-l.clearfix > li > i')[0].text.strip().split()
        if times != '':
            if len(times) > 0:
                time =times[0].replace('\n','').replace('\xa0','').replace('发布','')
            else:
                time = None
        else:
            time = None
        type1 = soup.select('  div.det-laybox > ul.det-infor > li  > span > a')
        type2= soup.select('  div.det-laybox > ul.det-infor > li  > span.f12.p-type > a')
        types=set(type1) - set(type2)
        prices = soup.select(' div > div > ul > li  > i.f22.fc-orange.f-type')
        trading_sites = soup.select(' div > ul.det-infor > li:nth-of-type(3)   > a')
        new_olds = soup.select('div.second-sum-cont  > ul.second-det-infor.clearfix > li ')
        for title,price,new_old in zip(titles,prices,new_olds):
            data={
                'title' : title.get_text(),
                'price': price.get_text(),
                'new_old' : new_old.get_text().replace('\n','').replace(' ',''),
                'url': url,
            }
            data['time'] =time
            data['type'] = list(map(lambda x:x.text,types))#有多个字段需要合成用这个方法！！！！！！！！！
            data['trading_site'] = list(map(lambda x:x.text,trading_sites))
            week_two_bigHW_sheet2.insert_one(data)
            print(data['url'])

def test(channel,page):
    url = '{}o{}'.format(channel,page)
    wb_data = requests.get(url,headers=headers)  #proxies=proxies
    wb_data.encoding = 'UTF-8'
    soup = BeautifulSoup(wb_data.text,'lxml')
 #   print(soup)
    link = soup.select('div.ft-db > ul > li > a ')
    if not soup.find('div','cont clearfix'):
        for links in link:
            #time.sleep(1)
            real_link =  links.get('href')
            get_item(real_link)
          #  print(soup)

    else:pass

#test('http://sh.ganji.com/mi-hongmi/',1)




#get_item('http://sh.ganji.com/shouji/1644393028x.htm')
# "url" : "http://sh.ganji.com/shouji/1419277653x.htm"  打印结果为‘’
#test('http://sh.ganji.com/mi-hongmi/',1)