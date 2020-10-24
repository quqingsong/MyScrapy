#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :有趣的两位数.py
# @Time      :2020/6/8 3:30
# @Author    :青松
 
count = 0


for i in range(11, 100):
    #十位数
    first_left = i // 10
    #个位数
    first_right = i % 10

    # 遍历出数字并找出个位和十位()第二个因子比第一个因子大，所以+1操作
    for j in range(i + 1, 100):
        second_left = j // 10
        second_right = j % 10

        # 交换位置
        newfirst = first_right * 10 + first_left
        newsecond = second_right * 10 + second_left
        # 进行if判断
        if i * j == newfirst * newsecond:
            #格式化输出
            print('{} * {} = {} * {}'.format(i, j, newfirst, newsecond))

            count += 1

print("这样的两位数组合一共有:",count,"组")

