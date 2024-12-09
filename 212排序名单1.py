#!/usr/bin/env python
# coding=utf-8

# 创建一个空列表用于存储名字
names = []

# 读取输入的名字
for i in range(10):
    name = input()
    names.append(name)

# 对名字进行排序
names.sort()

# 输出排序后的名字
for name in names:
    print(name)

