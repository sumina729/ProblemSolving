N = int(input())
miro = list(map(int, input().split()))

dp = [-1 for _ in range(N)]

dp[0] = 0
for i in range(0, N):
    n = miro[i]
    for j in range(1, n+1):
        if i+j < N:
            if dp[i] > -1 and  dp[i+j] == -1:
                dp[i+j] = dp[i]+1

print(dp[N-1])