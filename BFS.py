from collections import deque


n = int(input())
G = [None] * n

for i in range(n):
    data = list(map(int,input().split()))
    u = data[0]
    k = data[1]
    vs = data[2:]
    G[u-1] = [v-1 for v in vs] # 0始まりなので-1

print(G)
dist = [-1] * n
que = deque([0])
dist[0] = 0

while que:
    v = que.popleft()
    d = dist[v]
    for c in G[v]:
        if dist[c] > -1:
            continue
        dist[c] = d + 1
        que.append(c)     

for i in range(n):
    print(i + 1,dist[i])