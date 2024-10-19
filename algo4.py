T = int(input())

def kadane(arr):
    n = len(arr)
    
    # 배열의 길이가 1인 경우 바로 처리
    if n == 1:
        return (arr[0], 0, 0) if arr[0] > 0 else (0, -1, -1)
    
    # 첫 번째 요소로 최대합과 현재 합을 초기화
    ms = arr[0]
    cs = arr[0]
    bs = 0
    be = 0
    ts = 0
    
    for i in range(1, n):
        # 현재 구간 시작점이 0인 경우, 구간을 무시하고 새로 시작
        if cs <= 0 or arr[ts] == 0:
            cs = arr[i]
            ts = i
        else:
            cs += arr[i]
        
        # 최대합 갱신 조건: 먼저 시작 인덱스를 비교하고, 그 후 구간의 길이를 비교
        if (cs > ms or 
            (cs == ms and (ts < bs)) or 
            (cs == ms and (ts == bs and i - ts < be - bs))):
            # 시작 정수가 0인 구간은 선택하지 않음
            if arr[ts] != 0:
                ms = cs
                bs = ts
                be = i
    
    # 만약 최대합이 0 이하라면 최대합을 0으로 반환
    if ms <= 0:
        return 0, -1, -1
    return ms, bs, be

for _ in range(T):
    data = list(map(int, input().split()))
    n = data[0]
    arr = data[1:]
    result = kadane(arr)
    print(f"{result[0]} {result[1]} {result[2]}")
