def go_dp(N, money):
    
    dp = [0 for i in range(N)]
    dp[0] = money[0]
    dp[1] = max(money[0], money[1])
    # print(N)
    for i in range(2, N):
        # print(money, dp[i-1], dp[i-2])
        dp[i] = max(dp[i-1], dp[i-2]+money[i])
        # print(dp)
    
    # print()
    return max(dp)

def solution(money):
    answer = 0
    
    N = len(money)
    # print(N, money)
    
    
    
    
    return max(go_dp(len(money[0:N-1]), money[0:N-1]), go_dp(len(money[1:N]), money[1:N]))