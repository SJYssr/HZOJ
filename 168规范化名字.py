#!/usr/bin/env python
# coding=utf-8

n = int(input())
a = []

for i in range(n):
    word = input()
    if word[0].islower():
        word = word[0].upper() + word[1:]
    for j in range(1, len(word)):
        if word[j].isupper():
            word = word[:j] + word[j].lower() + word[j+1:]
    a.append(word)

a.sort()

for word in a:
    print(word)

