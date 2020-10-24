# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SunpoliticdetailItem(scrapy.Item):
    # define the fields for your item here like:
    #标题
    title = scrapy.Field()
    #发布时间
    issuetime=scrapy.Field()
    #发布内容
    issuecontent=scrapy.Field()
    # 处理状态
    dealstate = scrapy.Field()
