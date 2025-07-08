N, K = map(int, input().split())
bag = [list(map(int, input().split()) ) for _ in range(N)] #[W, V]

dp = [[0 for _ in range(N+1)] for _ in range(K+1)]

for i in range(1, K+1): #최대 무게
    for j in range(1, N+1): # j번 가방탐색 (1~j 번 까지 고려)

        w = bag[j-1][0] 
        v = bag[j-1][1] 

        if w > i: #j번 무게가 최대 부개를 넘어가면
            dp[i][j] = dp[i][j-1]
        else:
            min1 = dp[i][j-1] #안 넣었을 때의 가치
            min2 = v + dp[i-w][j-1] #j번 가방의 가치 + 남은 무게이먄서 j이전 탐색 까지의 가치

            dp[i][j] = max(min1, min2)

print(max(dp[K]))