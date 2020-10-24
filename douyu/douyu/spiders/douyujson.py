# -*- coding: utf-8 -*-
import scrapy
import json
from douyu import items

class DouyujsonSpider(scrapy.Spider):
    name = 'douyujson'
    allowed_domains = ['douyu.com']
    start_urls = ['https://www.douyu.com/gapi/rknc/directory/yzRec/1']
    url='https://www.douyu.com/gapi/rknc/directory/yzRec/'
    offset=1

    def parse(self, response):
        # 提取json字段
        datas=json.loads(response.text)["data"]["rl"]
        # print(datas)
        for dataline in datas:
            # print(dataline['rid'])
            douyuitem=items.DouyuItem()
            # 主播名字
            douyuitem["name"]=dataline["nn"]
            # 主播照片链接
            douyuitem["imagelink"]=dataline["rs1"]
            # 主播照片路径
            # douyuitem["imagepath"]=dataline["nn"]
            yield douyuitem

        if self.offset<2:
            self.offset+=1
            yield scrapy.Request(self.url+str(self.offset),callback=self.parse)