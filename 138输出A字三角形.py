#!/usr/bin/env python
# coding=utf-8

def generate_triangle(n):
    for i in range(n, 0, -1):  # 从n递减到1，控制行数
        print("A" * (2 * i))  # 打印每行的字母A

# 输入正整数n
n = int(input())
generate_triangle(n)
