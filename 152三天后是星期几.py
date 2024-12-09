#!/usr/bin/env python
# coding=utf-8

week = [
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
    "Sunday"
]

n = int(input())
print(week[(n + 2) % 7])
