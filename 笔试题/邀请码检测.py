#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :邀请码检测.py
# @Time      :2020/6/7 11:51
# @Author    :青松

'''
某产品的⽤户注册邀请码为⼀串有⼩写字⺟和数字组成的字符串，字符串⻓度为16。当⽤户数据邀
请码的时候，系统需要对邀请码做有效性验证，假设验证规则如下： 1、 从序列号最后⼀位字符开始，逆向将奇数位(1、3、5等等)相加；
2、从序列号最后⼀位数字开始，逆向将偶数位数字，先乘以2（如果乘积为两位数，则将其减去
9），再求和；
3、将奇数位总和加上偶数位总和，结果可以被10整除； 4、⼩写字⺟对应数值，可由下⾯键值对确定；
[(a,1), (b,2), (c,3)…,(i,9), (j,1), (k, 2)…]，亦即，按字⺟顺序，1-9循环。
输⼊：输⼊16位字符串，表示邀请码
输出：输出“ok”或者“error”
'''

from random import Random

#随机生成验证码
def random_str(randomlength=16):
    mystr = ''
    strs = 'abcdefghijklmnopqrstuvwxyz0123456789'
    length = len(strs) - 1
    random = Random()
    for i in range(randomlength):
        mystr+=strs[random.randint(0, length)]
    print("邀请码如下:",end="    ")
    print(mystr)
    return mystr

#创建字母字典
def create_dict():
    mydict={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':1,'k':2,'l':3,'m':4,'n':5,'o':6,'p':7,'q':8,'r':9,'s':1,'t':2,'u':3,'v':4,'w':5,'x':6,'y':7,'z':8}
    return mydict
#验证码检测
def create_verificationcode():
    mydict=create_dict()
    mystr=random_str()
    mylist=list(mystr)
    #列表反转
    newlist=list(reversed(mylist))


    #数据
    # print("字符串数据:")
    # for mychar in newlist:
    #     print(mychar,end="    ")
    # print("\n")
    # print("字符串数据索引:")
    #求和
    number = 0
    #奇数求和
    oddnumber = 0
    #偶数求和
    evennumber = 0
    #奇数位相加
    for myindex in range(len(newlist)):
        # print(myindex, end="    ")
        #索引为奇数
        if myindex%2!=0:
            #奇数相加
            for k in mydict:
                #和字典做对比
                # 邀请码如下:
                # lqve6zv9nvjaijky
                if newlist[myindex]==k:
                    oddnumber+=mydict[k]
                else:
                    oddnumber+=mydict[k]
        #索引为偶数
        else:
            for k in mydict:
                # 和字典做对比
                # 邀请码如下:
                # lqve6zv9nvjaijky
                if newlist[myindex] == k:
                    #如果是两位数
                    if mydict[k]*2 >= 10:
                        # 偶数位数字*2
                        temp=mydict[k]*2
                        # 如果乘积为两位数，则将其减去9，再求和;
                        temp -= 9
                        evennumber+=temp
                    #如果不是两位数
                    else:
                        evennumber+=mydict[k]
                #只是数字
                else:
                    evennumber += mydict[k]

        number=oddnumber+evennumber
    print("输出结果如下:",end="    ")
    # print(number)
    if number%10==0:
        print("ok")
    else:
        print("error")


if __name__=="__main__":
    #邀请码检验
    create_verificationcode()