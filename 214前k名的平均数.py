
n = int(input())
arr = list(map(int, input().split()))
k = int(input())

arr.sort(reverse = True)
sum = 0
for i in range(k):
    sum += arr[i]
print("%.2f" % (sum / k))
