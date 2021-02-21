# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os
from mySpider import settings
import urllib


class MyspiderPipeline:
    # silkbaby
    def process_item(self, item, spider):
        dir_path = '%s/%s' % (settings.IMAGES_STORE, spider.name)  # 存储路径
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        for image_url in item['image_urls']:
            list_name = image_url.split('/')
            file_name = list_name[len(list_name) - 1]  # 图片名称
            photoes_tag = file_name.split('-')[0]
            photoes_dir = "%s/%s" % (dir_path, photoes_tag)
            if not os.path.exists(photoes_dir):
                os.makedirs(photoes_dir)
            file_path = '%s/%s' % (photoes_dir, file_name)
            if os.path.exists(file_name):
                continue
            with open(file_path, 'wb') as file_writer:
                conn = urllib.request.urlopen(image_url)  # 下载图片
                print('photo %s is downloading' % file_path)
                file_writer.write(conn.read())
            file_writer.close()
        return item

    # MaskedQueen
    # def process_item(self, item, spider):
    #     dir_path = '%s/%s' % (settings.IMAGES_STORE, spider.name)  # 存储路径
    #     if not os.path.exists(dir_path):
    #         os.makedirs(dir_path)
    #     for image_url in item['image_urls']:
    #         list_name = image_url.split('/')
    #         file_name = list_name[len(list_name) - 1]  # 图片名称
    #         photoes_dir = "%s/%s" % (dir_path, item['alt'])
    #         if not os.path.exists(photoes_dir):
    #             os.makedirs(photoes_dir)
    #         file_path = '%s/%s' % (photoes_dir, file_name)
    #         if os.path.exists(file_name):
    #             continue
    #         with open(file_path, 'wb') as file_writer:
    #             conn = urllib.request.urlopen(image_url)  # 下载图片
    #             print('photo %s is downloading' % file_path)
    #             file_writer.write(conn.read())
    #         file_writer.close()
    #     return item
