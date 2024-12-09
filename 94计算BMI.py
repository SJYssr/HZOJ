#!/usr/bin/env python
# coding=utf-8

w, h = input().split(' ')
w = float(w)
h = float(h)
BMI = w / (h * h)
print("%.2f" % BMI)
