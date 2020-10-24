#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :计算最大差值.py
# @Time      :2020/6/8 4:12
# @Author    :青松

'''
 有两组数，第⼀组数顺序固定，请编程实现让第⼆组数 相邻数字间的⼤⼩关系和第⼀组数相同，且
第⼆组相邻数字间的差值之和最⼤
下⾯给出⼀个示例
第⼀组数： 5 7 4 9
第⼆组数：1 2 3 4
第⼆组数排序结果：2 4 1 3
第⼆组数排序后的差值之和：7 = abs(2-4) + abs(4-1) + abs(1-3)
'''
firstlist=[5,7,4,9]
secondtlist=[1,2,3,4]

#排序
def sort(firstlist,secondlist):
    print("第一组:")
    for first in firstlist:
        print(first,end="    ")
    print()
    # if firstlist[1]>firstlist[0] and firstlist[2]<firstlist[1] and firstlist[3]>firstlist[2]:
    print("第二组:")
    thirdlist=sorted(secondtlist)
    # print("列表排序处理")
    # for third in thirdlist:
    #     print(third,end="    ")
    #找出最小值
    min_velue=thirdlist[0]
    #找出最大值
    max_velue=thirdlist[3]
    #找到次小值
    minsencond_velue=thirdlist[1]
    #排列方法就是次小，最小，最大，次大
    fourthlist=[0,0,0,0]
    fourthlist[0]=minsencond_velue
    fourthlist[1]=max_velue
    fourthlist[2]=min_velue
    fourthlist[3]=thirdlist[2]
    for fourth in fourthlist:
        print(fourth, end="    ")


    maxdifference_value=abs(fourthlist[0]-fourthlist[1])+abs(fourthlist[1]-fourthlist[2])+abs(fourthlist[2]-fourthlist[3])
    print()
    print("最大差值为:",maxdifference_value)





if __name__=="__main__":
    sort(firstlist,secondtlist)
