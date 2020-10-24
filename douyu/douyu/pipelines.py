# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from urllib import request

class DouyuPipeline:
    def process_item(self, item, spider):
        print(item["name"])
        print(item["imagelink"])

        # request.urlretrieve((item["imagelink"],"jpg/"+item["name"]+".jpg"))
        '''
        split()：拆分字符串。通过指定分隔符对字符串进行切片，并返回分割后的字符串列表（list）
        '''
        templist=item["imagelink"].split("/")
        # print(len(templist))
        jpgname=templist[len(templist)-2 ]
        print(jpgname)
        request.urlretrieve(item["imagelink"],"jpg/"+item["name"]+".jpg")

        return item
