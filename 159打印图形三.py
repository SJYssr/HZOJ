#!/usr/bin/env python
# coding=utf-8

letter = input()
n = ord(letter) - ord('A')

for i in range(n, -1, -1):
    for j in range(n - i):
        print(" ", end="")

    for j in range(i, -1, -1):
        print(chr(ord('A') + j), end="")

    for j in range(i):
        print(chr(ord('A') + j), end="")

    print()

