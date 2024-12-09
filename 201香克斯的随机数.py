#!/usr/bin/env python
# coding=utf-8

n = int(input())
arr = set(map(int, input().split()))
arr = sorted(list(arr))
print(len(arr))
print(*arr)
