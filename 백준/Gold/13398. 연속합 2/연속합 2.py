import sys
input = sys.stdin.readline

N = int(input()) 
A = list(map(int, input().split()))
dp = [[0 for _ in range(N)]for _ in range(2)]

dp[0][0] = A[0]
dp[1][0] = A[0]


for i in range(1, N):
    dp[0][i] = max(A[i], A[i]+dp[0][i-1]) 
    dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + A[i])


print(max(max(dp[0]), max(dp[1])))