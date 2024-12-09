#!/usr/bin/env python
# coding=utf-8

def solve(x):
    fib = [0, 1]
    n = 1
    while n < x:
        n += 1
        fib[n % 2] = (fib[(n - 1) % 2] + fib[(n - 2) % 2]) % (10**9 + 7)
    print(fib[x % 2])

if __name__ == "__main__":
    while True:
        try:
            n = int(input())
            solve(n)
        except EOFError:
            break

