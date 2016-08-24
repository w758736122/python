from bs4 import BeautifulSoup
import  requests
import time

url = 'http://piao.ctrip.com/dest/dc-shanghai-2/s-tickets/P1/'
url_saves = 'http://my.ctrip.com/FavoriteOnline/hotel/hotellist.aspx#'
urls = ['http://piao.ctrip.com/dest/dc-shanghai-2/s-tickets/P{}/'.format(str(i)) for i in range(1,26)]

headers = { #键值对加逗号！！！
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
    'Cookie' : 'TicketSiteID=SiteID=1001; appFloatCnt=1; corpid=; corpname=; CtripUserInfo=VipGrade=0&UserName=%bd%aa%bc%ce%ea%ca&NoReadMessageCount=0&U=0673E3D07678346EE26CA52465EDF0F0; AHeadUserInfo=VipGrade=0&UserName=%bd%aa%bc%ce%ea%ca&NoReadMessageCount=0&U=0673E3D07678346EE26CA52465EDF0F0; LoginStatus=1%7c; ticket_ctrip=uoeOwviAJ6VQEgTNwLuTqSV9j/bS+aOP3Riia1P+kyQbgkQZsD2gid+UgjBhH26Q0sy3RzNHdVFGjPbCpmq5KcU0lxsc/1hHHeZvhdcGFuT6EhlrHKrP5rZe8lQCNJ1MJmohlMEhXwDxBjpTpcfjsxUspWMyj6xQjwTvIWJx6Souy3cp5Gop9usj0tASiMMHEOfReErl5KVe1Z8ZgW6rWVoksqlcr83RFTqZtukZ7JiMKUlm5BdNpP27W6CCDK4Cs2yX9w+QQwoWiEsGLFIJSw==; login_type=0; login_uid=0673E3D07678346E5872BB99A18AE021; _fpacid=09031127110292664855; GUID=09031127110292664855; _abtest_userid=9e39a55a-be31-447c-ae23-ff3421d2e944; adscityen=Shanghai; userNofloat=false; ASP.NET_SessionSvc=MTAuOC4xMTUuNDJ8OTA5MHxqaW5xaWFvfGRlZmF1bHR8MTQ0OTEzMzU4NDAzMA; ASP.NET_SessionId=gqhfkdtonxsikkx2blmuhrm3; MyCtripDescription=UID=0673E3D07678346EDD3BB4EE7AD4EB92&IsClub140=F&IsHoliday=F&CorpMileage=F; IntHotelCityID=splitsplitsplit2016-07-01split2016-07-02splitsplit; __utma=13090024.717099024.1467119118.1467123019.1467260015.2; __utmc=13090024; __utmz=13090024.1467260015.2.2.utmcsr=my.ctrip.com|utmccn=(referral)|utmcmd=referral|utmcct=/FavoriteOnline/hotel/hotellist.aspx; StartCity_Pkg=PkgStartCity=2; _gat=1; _ga=GA1.2.717099024.1467119118; __zpspc=9.4.1467262290.1467263340.14%234%7C%7C%7C%7C%7C%23; _jzqco=%7C%7C%7C%7C1467259947708%7C1.1981039116.1467119117573.1467263324351.1467263340051.1467263324351.1467263340051.undefined.0.0.33.33; _bfa=1.1467119083859.2p1p4h.1.1467259943682.1467262287379.4.43; _bfs=1.17; _bfi=p1%3D600001509%26p2%3D600001509%26v1%3D43%26v2%3D42'
    }

def get_attractions(url,data=None):
    wb_data = requests.get(url)# 返回response
    time.sleep(4)
    soup = BeautifulSoup(wb_data.text,'lxml')#text 方法， 使response 可读

    titles = soup.select('div.search_ticket_title > h2 > a')
    imgs = soup.select('img[width=132]')
    scores = soup.select('div.search_ticket_assess > span.grades')
    stars = soup.select('span.rate')
    if data == None:
        for title,img,score,star in zip(titles,imgs,scores,stars):
            data = {
                '景区名称': title.get_text().replace('\n','').replace(' ',''),
                '景点图片' : img.get('src'),
                '网友评分': score.get_text().replace(' ','').replace('\n',''),
                '国际评级' : len(star.get_text())
            }
            print(data)
def get_favs(url,data = None):
    wb_data =requests.get(url,headers=headers)
    soup = BeautifulSoup(wb_data.text,'lxml')
    titles= soup.select('h2.desc > a')
    imgs = soup.select('img[width="188"]')
    scores = soup.select('span.rank')
    prices  = soup.select('span.price ')
    if data == None:
        for title,img,score, price in zip(titles,imgs,scores,prices):
            data ={
                'title' : title.get_text(),
                'img' : img.get('src'),
                'score': score.get_text(),
                'price' : price.get_text()
            }
            print(data)

for single_url in urls:
    get_attractions(single_url)