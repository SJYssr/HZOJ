#!/usr/bin/env python
# coding=utf-8

def output(n):
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" " if j != 1 else "")
        print()

def main():
    n = int(input())
    output(n)

if __name__ == "__main__":
    main()

