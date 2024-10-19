n = int(input())
R = [int(input()) for _ in range(n)]

##最大利益
minv = R[0]
maxv = -999999999999999999999
for i in range(1,n):
    maxv = max(maxv,R[i]- minv)
    minv = min(minv,R[i])
    
print(maxv)