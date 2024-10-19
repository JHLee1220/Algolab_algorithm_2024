T = int(input())

def s_sort(array):
    n = len(array)
    
    count_ops = 0
    count_swap = 0
    
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            count_ops += 1
            if array[j] < array[min]:
                min = j
        if min != i:
            array[i], array[min] = array[min], array[i]
            count_swap += 1
            
    return count_ops, count_swap

for _ in range(T):
    data = list(map(int, input().split()))
    n = data[0]
    array = data[1:]
    
    count_ops, count_swap = s_sort(array)
    
    print(f"{count_ops} {count_swap}")