n = int(input())
G = [[0 for _ in range(n)] for _ in range(n)]
d = [0] * n
f = [0] * n
check = [False] * n

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

time = 0

def dfs(i):
    global time
    time += 1
    d[i] = time
    check[i] = True
    for j in range(n):
        if check[j] == False and G[i][j] == 1:
            dfs(j)
    time += 1
    f[i] = time

for i in range(n):
    if check[i]:
        continue
    dfs(i)

for i in range(n):
    print(i + 1,d[i],f[i])


