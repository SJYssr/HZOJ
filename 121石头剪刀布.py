#!/usr/bin/env python
# coding=utf-8

a, b = input().split()
if a == b:
    print('TIE')
elif (a == 'O' and b == 'Y') or (a == 'Y' and b == 'H') or (a == 'H' and b == 'O'):
    print('MING')
else:
    print("LI")

