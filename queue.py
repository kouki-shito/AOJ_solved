from collections import deque

N,Q = map(int,input().split())
res = []
times = 0
s = deque([])
for i in range(N):
    name, time = input().split()
    s.append((name,int(time))) #値の変更しないならtupleが便利

while len(s) != 0:
    tup = s.popleft()
    if tup[1] <= Q:
        times += tup[1]
        res.append((tup[0],times))
    else:
        times += Q
        s.append((tup[0],tup[1] - Q))

for i in res:
    print(i[0],i[1])