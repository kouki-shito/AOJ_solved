## bubble sort
def bubble(x:list) -> list:
    for i in range(len(x)):
        for j in range(len(x) - 1 - i):
            if int(x[j]) > int(x[j + 1]):
                x[j],x[j + 1] = x[j + 1],x[j]
    return x

## selection sort

def selection(x:list) -> list:
    for i in range(len(x)):
        min_idx = i
        for j in range(i + 1,len(x)):
            if int(x[j]) < int(x[min_idx]):
                min_idx = j
        x[i],x[min_idx] = x[min_idx],x[i]
    return x

## insetion

def insertion(x:list) -> list:
    for i in range(1,len(x)):
        temp = x[i]
        j = i - 1
        while j >= 0 and x[j] > temp: ##降順の際は x[j] < tempでOK
            x[j + 1] = x[j]
            j -= 1
        x[j + 1] = temp
    return x
