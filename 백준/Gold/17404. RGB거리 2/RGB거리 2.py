N = int(input())
RGB_list = [list(map(int, input().split())) for _ in range(N)]

ans = [] 

for k in range(3):
    dp = [[0, 0, 0] for _ in range(N)]
    dp[0] = [RGB_list[0][k], RGB_list[0][k], RGB_list[0][k]]

    for i in range(1, N):
    
        dp[i][0] = min(RGB_list[i][0]+dp[i-1][1], RGB_list[i][0]+dp[i-1][2])
        dp[i][1] = min(RGB_list[i][1]+dp[i-1][0], RGB_list[i][1]+dp[i-1][2])
        dp[i][2] = min(RGB_list[i][2]+dp[i-1][1], RGB_list[i][2]+dp[i-1][0])

        if i == 1:
            dp[1][k]= 10000
    
    tmp = []
    for i in range(3):
        if i == k:
            continue
        
        tmp.append(dp[N-1][i])
    
    ans.append(min(tmp))

print(min(ans))
 

