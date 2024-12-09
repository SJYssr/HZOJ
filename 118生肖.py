#!/usr/bin/env python
# coding=utf-8

year = int(input())

arr = ["rat", "ox", "tiger", "rabbit", "dragon", "snake", "horse", "sheep", "monkey",
       "rooster", "dog", "pig"]
print(arr[(year - 1900) % 12])
