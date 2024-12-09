#!/usr/bin/env python
# coding=utf-8

n = int(input())
ans = ""

for i in range(n):
    str_input = input()
    temp_len = len(str_input)
    if temp_len <= len(ans):
        continue
    ans = str_input

print(ans)

