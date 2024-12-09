#!/usr/bin/env python
# coding=utf-8

def find_elements_with_sum(arr, s):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == s:
            return arr[left], arr[right]
        elif current_sum < s:
            left += 1
        else:
            right -= 1
    return None

n = int(input())
arr = list(map(int, input().split()))
s = int(input())

result = find_elements_with_sum(arr, s)

if result is not None:
    print("Yes")
else:
    print("No")

