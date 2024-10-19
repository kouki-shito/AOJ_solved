N = int(input())
S = list(map(int,input().split()))
res = 0

def mergeSort(num:list) -> list:
    global res
    if len(num) <= 1:
        return num
    
    center = len(num) // 2
    left = num[:center]
    right = num[center:]
    
    mergeSort(left)
    mergeSort(right)
    
    i = j = k = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            num[k] = left[i]
            i += 1
        else:
            num[k] = right[j]
            j += 1
        k += 1
        res += 1
    
    while i < len(left):
        num[k] = left[i]
        i += 1
        k += 1
        res += 1
    
    while j < len(right):
        num[k] = right[j]
        j += 1
        k += 1
        res += 1
    
    return num

print(*mergeSort(S))
print(res)