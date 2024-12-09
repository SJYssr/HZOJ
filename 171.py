def is_palindrome(num):
    return str(num) == str(num)[::-1]

def find_min_diff_palindrome(N):
    if is_palindrome(N):
        return N
    else:
        for i in range(N - 1, 0, -1):
            if is_palindrome(i):
                return i

N = int(input())
result = find_min_diff_palindrome(N)
print(result)