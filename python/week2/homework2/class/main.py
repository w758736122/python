from multiprocessing import Pool
from page_parsing import get_links_from
from channel_extract import channel_list


def get_all_links_from(channel):
    for num in range(1,2):
        get_links_from(channel,num)

if __name__ == '__main__':
    pool =Pool()
    pool.map(get_all_links_from,channel_list.split())