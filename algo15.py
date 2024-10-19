T = int(input())

def merge(arr, a, a2, a3):
    temp = arr[a:a3+1]
    i, j, k, c = a, a2 + 1, a, 0

    while i <= a2 and j <= a3:
        if temp[i-a] <= temp[j-a]:
            arr[k], i = temp[i-a], i + 1
        else:
            arr[k], j = temp[j-a], j + 1
        k, c = k + 1, c + 1

    arr[k:a3+1] = temp[i-a:a2-a+1] + temp[j-a:a3-a+1]
    return c

def merge_sort(arr, n):
    c, w = 0, 1
    while w < n:
        for i in range(0, n, 2*w):
            c += merge(arr, i, min(i+w-1, n-1), min(i+2*w-1, n-1))
        w *= 2
    return c

for _ in range(T):
    case = list(map(int, input().split()))
    print(merge_sort(case[1:], case[0]))
