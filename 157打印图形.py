#!/usr/bin/env python
# coding=utf-8

def main():
    n = int(input())

    for i in range(n):
        for j in range(i):
            print(" ", end="")

        for j in range(i, n):
            print(chr(ord('A') + j), end="")

        for j in range(n - 2, i - 1, -1):
            print(chr(ord('A') + j), end="")

        print()

    for i in range(n - 2, -1, -1):
        for j in range(i):
            print(" ", end="")

        for j in range(i, n):
            print(chr(ord('A') + j), end="")

        for j in range(n - 2, i - 1, -1):
            print(chr(ord('A') + j), end="")

        print()

if __name__ == "__main__":
    main()

