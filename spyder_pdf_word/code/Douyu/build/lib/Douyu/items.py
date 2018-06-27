# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    # 房间id
    room_link = scrapy.Field()
    # 昵称
    nick_name = scrapy.Field()
    # 所在城市
    city = scrapy.Field()
    # 图片的网络链接
    image_link = scrapy.Field()
    # 图片在本地的存储路径
    image_path = scrapy.Field()
