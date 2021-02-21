import re
import scrapy
from mySpider.items import MyspiderItem, MaskedQueenItem


class ItcastSpider(scrapy.Spider):
    name = 'silkbaby'
    allowed_domains = []
    start_urls = ["https://www.sm265.net/bd/84/",
                  "https://www.sm265.net/bd/73/list_84_2.html",
                  "https://www.sm265.net/bd/73/list_84_3.html",
                  "https://www.sm265.net/bd/73/list_84_4.html"]

    def parse(self, response, **kwargs):
        # filename = 'teacher.html'
        # open(filename, 'wb').write(response.body)

        # content = response.xpath("/html/head/title/text()")
        # title = content.extract_first()
        # print(title)
        current_hrefs_list = \
            response.xpath('//div[@class="con-3-2 mt20"]//ul[@class="detail-list"]/li/a/@href').extract()
        for current_href in current_hrefs_list:
            yield scrapy.Request(url=current_href, callback=self.get_info)

    def get_info(self, response):
        total_page = re.match(
            r"共(\d+)页", response.xpath('//div[@class="page mt20"]//div[@class="page-show"]/a/text()').extract()[0]).group(1)
        print('current url==%s' % response.url)
        yield scrapy.Request(url=response.url, callback=self.get_urls)
        current_url = response.url
        for i in range(2, int(total_page)+1):
            url = current_url[:-5] + '_%s.html' % i
            print('**current url==%s' % url)
            yield scrapy.Request(url=url, callback=self.get_urls)

    def get_urls(self, response):
        item = MyspiderItem()
        each = response.xpath("//div[@class='content']/img//@src")
        item['image_urls'] = each.extract()  # 提取图片链接
        yield item


        # next_page_urls = response.xpath(
        #     "//div[@class='page mt20']//div[@class='page-show']/a/@href").extract()  # 翻页
        # print(next_page_urls)
        # next_url = next_page_urls.pop()
        # print(next_url)
        # next_start = response.follow(next_url)
        # if next_page_urls is not None:
        #     print('enter next request')
        #     yield response.follow(next_url,)


class MaskedQueenSpide(scrapy.Spider):
    name = 'MaskedQueen'
    start_urls = ["https://zhuaicun.com/other/masked.html"]

    def parse(self, response, **kwargs):
        print(response.url)
        current_hrefs_list = \
            response.xpath('//div[@class="update_area"]//div[@class="update_area_content"]/ul/li/a/@href').extract()

        print(current_hrefs_list)

        for current_href in current_hrefs_list:
            url = "https://zhuaicun.com" + current_href
            yield scrapy.Request(url=url, callback=self.get_info)

    def get_info(self, response):
        print('current url==%s' % response.url)
        yield scrapy.Request(url=response.url, callback=self.get_urls)
        urls = response.xpath('//div[@class="nav-links page_imges"]//a[@class="page-numbers"]/@href').extract()
        print(urls)
        for u in urls:
            url = "https://zhuaicun.com" + u
            print('**current url==%s' % url)
            yield scrapy.Request(url=url, callback=self.get_urls)

    def get_urls(self, response):
        item = MaskedQueenItem()
        each = response.xpath('//div[@class="content"]//div[@class="content_left"]/p/img//@src')
        alt = response.xpath('//div[@class="item_title"]/h1/text()').extract()[0]
        item['image_urls'] = each.extract()  # 提取图片链接
        item['alt'] = alt
        print('alt==%s' % item['alt'])
        yield item




