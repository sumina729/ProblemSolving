def solution(m, n, puddles):
    global s_len, answer, visited
    answer = 0
    
    dp = [[0 for j in range(m) ] for i in range(n)]
    
    for x, y in puddles:
        dp[y-1][x-1] = -1
        
    dp[0][0] = 1
    # puddles = set(puddles)
    for y in range(n):
        for x in range(m):
            if dp[y][x] == -1:
                dp[y][x] = 0
                continue
                
            if y > 0:
                dp[y][x] += dp[y-1][x]
            if x > 0:
                dp[y][x] += dp[y][x-1]
             
            dp[y][x] %= 1000000007
            
    return dp[n-1][m-1]