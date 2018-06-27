# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
import os
from scrapy.pipelines.images import ImagesPipeline
from settings import IMAGES_STORE

import pymongo

# 自定义了图片管道类，重写父类的方法处理图片
class DouyuPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        # 发送图片请求，并将图片自动保存到settings.py里配置IMAGES_STORE指定的路径下
        yield scrapy.Request(item['image_link'])

    def item_completed(self, results, item, info):
        #print "*****" * 30
        #print results
        #print "*****" * 30

        # 取出每个图片的原文件名
        image_path = [x['path'] for ok, x in results if ok]

        # 指定图片的新的保存路径
        item['image_path'] = IMAGES_STORE + item['nick_name'] + '.jpg'

        # 根据图片的原位置，修改为新的图片名
        os.rename(IMAGES_STORE + image_path[0], item['image_path'])

        return item


class DouyuMongoDBPipeline(object):
    def __init__(self):
        # 创建MongoDB数据库链接
        self.client = pymongo.MongoClient(host = "127.0.0.1", port = 27017)
        # 指定存储数据的数据库名
        self.db_name = self.client['Douyu']
        # 指定数据库下的表名
        self.sheet_name = self.db_name['DouyuDirector']

    def process_item(self, item, spider):
        # 向数据库的表里插入数据，参数是一个字典
        self.sheet_name.insert(dict(item))
        return item




