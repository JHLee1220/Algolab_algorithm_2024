T = int(input())

def cross(arr, a, b, c):
    ls = float('-inf')
    sum = 0
    for i in range(b, a-1, -1):
        sum += arr[i]
        if sum > ls:
            ls = sum

    rs = float('-inf')
    sum = 0
    for i in range(b + 1, c + 1):
        sum += arr[i]
        if sum > rs:
            rs = sum

    return ls + rs

def sub(arr, a, c):
    if a == c:
        return arr[a]

    b = (a + c) // 2

    return max(
        sub(arr, a, b),
        sub(arr, b+1, c),
        cross(arr, a, b, c)
    )

for _ in range(T):
    arr = list(map(int, input().split()))[1:]
    print(max(0, sub(arr, 0, len(arr) - 1)))

