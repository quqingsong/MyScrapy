#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test.py
# @Time      :2020/6/6 15:48
# @Author    :青松
'''
def partition(arr, low, hight):
    i = low - 1
    for j in range(low, hight):
        if arr[j] <= arr[hight]:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[hight] = arr[hight], arr[i + 1]
    return i

def quick_sort(l, low, hight):
    if low < hight:
        key_Index = partition(l, low, hight)
        quick_sort(l, low, key_Index)
        quick_sort(l, key_Index + 1, hight)
    else:
        return

l = [5,8,1,3,15,12,0]
quick_sort(l, 0, len(l) - 1)
print("after sort:", l)

# 运行后的结果为：after sort: [0, 1, 3, 5, 8, 12, 15]
'''

'''
scores = {'语文': 89, '数学': 92, '英语': 93}
print(scores)
print("语文")
# 空的花括号代表空的dict
empty_dict = {}
print(empty_dict)
# 使用元组作为dict的key
dict2 = {(20, 30):'good', 30:'bad'}
print(dict2)
'''


'''
mydict={'A':10,'B':7,'C':5,'D':4}
print(mydict['A'])
'''

'''
add = lambda x, y : x+y
print('lambda用法:','x+y=',add(1,2)) # 结果为3

def dictionairy():
    # 声明字典
    key_value = {}

    # 初始化
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323

#   items方法将字典中所有的项以列表方式返回，但是在返回的时候没有特定的顺序；
    print("字典数据输出:")
    print(key_value.items())
    # 输出:dict_items([(2, 56), (1, 2), (5, 12), (4, 24), (6, 18), (3, 323)])
    print(list(key_value.items()))
    print("按值(value)排序:")
    print(sorted(key_value.items(), key=lambda kv:(kv[1], kv[0]),reverse=True))


def main():
    dictionairy()


if __name__ == "__main__":
    main()
'''

'''
d = {'a': 2, 'A': 1, 'c': 3, 'b': 2}
sorted_key_list = sorted(d, key=lambda x: d[x])  # 正向排序
# sorted_key_list = sorted(d, key=lambda x:d[x], reverse=True)      #逆向排序
print(sorted_key_list)

sorted_dict = list(map(lambda x: {x: d[x]}, sorted_key_list))
print(sorted_dict)
'''
'''
mydict={'A':10,'B':7,'C':5,'D':4}

print(list(mydict.items()))
'''

'''
from random import Random
def random_str(randomlength=16):
    mystr = ''
    strs = 'abcdefghijklmnopqrstuvwxyz0123456789'
    length = len(strs) - 1
    random = Random()
    for i in range(randomlength):
        mystr+=strs[random.randint(0, length)]
    print(mystr)
    return mystr

random_str()
'''
# from random import Random
# #随机生成验证码
# def random_str(randomlength=16):
#     mystr = ''
#     strs = 'abcdefghijklmnopqrstuvwxyz0123456789'
#     length = len(strs) - 1
#     random = Random()
#     for i in range(randomlength):
#         mystr+=strs[random.randint(0, length)]
#     print("邀请码如下:")
#     print(mystr)
#     #打印单个字符
#     for mycha in mystr:
#         print(mycha,end="    ")
#     print("\n")
#     #打印索引
#     for mychar in mystr:
#         # print(mychar)
#         print(mystr.index(mychar),end="    ")
#     return mystr
#
# random_str()


# x = [0, 0, 1, 2, 5, 3, 0, 1, 8, 5]
# x_index = []
# for i in range(len(x)):
#     #x[:i]即x[0:i]
#     if x[i] in x[:i]:
#         x_index.append(x_index[-1] + 1)
#     else:
#         x_index.append(x.index(x[i]))
#
# print(x_index)
# for ind in x:
#     print(ind,end="    ")
# print("\n")
# for ind in x:
#     print(x.index(ind),end="    ")
# print("\n")
# # enumerate 方法,将列表中的元素元组化
# print(list(enumerate(x)),end="    ")
# print("\n")
# print(x[0],x[1],x[2])

#根据列表索引输出数据

# print("索引为:")
# for i in range(len(x)):
#     print(i,end="    ")
# print("\n")
# print("索引输出数据:")
# for i in range(len(x)):
#     print(x[i],end="    ")
# print("\n")
# print("输出数据索引:")
# for ind in x:
#     print(x.index(ind),end="    ")

# mydict={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':1,'k':2,'l':3,'m':4,'n':5,'o':6,'p':7,'q':8,'r':9,'s':1,'t':2,'u':3,'v':4,'w':5,'x':6,'y':7,'z':8}
# key = input("请输入你的key:")
# for k in mydict:
#     # print(k,mydict[k])
#     if key==k:
#         print(mydict[k])

