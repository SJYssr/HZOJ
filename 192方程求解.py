#!/usr/bin/env python
# coding=utf-8

import math

ESPL = 1e-5

def func(x):
    return x * math.exp(x)

def binary_search(f, l, r, x):
    head = l
    tail = r
    while tail - head > ESPL:
        mid = (head + tail) / 2
        if f(mid) > x:
            tail = mid
        else:
            head = mid
    return head

def solve(n):
    result = binary_search(func, 0, 20, n)
    print(f"{result:.4f}")

if __name__ == "__main__":
    while True:
        try:
            n = float(input())
            solve(n)
        except EOFError:
            break

