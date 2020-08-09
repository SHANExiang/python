from bs4 import BeautifulSoup
from multiprocessing import Pool
import os
import re
import requests

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}

# home_url = 'https://www.sm265.net/'

# one_url = 'https://www.sm265.net/bd/69/39022.html'

# label_url = 'https://www.sm265.net/bd/6/'


# 处理分页子页面
def get_pagination_url(one_url):
    html = requests.get(one_url, headers).content
    soup = BeautifulSoup(html, features='html.parser')
    hrefs = soup.find_all(class_="page-show")[0].find_all('a')
    url_list = set()
    base_url = one_url.split('/')[:-1]
    base_url = '/'.join(base_url)
    for x in hrefs:
        href = x.get('href')
        print(href)
        if not href:
            continue
        url_list.add(base_url + "/" + href)
    url_list.add(one_url)
    return list(url_list)


def scrapy_photoes_one_url(url):
    html = requests.get(url, headers).content
    soup = BeautifulSoup(html, features='html.parser')
    text = soup.find_all('img')
    for x in text:
        src = x.get('src')
        dir = x.get('alt')
        if not os.path.exists(dir):
            os.mkdir(dir)
        image_name = src.split('/')[-1]
        res = requests.get(src, headers)
        with open(dir + '/' + image_name, 'wb') as f:
            f.write(res.content)
            print('get images %s successful' % (dir + '/' + image_name) )


# 一个页面有多个子页面
def scrapy_label_photoes(label_url):
    html = requests.get(label_url, headers).content
    soup = BeautifulSoup(html, features='html.parser')
    text = soup.find_all('li')
    label_url_list = list()
    for x in text:
        href = x.a.get('href')
        base_url = href.split('/')[:-1]
        base_url = '/'.join(base_url)
        if base_url + '/' == label_url:
            label_url_list.append(href)
    return label_url_list


def scrapy_photoes_all_urls():
    # pool = Pool(8)
    # pool.map(scrapy_photoes_one_url, get_pagination_url(one_url))
    for x in get_pagination_url(label_url):
        for y in scrapy_label_photoes(x):
            pool = Pool(8)
            pool.map(scrapy_photoes_one_url, get_pagination_url(y))


# soup = BeautifulSoup(text, features='html.parser')
# a = soup.find_all('img')
# print(a)
# url_list = list()
# for tag in a:
#     new_url = tag.attrs['src']
#     image_name = tag.attrs['alt']
#     url_list.append({image_name: new_url})
#


if __name__ == '__main__':
    scrapy_photoes_all_urls()