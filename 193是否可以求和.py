#!/usr/bin/env python
# coding=utf-8

def solve(n):
    arr = list(map(int, input().split()))
    k, s = map(int, input().split())
    if s - k in arr:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    while True:
        try:
            n = int(input())
            solve(n)
        except EOFError:
            break

