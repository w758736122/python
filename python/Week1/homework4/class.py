import requests
import time
from bs4 import BeautifulSoup

#list[titles.stripped_strings] 可以得到多个标签
def home_page(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    links =soup.select('h4 > a' )
    for link in links:
        page_link = link_add(link.get('href'))
        main_page(page_link)

def main_page(url,data = None):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    imgs = soup.select('img[itemprop=image]  ')
    titles = soup.select('h1 > a')
    links =soup.select('h1 > a' )
   # print('img=%d,title=%s,link=%s' %(len(imgs),len(titles),len(links)))

    if data == None:
       # for img,title,link in zip (imgs,titles,links):
        for title,link in zip (titles,links):
            data ={
                'title': title.get_text(),
                'link': link_add(link.get('href')),
             #   'img': img.get('src')
           }
            i=1
            for img in imgs:
                img = img.get('src')
                data['img '+str(i)]= img
                download(img,data['title']+str(i))
                i=i+1
            print(data)



def download(url,filename):
    r = requests.get(url)
    if r.status_code != 200:
        return
   # filename = https://making-photos.b0.upaiyun.com/photos/dfb2128421b04664894a391eb58ab6d0.jpg!middle
   # filename = url.split('!')[0].split('/')[-3]# 第一个split 得到！前面的内容，第二个得到倒数第3个/  后面的内容
    target = './{}.jpg'.format(filename)
    with open(target,'wb') as fs:
         fs.write(r.content)




def link_add(link):
    link = 'https://knewone.com' + link
    return link

def start(start,end):
    for i in range(start,end+1):
        time.sleep(1)
        url='https://knewone.com/things/?page={}'.format(i)
        home_page(url)
start(1,10)