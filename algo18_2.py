import sys
sys.setrecursionlimit(10**6) #10^3 에서 10^6으로, 재귀 한도 늘리기

T = int(input()) #입력받기

def partition(arr, l, h, scheme): #배열 arr의 구간 [i, h]을 피벗을 기준으로 나누는 함수
    #arr:분할할 배열, l:분할할 구간의 시작 인덱스, h:구간의 끝 인덱스, scheme:분할 방식
    pivot = arr[l]
    i, j = l, h
    s = c = 0 #s는 교환 횟수, c는 비교 횟수를 추적한다.
    #Hoare 방식
    if scheme == 'hoare':
        i -= 1
        j += 1
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
    #Lomuto방식
    else:
        for k in range(l + 1, h + 1):
            c += 1
            if arr[k] < pivot: #arr[k] < pivot 이면 i를 증가시키고 arr[i], arr[k]의 값을 교환한다.
                i += 1
                arr[i], arr[k] = arr[k], arr[i]
                s += 1
        arr[l], arr[i] = arr[i], arr[l] #피벗을 i위치로 이동시킨다.
        s += 1
        return i, s, c 

def quicksort(arr, l, h, scheme): #주어진 배열을 재귀적으로 정렬
    s = c = 0
    if l < h:
        p, s1, c1 = partition(arr, l, h, scheme)
        s += s1
        c += c1
        s2, c2 = quicksort(arr, l, p - (scheme == 'lomuto'), scheme)
        s3, c3 = quicksort(arr, p + 1, h, scheme)
        s += s2 + s3
        c += c2 + c3
    return s, c

def process(T, test_cases): #T개의 테스트 케이스를 처리
    results = []
    for case in test_cases:
        n, *arr = case
        arr_hoare = arr[:]
        arr_lomuto = arr[:]
        
        hoare_s, hoare_c = quicksort(arr_hoare, 0, n - 1, 'hoare')
        lomuto_s, lomuto_c = quicksort(arr_lomuto, 0, n - 1, 'lomuto')
        
        results.append(f"{hoare_s} {lomuto_s} {hoare_c} {lomuto_c}")
    
    return results

test_cases = [list(map(int, input().split())) for _ in range(T)] #각 테스트 케이스를 리스트로 변환하여 test_cases에 저장한다.
results = process(T, test_cases)

for result in results:
    print(result)