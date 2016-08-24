from multiprocessing import Pool
from page_parsing import test
from channel_list_page import channel_lists
import time



def start_BIGhomeWork(channel):
    for i in range(1,2):
        time.sleep(1)
        test(channel,i)


if __name__ == '__main__':
    #pool = Pool(processes=6)
    pool = Pool()
    pool.map(start_BIGhomeWork,channel_lists.split() )
