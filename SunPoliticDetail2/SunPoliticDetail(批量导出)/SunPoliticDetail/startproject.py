#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :startproject.py
# @Time      :2020/5/17 19:37
# @Author    :青松
 

from scrapy import cmdline

cmdline.execute(["scrapy","crawl","SunPoticsDetail","-o","1.json","-s","FEED_EXPORT_ENCODING=utf-8"])