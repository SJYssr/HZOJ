#!/usr/bin/env python
# coding=utf-8
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_sqrt(n):
    x = int(math.sqrt(n))
    return x * x == n

def check(n):
    return is_prime(n) and is_sqrt(n // 100) and is_sqrt(n % 100)

a, b = map(int, input().split())
flag = 0

for i in range(a, b + 1):
    if not check(i):
        continue
    if flag > 0:
        print(" ", end="")
    print(i, end="")
    flag += 1

print()
print(flag)

