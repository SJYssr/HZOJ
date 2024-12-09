#!/usr/bin/env python
# coding=utf-8

def power(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        half_pow = power(x, n // 2)
        return half_pow * half_pow
    else:
        half_pow = power(x, (n - 1) // 2)
        return half_pow * half_pow * x

n = int(input())

result = power(2, n)
print(result)
