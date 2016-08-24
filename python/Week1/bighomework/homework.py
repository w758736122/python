from bs4 import BeautifulSoup
import requests
import time
url_home='http://bj.58.com/pingbandiannao/1/?PGTID=0d305a36-0000-1cbd-9ba1-8b330c3c7459&ClickID=1'
url='http://bj.58.com/pingbandiannao/25555198294863x.shtml'


def get_view_from(url):
    id = url.split('/')[-1].strip('x.shtml')
    api ='http://jst1.58.com/counter?infoid={}'.format(id)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
        'Cookie': 'id58=YM8UUVct+hwODZzz1llByg==; als=0; myfeet_tooltip=end; bj58_id58s="LTcwWUd5WDVmY2h0NjY5MQ=="; bangbigtip2=1; cookieuid=d536ed1f-182c-466f-a5a5-ad6616d977d7; br58_ershou=salev1_ershou; m58comvp=t01v115.159.229.11; cookieuid1=c5/ni1d2dA83d0SNA4EcAg==; 58_to_zz=1; mcity=bj; mcityName=%E5%8C%97%E4%BA%AC; nearCity=%5B%7B%22cityName%22%3A%22%E5%8C%97%E4%BA%AC%22%2C%22city%22%3A%22bj%22%7D%5D; 58app_hide=1; city=sh; 58home=sh; ipcity=sh%7C%u4E0A%u6D77; sessionid=38f5350a-126f-45bc-a09f-174f0c6c92ee; zz_download=2; 58tj_uuid=2cb41fa8-d0e3-4e44-9543-961dc6e8c690; new_session=0; new_uv=3; utm_source=; spm=; init_refer=; final_history={}%2C26553966056499%2C26549884228810%2C26062681492781%2C26542862991666; bj58_new_session=0; bj58_init_refer=""; bj58_new_uv=3'.format(id),
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'jst1.58.com',
        'Referer': r'http://bj.58.com/pingbandiannao/{}x.shtml'.format(str(id))
        }
    js = requests.get(api , headers=headers)
    view =js.text.split('=')[-1]
    return view

#get_view_from(url)





def home_page(start,end):
    urls=[]
    for i  in range(start,end+1):
        list_views = 'http://bj.58.com/pingbandiannao/{}/?PGTID=0d305a36-0000-1cbd-9ba1-8b330c3c7459&ClickID=1'.format(
            0)
        wb_data = requests.get(list_views)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        links=soup.select('  td.t a.t ')
        print(links)
home_page(1,9)


def goods_page(url,data= None):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    categorys = soup.select('  #header > div.breadCrumb.f12')
 #   categorys = soup.select('  a[href="http://bj.58.com/pbdn/"]')
    titles = soup.select(' div.col_sub.mainTitle > h1')
   #    titles = soup.title.text
    prices = soup.select(' div.su_con > span')
    addresses = soup.select(' div.tonte_two_p')
    volumns = soup.select(' li.count')
    times = soup.select(' ul.mtit_con_left.fl > li.time')
    print(times)
    if data == None:
        for category,title,price,time_s,addresses,volumn in zip(categorys,titles,prices,times,addresses,volumns):
            data = {
                'category' : category.get_text().replace('\n','',1 ).replace('\n','--',2).replace('\n',''),
                'title': title.get_text(),
                'prices': price.get_text(),
                'time' : time_s.get_text(),
                'addresses' : addresses.get_text().split('\n')[1],
                'volumn' : volumn.get_text()
            }
            print(data)


#goods_page(url)


