import sys
input = sys.stdin.readline


N = int(input())
lists = []
dp = []

for i in range(N): 
    dp.append([0]*(i+1))
    lists.append(list((map(int, input().split()))))

dp[0][0] = lists[0][0]

for i in range(1, N):
    for j in range(i+1):
        if j-1 < 0:
            dp[i][j] =  dp[i-1][j] + lists[i][j]
        elif j == i:
            dp[i][j] =  dp[i-1][j-1] + lists[i][j]
        elif dp[i-1][j-1] < dp[i-1][j]:
            dp[i][j] =  dp[i-1][j] + lists[i][j]
        else:
            dp[i][j] =  dp[i-1][j-1] + lists[i][j]

print(max(dp[N-1]))