# #随机生成验证码
# from random import Random
# def random_str(randomlength=16):
#     mystr = ''
#     strs = 'abcdefghijklmnopqrstuvwxyz0123456789'
#     length = len(strs) - 1
#     random = Random()
#     for i in range(randomlength):
#         mystr+=strs[random.randint(0, length)]
#     print("邀请码如下:")
#     print(mystr)
#     return mystr
# random_str()


# num=0
# for i in range(1,3):
#     num+=i
# print(num)

# number=0
# x = [0, 0, 1, 2, 5, 3, 0, 1, 8, 5]
# for i in x:
#     print(type(i))
#     number+=i
# print(number)

#随机生成验证码
# from random import Random
# def random_str(randomlength=16):
#     mystr = ''
#     strs = 'abcdefghijklmnopqrstuvwxyz0123456789'
#     length = len(strs) - 1
#     random = Random()
#     for i in range(randomlength):
#         mystr+=strs[random.randint(0, length)]
#     print("邀请码如下:")
#     print(mystr)
#     print(type(mystr[0]))
#     return mystr
#
# random_str()
# number=input("请输入数据:")
# data=int(number) % 10
# print(data)
# if data == 0:
#     print("ok")
# else:
#     print("error")

# x=1
# # b=-1
# # if b==x and b>0:
# #     print("哈哈")
# # else:
# #     print("嘿嘿")

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :游戏币组合.py
# @Time      :2020/6/7 21:22
# @Author    :青松


# def calculate_money(x):
#     # 金额
#     sum = 0
#     # 符合条件的组合次数
#     count = 0
#     # 循环次数
#     times = 0
#     # 硬币面额
#     mylist = [1, 5, 10, 20, 50, 100]
#
#     # 100元次数
#     for a in range(x // mylist[5] + 1):
#         # 50元次数
#         for b in range(x // mylist[4] + 1):
#             # 20元次数
#             for c in range(x // mylist[3] + 1):
#                 # 10元次数
#                 for d in range(x // mylist[2] + 1):
#                     # 5元次数
#                     for e in range(x // mylist[1] + 1):
#                         # #1元次数
#                         n = x - (a * mylist[5] + b * mylist[4] + c * mylist[3] + d * mylist[2] + e * mylist[1])
#                         sum = a * mylist[5] + b * mylist[4] + c * mylist[3] + d * mylist[2] + e * mylist[1] + n *mylist[0]
#                         if sum == x and n >= 0:
#                             count += 1
#     print("组合种类:", count)
#
# if __name__ == "__main__":
#     # 输入金额
#     money=input("请输入金额:")
#     calculate_money(int(money))


# ⼩明的抽屉⾥有n个游戏币，总⾯值m，游戏币的设置有1分的，2分的，5分的，10分的，⽽在⼩明
# 所拥有的游戏币中有些⾯值的游戏币可能没有，求⼀共有多少种可能的游戏币组合⽅式？
# 输⼊：输⼊两个数n(游戏币的个数)，m(总⾯值)。
# 输出：请输出可能的组合⽅式数；

# 有数学家发现⼀些两位数很有意思，⽐如，
# 34 * 86 = 43 * 68
# 也就是说，如果把他们的⼗位数和个位数交换，⼆者乘积不变。
# 编程求出满⾜该性质的两位数组合。
# 提示，暴⼒解法⾮最优解。

# 空桶的意义是说明：最大差值不可能是来自同一个桶内的两个数。
import sys


def max_difference(arr):
    max_num = -sys.maxsize  # 最大值取系统最小值
    min_num = sys.maxsize  # 最小值取系统最大值
    for i in arr:  # 循环arr数组中的每一个数
        max_num = max_num if i < max_num else i
        min_num = min_num if i > min_num else i
    bool_bucket = ["false"] * (len(arr) + 1)
    min_bucket = [None] * (len(arr) + 1)
    max_bucket = [None] * (len(arr) + 1)
    for i in arr:
        which = which_bucket(i, min_num, max_num, len(arr))
        if bool_bucket[which] == "false":
            min_bucket[which] = i
            max_bucket[which] = i
            bool_bucket[which] = "true"
        else:
            min_bucket[which] = min(min_bucket[which], i)
            max_bucket[which] = max(min_bucket[which], i)

    pre_max = max_bucket[0]
    ret = 0
    for i in range(1, len(arr) + 1):  # 从第二个桶开始
        if bool_bucket[i] == "true":  # 假设空桶就跳过，利用空桶下一个桶中最小值减去空桶上一个桶的最大值求差值。
            ret = max(ret, (min_bucket[i] - pre_max))
            pre_max = max_bucket[i]
    return ret


# 求数组中的数分配的桶号
def which_bucket(num, min_num, max_num, len):
    return int((num - min_num) * len / (max_num - min_num))


arr = [4, 3, 2, 1, 7]
print(max_difference(arr))
# 3  --> 7-4=3