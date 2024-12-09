#!/usr/bin/env python
# coding=utf-8

n = int(input())
m = 3
sum = 0

for i in range(n):
    m += 2 * i
    print(m)
    sum += m

print(sum)

