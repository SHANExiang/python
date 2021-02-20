import scrapy
from mySpider.items import MyspiderItem


class ItcastSpider(scrapy.Spider):
    name = 'silkbaby'
    allowed_domains = []
    start_urls = ["https://www.sm265.net/bd/6/"]

    def parse(self, response):
        # filename = 'teacher.html'
        # open(filename, 'wb').write(response.body)

        # content = response.xpath("/html/head/title/text()")
        # title = content.extract_first()
        # print(title)
        #
        href_list = response.xpath("//div[@class='con-3-2 mt20']/ul[@class='detail-list']/li/a/@href")
        print(list(href_list))
        for href in href_list:
            print(href)
            yield scrapy.Request(url=href.extract(), callback=self.get_info)

        next_page_urls = response.xpath(
            "//div[@class='con-3-left fl']//div[@class='page mt20']//div[@class='page-show']/a/@href").extract()  # 翻页
        next_page_urls.pop()
        next_url = next_page_urls.pop()
        next_start = response.follow(next_url)
        if next_page_urls is not None:
            yield response.follow(next_url, self.parse)

    def get_info(self, response):
        for each in response.xpath("//div[@class='content']"):
            print(each)
            item = MyspiderItem()
            item['image_urls'] = each.xpath(
                '//img//@src').extract()  # 提取图片链接
            # print 'image_urls',item['image_urls']
            yield item

        next_page_urls = response.xpath(
            "/html/body/div[@class='page mt20']//div[@class='page-show']/a/@href").extract()  # 翻页
        next_url = next_page_urls.pop()
        next_start = response.follow(next_url)
        if next_page_urls is not None:
            print('enter next request')
            yield response.follow(next_url, callback=self.get_info)
