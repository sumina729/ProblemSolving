import sys
N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
count = 0

def dfs(idx, number):
    global count
    if(idx==N) : return

    for i in range(idx, N):
        if number+numbers[i] == M : 
            count+=1
        dfs(i+1, number+numbers[i])

    
dfs(0, 0)
print(count)