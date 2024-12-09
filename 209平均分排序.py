n = int(input())
arr_list = input().split()
arr_list.sort(key=float)
for i in arr_list:
    print(i)