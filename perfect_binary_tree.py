import sys

n = int(input())
heap = list(map(int,input().split()))

## left,right,parentはvalue表示なのに注意
for i,node in enumerate(heap,start = 1):
    print(f"node {i}: key = {node}, ", end = '')
    if i // 2 != 0:
        print(f"parent key = {heap[i//2 -1]}, ", end = '') # start = 1の対応
    if 2 * i <= n:
        print(f"left key = {heap[2*i -1]}, ", end = '')
    if 2 * i + 1 <= n:
        print(f"right key = {heap[2*i]},", end = '')
    print()