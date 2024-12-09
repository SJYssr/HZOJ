#!/usr/bin/env python
# coding=utf-8

import math

r, h = map(float, input().split())
s = math.sqrt(8 * r * r)
result = (5.14 * r + s) * h + 7.14 * r * r
print("%.2f" % result)

