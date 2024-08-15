import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
P.insert(0, 0)

dp = [0]*(N+1)

dp[1] = P[1]
for i in range(2, N+1): #4
    dp[i] = P[i]
    for j in range(1, i): #1,2,3
        dp[i] = min(dp[i], dp[j]+P[i-j])

print(dp[N])