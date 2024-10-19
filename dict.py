from collections import defaultdict

N = int(input())
dic = defaultdict(int) 
for i in range(N):
    com,strs = input().split()
    if com == "insert":
       dic[strs] = 999
    elif com == "find":
        if dic[strs] == 999: # inでも可
            print("yes")
        else:
            print("no")
