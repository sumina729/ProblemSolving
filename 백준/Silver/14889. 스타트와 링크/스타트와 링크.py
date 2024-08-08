def dfs(n, idx):
    global min_num
    if n==N//2:
        a = 0
        b = 0
        for i in range(N): 
            for j in range(N):
                if ck[i] and ck[j]:
                    a += score[i][j]
                elif not ck[i] and not ck[j]:
                    b += score[i][j]
        min_num = min(min_num, abs(a-b))
        return
    else:
        for i in range(idx, N):
            if ck[i] == False : 
                ck[i] = True
                dfs(n+1, i+1)
                ck[i] = False
import sys
N = int(sys.stdin.readline())
ck = [False]*N
score = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
min_num = 1000000000
dfs(0, 0)
print(min_num)

