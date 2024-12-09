#!/usr/bin/env python
# coding=utf-8

n = int(input())
str = input().split()
sum = 0
for i in range(n):
    sum += int(str[i])
print('%.2f' % (sum / n))
