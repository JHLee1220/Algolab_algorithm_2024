T = int(input())

for _ in range(T):
    n = str(input())
    m = ''
    for char in n:
        m = char + m
        
    print(m)