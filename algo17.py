T = int(input())

def hanoi(n, start, end, temp, result, tower3):
    if n == 0:
        return
    # n-1개의 디스크를 temp 기둥으로 이동
    hanoi(n-1, start, temp, end, result, tower3)
    
    # 가장 큰 디스크를 end 기둥으로 이동
    if end == 3:
        result.append(n)
        tower3.append(n)  # 3번 기둥에 디스크 추가
    elif start == 3:
        tower3.pop()  # 3번 기둥에서 디스크 제거
        if len(tower3) == 0:  # 3번 기둥이 비었을 경우에만 0 출력
            result.append(0)
        else:
            result.append(tower3[-1])  # 3번 기둥에 남은 디스크의 번호 출력

    # n-1개의 디스크를 end 기둥으로 이동
    hanoi(n-1, temp, end, start, result, tower3)

def solve(t):
    for n in t:
        result = []
        tower3 = []  # 3번 기둥의 상태를 추적하는 리스트
        hanoi(n, 1, 3, 2, result, tower3)
        print(" ".join(map(str, result)))

# 입력 받기
t = [int(input()) for _ in range(T)]

# 결과 출력
solve(t)