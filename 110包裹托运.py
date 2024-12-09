#!/usr/bin/env python
# coding=utf-8

x = float(input())
print('%.2f' % (x * 6 if x <= 15 else 15 * 6 + (x - 15) * 9))
