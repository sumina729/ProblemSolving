import sys
import math

N = int(sys.stdin.readline())
num = []
is_stop = False
def dfs(n):
    global is_stop

    if(n == N): 
        for i in range(N):
            print(num[i], end="")
        is_stop = True
        return
    
    for i in range(1, 4):

        if(is_stop) : break

        num.append(i)
        m = (n+1)//2
        is_dfs = True
        for j in range(m):
            if num[n-j:n+1] == num[n-j-j-1:n-j] : 
                #print(num[n-j:n+1], num[n-j-j-1:n-j])
                is_dfs = False
        if is_dfs : dfs(n+1)
        num.pop()
dfs(0)