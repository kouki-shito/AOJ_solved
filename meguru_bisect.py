N = int(input())
S = list(map(int,input().split()))
Q = int(input())
T = list(map(int,input().split()))
res = 0

def isOK(A:list,index:int,key:int) -> bool:
    if A[index] <= key:
        return True
    else:
        return False

def meguru_bisect(A:list,key:int) -> bool:
    ok = -1
    ng =  len(A)

    while abs(ng - ok) > 1:
        mid = (ok + ng) // 2
        if isOK(A,mid,key):
            ok = mid
        else:
            ng = mid
    return A[ok] == key

for i in T:
    if meguru_bisect(S,i):
        res += 1
print(res)
