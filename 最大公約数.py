a,b = map(int,input().split())

x = max(a,b)
y = min(a,b)

## 最大公約数 ユークリッドの互除法
while y > 0:
    r = x % y
    x = y
    y = r

print(x)
