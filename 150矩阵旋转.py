#!/usr/bin/env python
# coding=utf-8

m, n = map(int, input().split())

arr = []
for i in range(m):
    row = list(map(int, input().split()))
    arr.append(row)

for i in range(n):
    for j in range(m - 1, -1, -1):
        print(arr[j][i], end="")
        if j > 0:
            print(" ", end="")
    print()

