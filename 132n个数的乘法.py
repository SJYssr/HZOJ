#!/usr/bin/env python
# coding=utf-8

from functools import reduce

n = int(input())
str = input().split()
num_list = [int(i) for i in str]
result = reduce((lambda x, y: x * y), num_list)
print(result)
