#!/usr/bin/env python
# coding=utf-8

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a + b <= c:
    print("illegal triangle")
elif a * a + b * b > c * c:
    print("acute triangle")
elif a * a + b * b == c * c:
    print("right triangle")
elif a * a + b * b < c * c:
    print("obtuse triangle")
