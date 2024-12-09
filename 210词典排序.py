#!/usr/bin/env python
# coding=utf-8

n = int(input())  # 输入字符串的数量

strings = list(input().split())

strings.sort()  # 对字符串列表进行升序排序

print(" ".join(strings))  # 使用空格将排序后的字符串连接并打印
