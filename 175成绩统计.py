#!/usr/bin/env python
# coding=utf-8

def check(arr, temp):
    if 0 <= temp < 60:
        arr[3] += 1
    elif temp < 80:
        arr[2] += 1
    elif temp < 90:
        arr[1] += 1
    elif 90 <= temp <= 100:
        arr[0] += 1

n = int(input())
arr = [0] * 4
x_str = input().split()
for i in x_str:
    check(arr, int(i))

print("You", arr[0])
print("Liang", arr[1])
print("Zhong", arr[2])
print("Cha", arr[3])
