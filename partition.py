N = int(input())
A = list(map(int,input().split()))

def partition(A,p,r):
    x = A[r]
    i = p - 1
    
    for j in range(p,r):
        if A[j] <= x:
            i = i + 1
            A[i],A[j] = A[j],A[i]
    A[i + 1],A[r] = A[r],A[i + 1]
    
    return i + 1

left = 0
right = len(A) - 1

q = partition(A,left,right)
A[q] = "[{}]".format(A[q]) 

print(*A)

