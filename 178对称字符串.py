#!/usr/bin/env python
# coding=utf-8

def output(n):
    if n == 1:
        print('A', end='')
        return
    output(n - 1)
    print(chr(ord('A') + n - 1), end='')
    output(n - 1)

n = int(input())
output(n)
print()

