#!/usr/bin/env python
# coding=utf-8

MAX_N = 1000000

prime = [0] * (MAX_N + 5)

def init_prime():
    for i in range(2, MAX_N + 1):
        if prime[i]:
            continue
        prime[0] += 1
        prime[prime[0]] = i
        for j in range(i, MAX_N // i + 1):
            prime[j * i] = 1

init_prime()

n, m = map(int, input().split())
for i in range(1, prime[0] + 1):
    if prime[i] <= n:
        if prime[i] < m:
            continue
        print(prime[i])

