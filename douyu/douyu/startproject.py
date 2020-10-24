#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :startproject.py
# @Time      :2020/5/17 19:37
# @Author    :青松
 

from scrapy import cmdline
import os
import sys
# sys.path.append(os.path.dirname(os.path.abspath("D:\PycharmProjects\MyScrapy\douyu\douyu\spiders\douyujson.py")))
# sys.path.append("spiders/douyujson.py")
cmdline.execute(["scrapy","crawl","douyujson","-o","1.json","-s","FEED_EXPORT_ENCODING=utf-8"])
