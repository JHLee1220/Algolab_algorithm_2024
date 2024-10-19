T = int(input())

def gen(s): #순열을 구하는 재귀 함수
    if len(s) == 1:
        return [s]
    
    p = []
    for i, ch in enumerate(s): #재귀적으로 순열 생성
        sub = gen(s[:i] + s[i + 1:])
        
        for pe in sub:
            p.append(ch + pe)
            
    return p

def ws(s): #가중치를 계산하는 함수
    w = 0
    for j, ch in enumerate(s):
        w += ((-1) ** j) * (ord(ch) - ord('a')) #ord함수 : 문자의 아스키 값을 반환해주는 함수
    return w

def cws(s): #양수 가중치를 가진 순열의 개수를 계산하는 함수
    c = 0
    
    pe = gen(s) #순열 생성
    for k in pe: 
        if ws(k) > 0: #순열의 가중치를 계산, 양수면 c 에 +1를 한다.
            c += 1
    return c

for _ in range(T):
    s = input().strip() #문자열 입력
    result = cws(s)
    print(result)