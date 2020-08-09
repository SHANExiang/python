from bs4 import BeautifulSoup
from multiprocessing import Pool
import os
import re
import sys
import time
import urllib.request

 
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# soup = BeautifulSoup(html_doc, features='html.parser')

# print(soup.title) # 获取title标签
# print(soup.prettify()) # 结构化输出文档
# print(soup.title.name) # 获取title标签名称
# print(soup.title.parent.name) # tille的上一级标签名称
# print(soup.p['class'])  # ['title']  p标签的class的值
# print(soup.get_text())  # 获取所有文档内容

# for link in soup.find_all('a'):
#     print(link)
#     print(link.get('href'))  # 获得所有的url

# 伪装成浏览器访问，直接访问的话csdn会拒绝
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}


def get_html(url):
    req = urllib.request.Request(url, headers=headers)
    res = urllib.request.urlopen(req)
    page = res.read().decode('utf-8')
    return page


def get_one_blog(url):
    html = get_html(url)
    soup = BeautifulSoup(html, features='html.parser')
    text = soup.main.find_all('article')[0].div.get_text().strip()
    return text


def get_all_blogs():
    if not os.path.exists('blogs'):
        os.mkdir('blogs')
    url = 'https://blog.csdn.net/wylfengyujiancheng/category_9290640.html'
    html = get_html(url)
    soup = BeautifulSoup(html, features='html.parser')
    # 获得此url下的所有博客
    all_blogs = soup.main.find_all('li')
    for blog in all_blogs:
        one_blog_url = blog.a['href']  # 获得每篇博客的url
        title = blog.a.h2.get_text()  # 每篇博客title
        blog_title = re.findall('\s+.*?\s+(.*)', title)[0].strip()
        text = get_one_blog(one_blog_url)
        with open('blogs/' + blog_title + '.txt', 'w', encoding='utf-8') as f:
            f.write(text)


def get_one_blog_concurrent(blog):
    one_blog_url = blog.a['href']  # 获得每篇博客的url
    title = blog.a.h2.get_text()  # 每篇博客title
    blog_title = re.findall('\s+.*?\s+(.*)', title)[0].strip()
    html = get_html(one_blog_url)
    soup = BeautifulSoup(html, features='html.parser')
    text = soup.main.find_all('article')[0].div.get_text().strip()
    with open('blogs/' + blog_title + '.txt', 'w', encoding='utf-8') as f:
        f.write(text)
    print('博客-%s 已经爬取到本地' % blog_title)


def get_all_blogs_concurrent():
    if not os.path.exists('blogs'):
        os.mkdir('blogs')
    url = 'https://blog.csdn.net/wylfengyujiancheng/category_9290640.html'
    html = get_html(url)
    soup = BeautifulSoup(html, features='html.parser')
    # 获得此url下的所有博客
    all_blogs = soup.main.find_all('li')
    pool = Pool(10)
    pool.map(get_one_blog_concurrent, all_blogs)


if __name__ == '__main__':
    # start_time = time.time()
    # get_all_blogs()
    # end_time = time.time()
    # print(
    #     'use time %s' % (end_time - start_time)) # use time 23.16885471343994

    # 发现python默认的递归深度是很有限的（默认是1000），因此当递归深度超过999的样子，
    # 就会引发这样的一个异常。
    # 修改递归深度的值，让它变大大一点
    sys.setrecursionlimit(100000)
    start_time = time.time()
    get_all_blogs_concurrent()
    end_time = time.time()
    print(
        'use time %s' % (end_time - start_time))  # use time 4.254121780395508
