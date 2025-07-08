import sys
input = sys.stdin.readline

N = int(input())
c_list = [list(map(int, input().split())) for _ in range(N)]

dp = [0 for _ in range(N+1)]
max_v = 0

for i in range(1, N+1):
    t = c_list[i-1][0]
    p = c_list[i-1][1]
    
    if i+t-1 <= N:
        dp[i+t-1] = max(dp[i+t-1], max_v+p)
    
    max_v = max(dp[i], max_v) 

    # print(dp, max_v)
    
   

print(max(dp)) 