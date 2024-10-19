N = int(input())
A = list(map(int,input().split()))
res = 0
for i in range(len(A)):
    min_idx = i
    for j in range(i + 1, len(A)):
        if A[j] < A[min_idx]:
            min_idx = j
    if min_idx != i:
        res += 1    
    A[i], A[min_idx] = A[min_idx],A[i]

print(' '.join(map(str,A)))
print(res)