#!/usr/bin/env python
# coding=utf-8

n, m = map(int, input().split())  # 输入行数和列数
arr = [0] * m  # 创建一个长度为m的数组，用于存储每列的和

for i in range(n):
    row = list(map(int, input().split()))  # 读取当前行的元素
    for j in range(m):
        arr[j] += row[j]  # 将当前行的元素加到相应列的和上

for column_sum in arr:
    print(column_sum)

