#!/usr/bin/env python
# coding=utf-8

x = input()
dict = {'h':"He", 'l':"Li", 'c':"Cao", 'd':"Duan", 'w':"Wang"}
print(dict[x] if x in dict else "Not Here")
