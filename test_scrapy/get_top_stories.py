from bs4 import BeautifulSoup
from urllib.request import urlopen


def test_get_top_stories():
    # url = "https://news.google.com/rss?hl=zh-HK&gl=HK&ceid=HK:zh-Hant"
    # client = urlopen(url)
    # html_page = client.read()
    # client.close()
    with open('xml', 'r', encoding='utf-8') as f:
        xml_page = f.read()
    print(xml_page, type(xml_page))
    soup_page = BeautifulSoup(xml_page, 'xml')
    print(soup_page)
    news_list = soup_page.findAll('item')
    print(news_list)
    for x in news_list:
        print(x.title.text)
        print(x.link.text)
        print(x.pubDate.text)
        print('-'*60)


# test_get_top_stories()
