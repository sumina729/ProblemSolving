import sys
input = sys.stdin.readline

#1 100 2 50 60 3 5 6 7 8
N = int(input())
lists = list(map(int, input().split()))
dp = [[0 for _ in range(2)]  for _ in range(N)] 


dp[0][0] = 1

for i in range(N):
    dp[i][0] = 1
    tmp_dp = 0
    for j in range(i-1, -1, -1):
        if lists[i] > lists[j]:
            tmp_dp = max(tmp_dp, dp[j][0])
    dp[i][0] = dp[i][0]+ tmp_dp

dp[N-1][1] = 1
for i in range(N-1, -1, -1):
    dp[i][1] = 1
    tmp_dp = 0
    for j in range(i+1, N):
        if lists[i] > lists[j]:
            tmp_dp = max(tmp_dp, dp[j][1])
    dp[i][1] = dp[i][1]+ tmp_dp

max_num = 0
for i in range(N):
    tmp_num = dp[i][1] + dp[i][0] -1
    if  tmp_num > max_num:
        max_num = tmp_num

print(max_num) 