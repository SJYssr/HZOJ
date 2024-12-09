#!/usr/bin/env python
# coding=utf-8

n = int(input())  # 输入同学的数量
heights = list(map(int, input().split()))  # 输入同学的身高

# 创建一个包含同学编号和身高的元组的列表
students = [(i, h) for i, h in enumerate(heights, 1)]

# 按照身高从小到大排序，如果身高相同则按照编号从小到大排序
sorted_students = sorted(students, key=lambda x: (x[1], x[0]))

# 输出排序后的同学编号
sorted_ids = [student[0] for student in sorted_students]
print(" ".join(map(str, sorted_ids)))

