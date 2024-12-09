#!/usr/bin/env python
# coding=utf-8

n = int(input())
sum = 0
while n:
    sum += n % 10;
    n //= 10
print(sum)
