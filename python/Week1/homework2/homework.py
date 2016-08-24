from bs4 import BeautifulSoup
with open('./1_2_homework_required/index.html','r')as wb_data:
    Soup = BeautifulSoup(wb_data,'lxml')
    images = Soup.select(' body > div > div > div.col-md-9 > div > div > div > img')
    titles = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4 > a')
    prices = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right')
    stars  = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings  ')
    reviews = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p.pull-right')

for title,price,star,review,image in zip(titles ,prices ,stars ,reviews ,images ):
    data = {
        'title' : title.get_text(),
        'price' : price.get_text(),
        'star'  : len(star.find_all("span",class_='glyphicon glyphicon-star')),
        'review' : review.get_text(),
        'image': image.get('src'),
    }

    print(data)
# 总结：   1、每循环1次，输出一次， 不然就只输出最后、一次了！
#          2、find_all 是看同一行的 标签的！！
#          3、div:nth-child(2) 这种是要删掉的！！
#          4、键值对 的 键是要加‘’ 的