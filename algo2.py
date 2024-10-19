T = int(input())

def fac(n):
    if n == 0:
        return 1
    a = 1
    for i in range(2, n + 1):
        a *= i
    return a

def last(n):
    while n % 10 == 0:
        n //= 10
    return str(n)[-3:]

for _ in range(T):
    n = int(input())
    fl = fac(n)
    print(last(fl))