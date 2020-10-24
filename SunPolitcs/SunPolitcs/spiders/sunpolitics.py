# -*- coding: utf-8 -*-
import scrapy
#这种格式可以少写
from SunPolitcs import items
#提取链接
from scrapy.linkextractors import LinkExtractor
# 循环抓取规则
from scrapy.spiders import CrawlSpider,Rule


class SunpoliticsSpider(scrapy.Spider):
    count = 1
    name = 'sunpolitics'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/political/index/politicsNewest?id=1&page=1']

    def parse(self, response):
        # 字典的形式
        trlist = response.xpath('//ul[@class="title-state-ul"]/li')
        for list in trlist:
            sunpoliticsItems = items.SunpolitcsItem()
            sunpoliticsItems["id"] = list.xpath('normalize-space(./span[@class="state1"]/text())').extract()
            sunpoliticsItems["state"] = list.xpath('normalize-space(./span[@class="state2"]/text())').extract()
            sunpoliticsItems["title"] = list.xpath('normalize-space(./span[@class="state3"]/a/text())').extract()
            sunpoliticsItems["dealtime"] = list.xpath('normalize-space(./span[@class="state4"]/text())').extract()
            sunpoliticsItems["politicstime"] = list.xpath('normalize-space(./span[@class="state5 "]/text())').extract()

            yield sunpoliticsItems

        # 翻页爬取
        if self.count < 3:
            self.count += 1
        next_url = "http://wz.sun0769.com/political/index/politicsNewest?id=1&page=" + str(self.count)
        yield scrapy.Request(next_url, callback=self.parse)
