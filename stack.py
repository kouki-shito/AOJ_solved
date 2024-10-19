from collections import deque

## 逆ポーランド記法

s = deque([])
A = list(input().split())

for i in A:
    if i == '+':
        R = int(s.pop())
        L = int(s.pop())
        s.append(L + R)
    elif i == '-':
        R = int(s.pop())
        L = int(s.pop())
        s.append(L - R)
    elif i == '*':
        R = int(s.pop())
        L = int(s.pop())
        s.append(L * R)
    else:
        s.append(int(i))
print(s.pop())
