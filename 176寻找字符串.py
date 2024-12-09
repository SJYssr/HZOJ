#!/usr/bin/env python
# coding=utf-8

s1 = input()
s2 = input()
count = 0
pos = 0

while True:
    pos = s1.find(s2, pos)
    if pos != -1:
        pos += 1
        count += 1
    else:
        break

print(count)

