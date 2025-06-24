def solution(triangle):
    answer = 0
    
    dp = [[ 0 for j in range(len(triangle[i]))]for i in range(len(triangle))]
    
    dp[0][0] = triangle[0][0]
    
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            r = -1 
            l = -1
            
            if j < len(triangle[i-1]):
                r = triangle[i][j] + dp[i-1][j]
            
            if j-1 > -1:
                l = triangle[i][j] + dp[i-1][j-1]
            
            dp[i][j] = max(r, l)
            
    
    answer =  max(dp[len(triangle[i])-1])

    return answer