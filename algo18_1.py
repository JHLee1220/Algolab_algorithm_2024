import sys
sys.setrecursionlimit(10**6)

T = int(input())

def hoare(arr, l, h):
    pivot = arr[l]
    i = l - 1
    j = h + 1
    s = 0
    c = 0
    while True:
        i += 1
        while arr[i] < pivot:
            c += 1
            i += 1
        c += 1
        
        j -= 1
        while arr[j] > pivot:
            c += 1
            j -= 1
        c += 1
        
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            s += 1
        else:
            return j, s, c

def q_hoare(arr, l, h):
    s = c = 0
    if l < h:
        p, s1, c1 = hoare(arr, l, h)
        s += s1
        c += c1
        s2, c2 = q_hoare(arr, l, p)
        s3, c3 = q_hoare(arr, p + 1, h)
        s += s2 + s3
        c += c2 + c3
    return s, c

def lomuto(arr, l, h):
    pivot = arr[l]
    j = l
    s = 0
    c = 0
    for i in range(l + 1, h + 1):
        c += 1
        if arr[i] < pivot:
            j += 1
            arr[i], arr[j] = arr[j], arr[i]
            s += 1
    arr[l], arr[j] = arr[j], arr[l]
    s += 1
    return j, s, c

def q_lomuto(arr, l, h):
    s = c = 0
    if l < h:
        p, s1, c1 = lomuto(arr, l, h)
        s += s1
        c += c1
        s2, c2 = q_lomuto(arr, l, p - 1)
        s3, c3 = q_lomuto(arr, p + 1, h)
        s += s2 + s3
        c += c2 + c3
    return s, c

def quicksort(T, test_cases):
    results = []
    for case in test_cases:
        n, *arr = case
        
        arr_hoare = arr[:]
        hoare_s, hoare_c = q_hoare(arr_hoare, 0, n - 1)
        
        arr_lomuto = arr[:]
        lomuto_s, lomuto_c = q_lomuto(arr_lomuto, 0, n - 1)
        
        results.append(f"{hoare_s} {lomuto_s} {hoare_c} {lomuto_c}")
    
    return results

test_cases = [list(map(int, input().split())) for _ in range(T)]

results = quicksort(T, test_cases)
for result in results:
    print(result)