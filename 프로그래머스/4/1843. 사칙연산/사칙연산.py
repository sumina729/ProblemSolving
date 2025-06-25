import math

def solution(arr):
    answer = -1
    
    number = []
    operator = []
    
    for a in arr:
        if a == "-" or a == "+":
            operator.append(a)
        else:
            number.append(int(a))
            
    # print(number)
    # print(operator)
    
    N = len(number)
    
    min_dp = [[math.inf for _ in range(N)]for _ in range(N)]
    max_dp =  [[-math.inf for _ in range(N)]for _ in range(N)]
            
    
    
    for l in range(N):
        for i in range(N):
            j = i+l
            if j > N-1:
                continue
                
            # print(i, j)
            if i == j:
                min_dp[i][j] = number[i]
                max_dp[i][j] = number[i]
            else:
                for k in range(l):
                    # print(i, i+k, i+k+1, j, operator[i+k])
                    if operator[i+k] == '-':
                        max_dp[i][j] = max(max_dp[i][i+k] - min_dp[i+k+1][j], max_dp[i][j])
                        min_dp[i][j] = min(min_dp[i][i+k] - max_dp[i+k+1][j], min_dp[i][j])
                    else:
                        max_dp[i][j] = max(max_dp[i][i+k] + max_dp[i+k+1][j], max_dp[i][j])
                        min_dp[i][j] = min(min_dp[i][i+k] + min_dp[i+k+1][j], min_dp[i][j])
            # print("max", max_dp[i][j])
            # print("min",max_dp[i][j])
                        
                    
                
    # print(N)
    # print(min_dp)
    # print(max_dp)
    # print(max_dp[0][N-1])
        

    return max_dp[0][N-1]
