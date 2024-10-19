T = int(input())

def gcd(a, b):
    while b != 0: #b가 0이 아닐 때까지 반복
        a, b = b, a % b #a는 b로, b는 a % b로 값을 교체
    return a   #b가 0이 되면 a가 최대 공약수

for _ in range(T):
    a, b = map(int, input().split())
    print(gcd(a, b))