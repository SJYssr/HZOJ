#!/usr/bin/env python
# coding=utf-8

n = int(input())
num = []

for i in range(n):
    num.append(input())

for i in range(n):
    pos = num[i].find("Ban")
    while pos != -1:
        num[i] = num[i][:pos] + "No" + num[i][pos + 3:]
        pos = num[i].find("Ban", pos + 2)

for i in range(n):
    print(num[i])
