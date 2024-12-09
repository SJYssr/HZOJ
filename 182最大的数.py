#!/usr/bin/env python
# coding=utf-8

n = int(input())
x_str = input().split()
print(max(x_str, key = lambda x: int(x)))
