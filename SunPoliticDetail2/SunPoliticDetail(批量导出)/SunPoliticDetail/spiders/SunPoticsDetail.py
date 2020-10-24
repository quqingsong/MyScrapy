# -*- coding: utf-8 -*-
import scrapy
#这种格式可以少写
from SunPoliticDetail import items
#提取链接
from scrapy.linkextractors import LinkExtractor
# 循环抓取规则
from scrapy.spiders import CrawlSpider,Rule



class SunpoticsdetailSpider(CrawlSpider):
    name = 'SunPoticsDetail'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/political/index/politicsNewest?id=1&page=1']
    url='http://wz.sun0769.com/political/politics/index?id=456673'
    rules = (
        #翻页
        Rule(LinkExtractor(allow=r"id=1&page=\d+")),
        #标题链接
        #LinkExtractor你可以创建自己的自定义链接提取器，以满足您的需求通​​过实现一个简单的界面
        #allow（正则表达式（或的列表）） - 一个单一的正则表达式（或正则表达式列表），（绝对）urls必须匹配才能提取。如果没有给出（或为空），它将匹配所有链接。
        Rule(LinkExtractor(allow=r'id=\d+'),callback="parse_detail"),
    )
    def parse_detail(self, response):

        myitem=items.SunpoliticdetailItem()
        # 标题
        myitem["title"]=response.xpath('normalize-space(//div[@class="mr-three"]/p/text())').extract()[0]
        # 发布时间
        myitem["issuetime"]=response.xpath('normalize-space(//div[@class="mr-three"]//span[2]/text())').extract()[0]
        # 发布内容
        myitem["issuecontent"]=response.xpath('normalize-space(//div[@class="mr-three"]/div[@class="details-box"]/pre/text())').extract()[0]
        # 处理状态
        myitem["dealstate"]=response.xpath('normalize-space(//div[@class="mr-three"]//span[3]/text())').extract()[0]

        yield myitem
