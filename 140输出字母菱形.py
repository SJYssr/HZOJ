#!/usr/bin/env python
# coding=utf-8

def generate_diamond(n):
    start_char = ord('A')
    current_char = start_char
    # 上半部分菱形，逐行递增字母数量和减少空格数量
    for i in range(1, n + 1):
        spaces = " " * (n - i)  # 计算每行前的空格数量
        letters = chr(current_char) * (2 * i - 1)  # 计算每行的字母数量
        print(spaces + letters)
        current_char += 1

    # 下半部分菱形，逐行递减字母数量和增加空格数量
    current_char -= 2
    for i in range(n - 1, 0, -1):
        spaces = " " * (n - i)  # 计算每行前的空格数量
        letters = chr(current_char) * (2 * i - 1)  # 计算每行的字母数量
        print(spaces + letters)
        current_char -= 1

# 输入正整数n
n = int(input())
generate_diamond(n)
