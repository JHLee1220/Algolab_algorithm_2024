T = int(input())

def i_sort(array):
    n = len(array)
    
    count_ops = 0
    count_insert = 0
    
    for i in range(1, n):
        value = array[i]
        j = i - 1
        while j >= 0 and array[j] > value:
            count_ops += 1
            array[j + 1] = array[j]
            j -= 1
            count_insert += 1
        if j >= 0:
            count_ops += 1
        array[j + 1] = value
                             
    return count_ops, count_insert
            

for _ in range(T):
    data = list(map(int, input().split()))
    n = data[0]
    array = data[1:]
    
    count_ops, count_insert = i_sort(array)
    
    print(f"{count_ops} {count_insert}")