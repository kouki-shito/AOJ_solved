N,K = map(int,input().split())
W = [int(input()) for _ in range(N)]

def isOK(P):
    track_sum = 0
    w_index = 0

    for i in range(K):
        while w_index < N and track_sum + W[w_index] <= P:
            track_sum += W[w_index]
            w_index += 1
        if w_index == N:
            return True
        track_sum = 0

    return False

def bisect():
    
    l = 0
    r = sum(W)

    while l <= r:
        mid = (l + r) // 2
        if isOK(mid):
            r = mid - 1
        else:
            l = mid + 1
    print(l)

bisect()