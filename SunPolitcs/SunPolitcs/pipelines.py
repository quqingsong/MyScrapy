# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class SunpolitcsPipeline:
    # 初始化文件
    def __init__(self):
        self.file = open("1.txt", "w")

    # 关闭文件
    def __del__(self):
        self.file.close()

    # 处理文件
    def process_item(self, item, spider):
        text = str(item) + "\n"
        self.file.write(text)
        # self.flush()
        return item