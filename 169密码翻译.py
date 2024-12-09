#!/usr/bin/env python
# coding=utf-8

n = int(input())
num = [0] * 128

for i in range(n):
    a = input()
    b = input()
    num[ord(a)] = int(b)

str = input()
ans = 0

for char in str:
    ans += num[ord(char)]

print(ans)

