#!/usr/bin/env python
# coding=utf-8

n, m = map(int, input().split())
cnt = n // m
print(cnt + 1 if n % m != 0 else cnt)
