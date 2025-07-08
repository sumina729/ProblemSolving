import sys
input = sys.stdin.readline

N = int(input())
c_list = [list(map(int, input().split())) for _ in range(N)]

dp = [0 for _ in range(N+1)]
max_v = 0

for i in range(1, N+1):
    get_day = i+c_list[i-1][0]-1
    pay = c_list[i-1][1]
    
    if get_day <= N:
        n = max_v+pay
        dp[get_day] = max(dp[get_day], n)

    max_v = max(dp[i], max_v) 
    
    # print(dp, max_v)

print(max(dp)) 