T = int(input())

def merge(arr, a, mid, b):
    tmp = []
    i, j = a, mid + 1
    c = 0

    while i <= mid and j <= b:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1
        c += 1

    tmp.extend(arr[i:mid+1])
    tmp.extend(arr[j:b+1])

    arr[a:b+1] = tmp
    return c

def merge_sort(arr, a, b):
    if a >= b:
        return 0
    mid = (a + b) // 2
    c = merge_sort(arr, a, mid)
    c += merge_sort(arr, mid + 1, b)
    return c + merge(arr, a, mid, b)

for _ in range(T):
    arr = list(map(int, input().split()))[1:]
    print(merge_sort(arr, 0, len(arr) - 1))
