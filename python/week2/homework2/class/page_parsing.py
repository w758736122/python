import requests
from bs4 import BeautifulSoup
import pymongo
import time

#url = 'http://sh.58.com/shouji/0/pn2/'

client= pymongo.MongoClient('localhost',27017)
ceshi = client['ceshi']
url_list = ceshi['url_list']

item_info= ceshi['item_info_list']
#spider 1

def get_links_from(channel,pages,who_sells=0):
    list_view = '{}{}/pn{}/'.format(channel,str(who_sells),str(pages))
    if list_view == 'http://jump.zhineng.58.com/clk':
        pass
    else:
        wb_data =  requests.get(list_view)
        soup =BeautifulSoup(wb_data.text,'lxml')
        if soup.find('td','t'):#如果能找到td标签，class=t的 组
            for link in soup.select('    td.t > a.t'):
                item_link = link.get('href').split('?')[0]
                if 'sh.58.com' in item_link:
                    url_list.insert_one({'url': item_link})
                    print(item_link)
                else:
                    pass
        else:
            pass

def get_item_info(url):
    wb_data = requests.get(url)
    soup =BeautifulSoup(wb_data.text,'lxml')
    no_longer_exist = '404' in soup.find('script', type='text/javascript').get('src').split('/')
    if no_longer_exist :
        pass
    else:
        title =soup.title.text.replace('\r','').replace('\n','')
        price = soup.select('span.price_now')[0].text
        area =soup.select(' div.palce_li > span > i')[0].text if soup.find_all('div','palce_li') else None
        #find_all  (标签， class)
        item_info.insert_one({'title':title,'price':price,'area':area})
        print({'title':title,'price':price,'area':area})

#get_links_from('http://sh.58.com/shouji/',2)
#get_item_info('http://zhuanzhuan.58.com/detail/749420139193761796z.shtml')