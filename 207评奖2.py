#!/usr/bin/env python
# coding=utf-8

def main():
    n = int(input())
    students = []

    max_total = 0
    max_student = None
    min_score = 100
    max_score = 0

    for _ in range(n):
        name = input()
        scores = list(map(int, input().split()))
        total = sum(scores)

        if total > max_total:
            max_total = total
            max_student = name

        students.append({
            'name': name,
            'scores': scores,
            'total': total
        })

        for score in scores:
            if score < min_score:
                min_score = score
            if score > max_score:
                max_score = score

    for student in students:
        print(student['total'])

    print(max_student)
    print(max_score, min_score)

if __name__ == "__main__":
    main()

