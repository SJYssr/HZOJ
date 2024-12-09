#!/usr/bin/env python
# coding=utf-8

def output(s, n):
    for i in range(n):
        k = i * (n - 2)
        for j in range(n):
            print(s[(j + k) % n], end="")
        print()

str = input()
output(str, len(str))

