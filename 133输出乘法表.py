#!/usr/bin/env python
# coding=utf-8

# 获取用户输入的整数n
n = int(input())

# 遍历从1到n的所有整数i
for i in range(1, n + 1):
    # 创建一个空字符串x_str，用于存储当前行的乘法表达式
    x_str = ""

    # 遍历从i到n的所有整数j
    for j in range(i, n + 1):
        # 将当前的乘法表达式添加到x_str中，形式为"i*j=i*j的结果"
        x_str += str(i) + '*' + str(j) + '=' + str(i * j) + '\t'

    # 去掉x_str末尾的制表符'\t'
    x_str = x_str[:-1]

    # 打印出x_str，即当前行的乘法表达式
    print(x_str)
