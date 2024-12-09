#!/usr/bin/env python
# coding=utf-8

name = []

for i in range(10):
    name.append(input())

name.sort()

for i in range(10):
    print(name[i])
