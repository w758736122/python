import requests
from bs4 import BeautifulSoup
import pymongo

client = pymongo.MongoClient('localhost',27017)
week_two_bigHW = client['week_two_bigHW']
week_two_bigHW_sheet = week_two_bigHW['week_two_bigHW_sheet']

def big_channel(url,data = None):
    wb_data = requests.get(url)
    wb_data.encoding = 'utf-8'
    soup = BeautifulSoup(wb_data.text,'lxml')
    titles = soup.select('div.main > ul > li  > div > dl  > dd > a ')
    links = soup.select('div.main > ul > li  > div > dl  > dd > a ')
    if data == None:
        for title,link in zip (titles,links):
            data = {
                'title': title.get_text(),
                'link' : 'http://sh.ganji.com'+link.get('href')
            }
            week_two_bigHW_sheet.insert_one(data)
            print(data['link'])

#url='http://sh.ganji.com/wu/'
#big_channel(url)

channel_lists='''
http://sh.ganji.com/iphone/
http://sh.ganji.com/cpu/
http://sh.ganji.com/yingpan/
http://sh.ganji.com/xianshiqi/
http://sh.ganji.com/neicun/
http://sh.ganji.com/zhuban/
http://sh.ganji.com/wuxianluyouqi/
http://sh.ganji.com/yidongyingpan/
http://sh.ganji.com/diannaoyinxiang/
http://sh.ganji.com/dayinji/
http://sh.ganji.com/3gwangka/
http://sh.ganji.com/danfanxiangji/
http://sh.ganji.com/dandianxiangji/
http://sh.ganji.com/jingtou/
http://sh.ganji.com/shumashexiangji/
http://sh.ganji.com/yueqiyinxiang/
http://sh.ganji.com/psp/
http://sh.ganji.com/ps3/
http://sh.ganji.com/zhanghaozhuangbei/
http://sh.ganji.com/chongzhidianka/
http://sh.ganji.com/qqhao/z1/
http://sh.ganji.com/chuangdian/
http://sh.ganji.com/guizi/
http://sh.ganji.com/zhuoyi/
http://sh.ganji.com/shafachaji/
http://sh.ganji.com/rirongbaihuo/
http://sh.ganji.com/bangongjiaju/
http://sh.ganji.com/jiaju/_%E6%90%AC%E5%AE%B6/
http://sh.ganji.com/jiaju/p1/
http://sh.ganji.com/dianshi/
http://sh.ganji.com/bingxiang/
http://sh.ganji.com/kongtiao/
http://sh.ganji.com/reshuiqi/
http://sh.ganji.com/xiyiji/
http://sh.ganji.com/diancilu/
http://sh.ganji.com/weibolu/
http://sh.ganji.com/doujiangji/
http://sh.ganji.com/yueqiyinxiang/
http://sh.ganji.com/zixingchemaimai/
http://sh.ganji.com/diandongche/
http://sh.ganji.com/motuoche/
http://sh.ganji.com/sanlunche/
http://sh.ganji.com/anmobaojian/
http://sh.ganji.com/chuangshangyongpin/
http://sh.ganji.com/zhuangshibaishe/
http://sh.ganji.com/yingerche/
http://sh.ganji.com/niuniuche/
http://sh.ganji.com/xuebuche/
http://sh.ganji.com/ertonganquanzuoyi/
http://sh.ganji.com/yingerchuang/z1/
http://sh.ganji.com/niaobushi/
http://sh.ganji.com/naifen/
http://sh.ganji.com/tongche/
http://sh.ganji.com/tongzhuang/
http://sh.ganji.com/wanju/
http://sh.ganji.com/qunzi/
http://sh.ganji.com/gaogenxie/
http://sh.ganji.com/liangxie/
http://sh.ganji.com/shoubiao/
http://sh.ganji.com/shipin/
http://sh.ganji.com/lvxingxiang/
http://sh.ganji.com/danjianbao/
http://sh.ganji.com/shuangjianbao/
http://sh.ganji.com/shoutibao/
http://sh.ganji.com/xiangshui/
http://sh.ganji.com/fangshaishuang/
http://sh.ganji.com/dog/
http://sh.ganji.com/mao/

'''