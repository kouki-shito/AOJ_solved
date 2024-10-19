import math
n = int(input())
A = [int(input()) for _ in range(n)]
res = 0
# 素数判定

def isOk(x) -> bool:
    if x == 2: # 2は素数
        return True
    if x < 2 or x % 2 == 0: # 偶数は除外
        return False

    i = 3
    
    while i <= math.sqrt(x): # 割る数は3から√xまででよい
        if x % i == 0:
            return False
        i = i + 2
    return True

for i in A:
    if isOk(i):
        res += 1

print(res)