T = int(input())

MOD = 1000

def fex(a, n, mod = MOD):  
    if n == 0:
        return 1
    elif n % 2 == 0:
        half = fex(a, n // 2)
        return half * half % mod
    else:
        half = fex(a, (n - 1) // 2)
        return a * half * half % mod

for _ in range(T):
    a, n = map(int, input().split())
    print(fex(a, n))