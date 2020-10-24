# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    # define the fields for your item here like:
    # 主播名字
    name = scrapy.Field()
    # 主播照片链接
    imagelink=scrapy.Field()
    # 主播照片路径
    # imagepath=scrapy.Field()
