n = int(input())
G = [[0 for _ in range(n)] for _ in range(n)]

def add_graph(u,v,k):
    if k != 0:
        for i in v:
            G[u - 1][i - 1] = 1

for i in range(n):
    data = list(map(int,input().split()))
    u = data[0]
    k = data[1]
    v = data[2:]
    add_graph(u,v,k)

for i in G:
    print(*i)