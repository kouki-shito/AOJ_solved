N = int(input())
A = list(map(int,input().split()))

def countingSort(num:list) -> list:
    max_num = max(num)
    counts = [0] * (max_num + 1)
    results = [0] * len(num)

    for n in num:
        counts[n] += 1
    
    for i in range(1,len(counts)):
        counts[i] += counts[i-1]
    
    i = len(num) - 1
    while i >= 0:
        index = num[i]
        results[counts[index] - 1] = num[i]
        counts[index] -= 1
        i -= 1
    
    return results

print(*countingSort(A))