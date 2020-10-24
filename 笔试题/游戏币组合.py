#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :游戏币组合.py
# @Time      :2020/6/7 21:22
# @Author    :青松

mylist = [1, 2, 5, 10]
def calculate_money(count,money):
    mycount=0
    #1分
    for i in range(count+1):
        #2分
        for j in range(count-i+1):
            #5分
            for k in range(count-j+1):
                #计算总和，包含计算10分的面额
                temp=i+2*j+5*k+10*(count-i-j-k)
                if temp==money:
                    mycount+=1

    print("组合数量为:",mycount)

if __name__ == "__main__":
    #输入游戏币数量
    count=input("输入游戏币数量")
    # print("输入的金额范围为:",mylist[0]*int(count),"-",mylist[3]*int(count))
    # 输入金额
    money=input("输入总面值:")
    calculate_money(int(count),int(money))