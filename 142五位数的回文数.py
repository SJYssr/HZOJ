#!/usr/bin/env python
# coding=utf-8

import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def reverse(n):
    x_str = str(n)
    return x_str == x_str[::-1]

a, b = map(int, input().split())
x_str = ""
for i in range(a, b + 1):
    if is_prime(i) == False or reverse(i) == False: continue
    x_str += str(i) + ' '
x_str = x_str[:-1]
print(x_str)
