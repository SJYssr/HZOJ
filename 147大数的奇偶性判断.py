#!/usr/bin/env python
# coding=utf-8

arr = input()
len_arr = len(arr)
result = "NO" if int(arr[len_arr - 1]) % 2 == 1 else "YES"
print(result)
