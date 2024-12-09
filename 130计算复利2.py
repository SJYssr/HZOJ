#!/usr/bin/env python
# coding=utf-8

n, m = map(int, input().split())
sum = 0
for i in range(m):
    sum = (n + sum) * 1.00417
print('$%.2f' % sum)
