import sys

##わからん。
def maxHeapify(i):
    l = i * 2
    r = i * 2 + 1
    if l <= N and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= N and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i],A[largest] = A[largest],A[i]
        maxHeapify(largest)

def buildMaxHeap():
    for i in range(N//2,0,-1):
        maxHeapify(i)

N = int(input())
A = [-1 * sys.maxsize] + list(map(int,input().split()))
buildMaxHeap()
print("",*A[1:])