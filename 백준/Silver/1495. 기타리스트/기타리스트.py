N, S, M = map(int, input().split())
V = list(map(int, input().split()))

dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

dp[0][S] = 1

for n in range(1, N+1):
    for m in range(0, M+1):
        if dp[n-1][m] == 1:

            if m+V[n-1] < M+1:
                dp[n][m+V[n-1]] = 1

            if m-V[n-1] > -1:
                dp[n][m-V[n-1]] = 1
        

if max(dp[N]) == 0:
    print(-1)
else:
    for i in range(M, -1, -1):
        if dp[N][i] == 1:
            print(i)
            break