#!/usr/bin/env python
# coding=utf-8

n = int(input())
str = input().split()
num_list = [int(i) for i in str]
print(max(num_list) - min(num_list))
