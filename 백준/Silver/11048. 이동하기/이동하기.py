N, M = map(int, input().split())

pan = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(M)]for _ in range(N)]


dx = [-1, -1, 0]
dy = [0, -1, -1]

for y in range(N):
    for x in range(M):

        max_l = [0]
        for i in range(3):
            py = y+dy[i]
            px = x+dx[i]

            if -1<py<N and -1<px<M:
                max_l.append(dp[py][px])
            
        dp[y][x] = max(max_l) + pan[y][x]


print(dp[N-1][M-1])