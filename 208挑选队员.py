#!/usr/bin/env python
# coding=utf-8

n = int(input())  # 输入整数数组的长度
v = []
for i in range(n):
    v.append(int(input()))

v.sort(reverse=True)  # 按降序排序整数数组

m = int(input())  # 输入连续出现次数的阈值

cnt = 1
for i in range(1, len(v)):
    if v[i] != v[i - 1]:
        if cnt >= m:
            print(cnt)
            break
        cnt = 1
    else:
        cnt += 1
else:
    if cnt >= m:
        print(cnt)
    else:
        print(0)  # 如果没有满足阈值的连续出现次数，输出0

