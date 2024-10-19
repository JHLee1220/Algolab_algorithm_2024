T = int(input())

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)
    
for _ in range(T):
    n = int(input())
    
    print(fibo(n))