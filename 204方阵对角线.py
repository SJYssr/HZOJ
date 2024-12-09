n = int(input())
arr_list =[]
for i in range(n):
    x_str = input().split()
    arr_list.append(x_str)
for i in range(n):
    print(arr_list[i][i])