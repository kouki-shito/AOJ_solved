N = int(input())
A = list(input().split())

def bubble(x:list) -> list:
    for i in range(len(x)):
        for j in range(len(x) - 1 - i):
            if int(x[j][1:]) > int(x[j + 1][1:]):
                x[j],x[j + 1] = x[j + 1],x[j]
    return x

def selection(x:list) -> list:
    for i in range(len(x)):
        min_idx = i
        for j in range(i + 1,len(x)):
            if int(x[j][1:]) < int(x[min_idx][1:]):
                min_idx = j
        x[i],x[min_idx] = x[min_idx],x[i]
    return x
B = bubble(A[:])
S = selection(A[:])
print(*B)
print("Stable") # bubbleは常に安定ソート
print(*S)
if B == S:
    print("Stable")
else:
    print("Not stable")