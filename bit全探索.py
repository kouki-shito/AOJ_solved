N = int(input())
A = list(map(int,input().split()))
Q = int(input())
M = list(map(int,input().split()))
# bit全探索
# Aで作れる和の全パターンをsetに詰める
sets = set()
for bit in range(1,1 << N):
    tmp = 0
    for i in range(N):
        if (bit >> i) & 1:
            tmp += A[i]
    sets.add(tmp)
for i in range(Q):
    if M[i] in sets:
        print("yes")
    else:
        print("no")