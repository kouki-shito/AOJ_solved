memo = {} # メモ化再帰処理

def fib(n:int) -> int:

    if n in memo:
        return memo[n]

    if n == 0 or n == 1:
        memo[n] = 1
        return memo[n]
    else:
        memo[n] = fib(n-1) + fib(n-2) 
        return memo[n]

N = int(input())
print(fib(N))