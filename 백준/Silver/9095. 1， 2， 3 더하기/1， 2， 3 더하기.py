N = int(input())
for k in range(N):
    number = int(input())

    #각 숫자마다 불린 횟수를 저장
    dp = [0]*(number+1)

    if number > 0: dp[1] = 1
    if number > 1: dp[2] = 2
    if number > 2: dp[3] = 4
    if number > 3:
        for i in range(4, number+1):
            dp[i] = dp[i-1]+dp[i-2]+dp[i-3]

    print(dp[number])