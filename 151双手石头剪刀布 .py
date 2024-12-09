#!/usr/bin/env python
# coding=utf-8

def init():
    status = [[0] * 26 for _ in range(26)]
    status[ord('Y') - ord('A')][ord('O') - ord('A')] = -1
    status[ord('Y') - ord('A')][ord('H') - ord('A')] = 1
    status[ord('O') - ord('A')][ord('Y') - ord('A')] = 1
    status[ord('O') - ord('A')][ord('H') - ord('A')] = -1
    status[ord('H') - ord('A')][ord('Y') - ord('A')] = -1
    status[ord('H') - ord('A')][ord('O') - ord('A')] = 1
    return status

def check_win(a1, a2, b1, b2, status):
    m1 = ord(a1) - ord('A')
    m2 = ord(a2) - ord('A')
    n1 = ord(b1) - ord('A')
    n2 = ord(b2) - ord('A')

    if status[m1][n1] == 1:
        if status[m1][n2] >= 0:
            return 1
        else:
            if status[m2][n2] > 0:
                return 1
            else:
                return 2
    elif status[m1][n1] == 0:
        if status[m2][n2] > 0:
            return 1
        elif status[m2][n2] < 0:
            return 2
        else:
            return 0
    else:
        if status[m2][n1] <= 0:
            return 2
        else:
            if status[m2][n2] >= 0:
                return 1
            else:
                return 2

ans = ["TIE", "MING", "LIHUA"]
status = init()

a_input = input().split()
b_input = input().split()

a_left, a_right = a_input[0], a_input[1]
b_left, b_right = b_input[0], b_input[1]

ret = check_win(a_left, a_right, b_left, b_right, status)
print(ans[ret])

