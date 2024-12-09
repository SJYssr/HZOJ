#!/usr/bin/env python
# coding=utf-8

n = float(input())
sum = 0
for i in range(6):
    sum = (n + sum) * 1.00417
print('$%.2f' % sum)
