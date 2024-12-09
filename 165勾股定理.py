#!/usr/bin/env python
# coding=utf-8

import math

c = int(input())
cnt = 0

for a in range(1, c + 1):
    b = int(math.sqrt(c * c - a * a))
    if b < a:
        continue
    if a * a + b * b == c * c:
        cnt += 1

print(cnt)

