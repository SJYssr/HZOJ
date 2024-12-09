#!/usr/bin/env python
# coding=utf-8

EPSILON = 1e-7

def bisection(p, q, func):
    head = -20
    tail = 20
    mid = 0

    while True:
        mid = (head + tail) / 2
        if func(p, q, head) * func(p, q, mid) < 0:
            tail = mid
        else:
            head = mid
        if abs(func(p, q, mid)) <= EPSILON:
            break

    return mid

def f(p, q, x):
    return p * x + q

p, q = map(int, input().split())
result = bisection(p, q, f)
print(f"{result:.4f}")
