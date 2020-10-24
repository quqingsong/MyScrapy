# -*- coding: utf-8 -*-
import scrapy
#这种格式可以少写
from SunPoliticDetail import items


class SunpoticsdetailSpider(scrapy.Spider):
    name = 'SunPoticsDetail'
    allowed_domains = ['wz.sun0769.com']
    offset=0
    start_urls = ['http://wz.sun0769.com/political/index/politicsNewest?id=1&page=1']
    firsturl='http://wz.sun0769.com/political/index/politicsNewest?id=1&page='
    url='http://wz.sun0769.com'
    def parse(self, response):

        links=response.xpath('//*[@class="state3"]/a/@href').extract()

        for link in links:
            newurl=self.url+link
            yield scrapy.Request(newurl,callback=self.parse_content)
        if self.offset<=300:
            self.offset+=1
            yield scrapy.Request(self.firsturl+str(self.offset),callback=self.parse)

    def parse_content(selfs,response):
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
