from bs4 import BeautifulSoup
import time
import requests

def getSex(sex):
    if sex == ['member_ico']:
        return '男'
    elif sex == ['member_ico1']:
        return '女'
    else:
        return '未提交性别 '

def main_url(url):
 #   url='http://sh.xiaozhu.com/'
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    urls = soup.select(' ul > li > a.resule_img_a ')
    for url in urls:
        url = url.get('href')
        page(url)



def page(url,data = None):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')#不要忘了TEXT!!
    titles =soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > h4 > em')
    addresses = soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p > span.pr5')
    prices = soup.select('div.day_l')
    room_imgs = soup.select('div.pho_show_big > div > img')
    people_imgs =soup.select('div.member_pic > a > img')
    people_names = soup.select(' div.w_240 > h6 > a')
    people_sexs = soup.select(' div.member_pic > div')
    for title,address,price,room_img,people_img,people_name,people_sex in zip(titles,addresses,prices,room_imgs,people_imgs,people_names,people_sexs):
        if data == None:
            data ={
                'title': title.get_text(),
                'address' : address.get_text().replace('\n','').replace(' ',''),
                'price' : price.get_text(),
                'room_img' : room_img.get('src'),
                'people_img' : people_img.get('src'),
                'people_name': people_name.get_text(),
                'people_sex' : getSex(people_sex.get('class')),
            }
            print(data)


urls=['http://sh.xiaozhu.com/search-duanzufang-p{}-0/'.format(i) for i in range(1,14)]# 这是数列！！
for url in urls:
    main_url(url)
