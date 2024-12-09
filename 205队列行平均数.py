#!/usr/bin/env python
# coding=utf-8

m, n = map(int, input().split())  # 输入行数和列数

for i in range(m):
    row = list(map(int, input().split()))  # 读取当前行的元素
    average = sum(row) / n  # 计算当前行的平均值
    print(f"{average:.6f}")

