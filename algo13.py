def fibo(n):
    SIZE = 2
    MOD = 1000
    ZERO = [[1, 0], [0, 1]]
    BASE = [[1, 1], [1, 0]]
    
    def sq(a, b, size=SIZE, mod=MOD):
        new = [[0 for _ in range(size)] for _ in range(size)]
        for i in range(size):
            for j in range(size):
                for k in range(size):
                    new[i][j] = (new[i][j] + a[i][k] * b[k][j]) % mod
        return new
    
    def get(n):
        matrix = ZERO.copy()
        k = 0
        tmp = BASE.copy()
        
        while 2 ** k <= n:
            if n & (1 << k) != 0:
                matrix = sq(matrix, tmp)
            k += 1
            tmp = sq(tmp, tmp)
        
        return matrix
    
    if n == 0:
        return 0
    return get(n)[1][0]

t = int(input())
for _ in range(t):
    n = int(input())
    print(fibo(n))

