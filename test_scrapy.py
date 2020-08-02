from multiprocessing import Pool
import re
import sys
import urllib.request


def test_urllib_request():
    response = urllib.request.urlopen(
        'https://www.cnblogs.com/paulwhw/p/12054976.html')
    html = response.read()
    html = html.decode('utf-8')
    print(html)


# 伪装成浏览器访问，直接访问的话csdn会拒绝
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}


def get_one_blog_content(blog_url):
    req = urllib.request.Request(blog_url, headers=headers)
    response = urllib.request.urlopen(req)
    page = response.read().decode('utf-8')
    # print(page)
    blog_content = re.findall('<div id=\"topics\">(.*?)<script src=', page, re.S)
    title = re.findall('<span>(.*?)</span>', blog_content[0])
    with open('%s.txt' % title[0].lstrip().rstrip(), 'w+', encoding='utf-8') as f:
        dr = re.compile(r'<[^>]+>', re.S)
        blog_content = dr.sub('', blog_content[0])
        f.write(blog_content)
    # print(blog_content)


def get_all_blog_urls():
    base_url = 'https://www.cnblogs.com/jingqueyimu/category/1606791.html'

    # 构造请求
    req = urllib.request.Request(base_url, headers=headers)

    # 访问页面
    response = urllib.request.urlopen(req)
    page = response.read()
    # type = sys.getfilesystemencoding()
    page = page.decode('utf-8')
    print(page)
    blog_urls = re.findall(
        'entrylistItemTitle\"\s+href=\"(.*?)\">', page, re.S)
    print(len(blog_urls))
    # 多进程爬取
    pool = Pool(8)
    result = pool.map(get_one_blog_content, blog_urls)
    print(result)


if __name__ == '__main__':
    get_all_blog_urls()

