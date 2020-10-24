# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os

class SunpoliticdetailPipeline:

     # 初始化文件
    def __init__(self):
        self.file = open("1.txt", "w")

    # 关闭文件
    def __del__(self):
        self.file.close()

    # 处理文件
    def process_item(self, item, spider):
        text = str(item["title"]) +"\n"+ str(item["issuetime"])+"\n"+ str(item["issuecontent"])+"\n"+ str(item["dealstate"])+"\n\n\n"
        self.file.write(text)
        self.file.flush()
        return item

   #  def process_item(self, item, spider):
   #      # 获取当前工作目录
   #      base_dir = os.getcwd()
   #      fiename = base_dir + '/1.txt'
   #      # 从内存以追加的方式打开文件，并写入对应的数据
   #      with open(fiename, 'a') as f:
   #          f.write(item['title'] + '\n')
   #          f.write(item['issuetime'] + '\n')
   #          f.write(item['issuecontent'] + '\n')
   #          f.write(item['dealstate'] + '\n\n')
   #      return item
   #