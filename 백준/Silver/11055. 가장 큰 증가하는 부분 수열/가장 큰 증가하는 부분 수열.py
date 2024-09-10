import sys
input = sys.stdin.readline

#1 100 2 50 60 3 5 6 7 8
N = int(input())
lists = list(map(int, input().split()))
dp = [0]*N


dp[0] = lists[0]

for i in range(N):
    dp[i] = lists[i]
    tmp_dp = 0
    for j in range(i-1, -1, -1):
        if lists[i] > lists[j]:
            tmp_dp = max(tmp_dp, dp[j])
    dp[i] = dp[i]+ tmp_dp
    
print(max(dp))