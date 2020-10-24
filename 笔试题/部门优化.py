#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :智线云笔试题.py
# @Time      :2020/6/6 15:21
# @Author    :青松
 

'''
1.某公司内有 4 个项⽬组，项⽬组 A、B、C、D，项⽬组A现有10⼈，项⽬组B现有7⼈，项⽬组C现 有5⼈，项⽬组D现有4⼈。

为了实现跨项⽬组协作，公司决定每⽉从⼈数最多的项⽬组中抽调 3 ⼈
出来，到其他剩下 3 组中，每组 1 ⼈，这称之为⼀次调整优化

（亦即经过第⼀次调整后，A组有7
⼈，B组有8⼈，C组有6⼈，D组有5⼈）。
那么请问，经过⼗年的优化调整后，各项⽬组各有⼏⼈？
编程求解该问题，并思考是否为最优解。
'''

mydict={'A':10,'B':7,'C':5,'D':4}
# mydict={'A':5,'B':6,'C':8,'D':7}
mytask=120

#排序函数
def mysort(mydict):
   # print(mydict.keys())
   # print(mydict.values())
   #字典排序
   print("调度前:")
   #创建一个字典
   firstdict={}
   for k in sorted(mydict,key=mydict.__getitem__,reverse=True):
       firstdict[k]=mydict[k]
       print(k,mydict[k],end="    ")
   # print("\n")
   return firstdict

#函数优化
def optimization_function(mydict,mytask):
    # 创建新字典
    thirddict = {}
    # print(list(mydict.items()))
    for task in range(mytask):
        print("\n第",task+1,"次人员调度")
        #先进行排序
        if not thirddict:       #如果thirddict字典存在，执行初始条件，否则跳转
            seconddict=mysort(mydict)
        else:
            seconddict = mysort(thirddict)
        # print(seconddict.items())
        print("\n调度后:")


        i = 0
        #开始调度
        for k in seconddict:
            # print(k,firstdict[k],end="    ")
            if i==0:
                thirddict[k]=seconddict[k]-3;
            else:
                thirddict[k]=seconddict[k]+1
            i+=1
        #输出结果
        for k in thirddict:
            print(k,thirddict[k],end="    ")
        print("\n")
    return thirddict

if __name__=="__main__":
    optimization_function(mydict,mytask)

