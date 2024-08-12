import sys

N, L, R, X = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
count = 0 

def dfs(max_a, min_a, sum_a, idx):
    global count
    
    for i in range(idx, N):
        sum_tmp = sum_a+a[i]
        max_tmp = max(max_a, a[i])
        min_tmp = min(min_a, a[i])

        if L<=sum_tmp and R>=sum_tmp and max_tmp-min_tmp >= X:
            # print('===>')
            count+=1
        dfs(max_tmp, min_tmp, sum_tmp, i+1)

dfs(0, 1000000, 0, 0)
print(count)