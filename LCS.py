def solve(r,c) -> int:
    dp = [[0 for _ in range(len(c) + 1)] for _ in range(len(r) + 1)]
    for i in range(len(r)):
        for j in range(len(c)):
            if r[i] == c[j]: # 1からにしているから補正
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1],dp[i + 1][j])
    return dp[len(r)][len(c)]

n = int(input())
for i in range(n):
    R = input()
    C = input()
    print(solve(R,C))
    
# PyPyでないとTLE

#[ [for 列]  for 行]!!