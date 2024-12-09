#!/usr/bin/env python
# coding=utf-8

def output(h, m, s, t):
    t1 = t + h * 3600 + m * 60 + s
    h = t1 // 3600 % 24
    m = t1 % 3600 // 60
    s = t1 % 60
    h1 = 12 if h == 0 or h == 12 else h % 12
    time_period = "am" if h < 12 else "pm"

    print(f"{h1:d}:{m:d}:{s:d}{time_period}")

    rate = t * 1.0 / 86400 * 100
    print(f"{rate:.2f}%")

def main():
    h, m, s, t = map(int, input().split())
    output(h, m, s, t)

if __name__ == "__main__":
    main()

