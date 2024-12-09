#!/usr/bin/env python
# coding=utf-8

pi = 3.14
r1, r2 = map(float, input().split())
print('%.2f' % (pi * r1 * r1 - pi * r2 * r2))
