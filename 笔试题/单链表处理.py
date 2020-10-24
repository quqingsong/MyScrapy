#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :单链表处理.py
# @Time      :2020/6/8 5:43
# @Author    :青松
 
class SingleNode(object):
    """单链表的结点"""
    def __init__(self,item):
        # item存放数据元素
        self.item = item
        # next是下一个节点的标识
        self.next = None
class SingleLinkList(object):

    def __init__(self):
        self.__head = None

    def is_empty(self):
        '''判断链表是否为空'''
        return self.__head == None

    def length(self):
        '''链表长度'''
        # cur初始时指向头节点
        cur = self.__head
        count = 0
        # 当到达尾部时，尾节点指向None
        while cur != None:
            count += 1
            # 把cur后移一个节点
            cur = cur.next
        # 返回数量
        return count

    def travel(self):
        '''遍历链表'''
        cur = self.__head
        # 只要未到达末尾，也就是cur未指向None
        while cur != None:
            print(cur.item)
            # cur指向下一个节点
            cur = cur.next

        print("")

    def add(self, item):
        '''头部添加元素'''
        # 首先创建保存item值的节点
        node = SingleNode(item)
        # 将新节点的链接域next指向头节点，即__head指向的位置
        node.next = self.__head
        # 将链表的头__head指向新节点
        self.__head = node

    def append(self, item):
        '''尾部添加元素'''
        # 创建要添加的元素node
        node = SingleNode(item)
        # 首先判断链表是否为空，如果是空，则将__head指向新节点
        if self.is_empty():
            self.__head = node

        # 如果不为空，则将尾节点的next指向新节点
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        '''指定位置添加元素'''

        # 如果指定位置pos为第一个元素之前，则执行头部插入
        if pos <= 0:
            self.add(item)

        # 如果指定位置pos为最后一个元素之后，则执行尾部插入
        elif pos > (self.length() - 1):
            self.append(item)

        else:
            # 指定位置插入
            # 创建新元素
            node = SingleNode(item)

            count = 0
            # pre用来指向指定位置pos的前一个位置pos-1，初始从头节点移动到该位置
            pre = self.__head
            while count < (pos - 1):
                count += 1
                pre = pre.next

            # 先将新节点node的next指向插入位置的节点
            node.next = pre.next
            # 将插入位置的前一个节点的next指向新节点
            pre.next = node

    def remove(self, item):
        '''删除节点'''

        cur = self.__head
        pre = None
        while cur != None:
            # 找到了要删除的元素

            if cur.item == item:
                # 如果第一个元素就是要删除的节点
                if not pre:
                    # 将头指针指向头节点的后一个节点
                    self.__head = cur.next
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                break
            else:
                # 未找到要删除的元素.继续向后移动节点
                pre = cur
                cur = cur.next

    def search(self, item):
        '''查找节点是否存在，返回True或False'''
        cur = self.__head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next

        return False


if __name__=="__main__":
    pass