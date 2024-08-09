import sys
N, M, K = map(int, sys.stdin.readline().split())
lists = [list(str(sys.stdin.readline().strip())) for i in range(N)]
num = 0
s, e, n = 0, 0, 0


for i in range(N):
    n = 0
    s = 0
    e = K-1
    for j in range(e):
        if(e>=M): break
        if(lists[i][j] == '0'):  
            n+=1

    while(e<M and s<M):
        if(lists[i][e] == '0'):  n+=1
        if(n == K) : num +=1
        if(lists[i][s] == '0'):  n-=1
        s+=1
        e+=1

print(num)
        