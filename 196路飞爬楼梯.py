#!/usr/bin/env python
# coding=utf-8

def solve(n):
    if n < 2:
        return 0
    if n == 2 or n == 3:
        return 1
    return solve(n - 2) + solve(n - 3)

if __name__ == "__main__":
    n = int(input())
    result = solve(n)
    print(result)

