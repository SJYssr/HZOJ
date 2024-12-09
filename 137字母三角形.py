#!/usr/bin/env python
# coding=utf-8

def generate_triangle(n):
    start_char = ord('A')
    current_char = start_char
    for i in range(n):
        for j in range(n - i):
            print(chr(current_char), end="")
            current_char += 1
        print()

n = int(input())
generate_triangle(n)