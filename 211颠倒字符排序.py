#!/usr/bin/env python
# coding=utf-8

n = int(input())  # 输入字符串的数量
names = []  # 创建一个空列表用于存储字符串

for i in range(n):
    s = input()
    reversed_s = s[::-1]  # 反转字符串
    names.append(reversed_s)

names.sort()  # 对反转后的字符串列表进行升序排序

for name in names:
    print(name)  # 逐行打印排序后的字符串

