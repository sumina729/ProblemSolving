def go_dp(N, money):
    
    dp = [0 for i in range(N)]
    dp[0] = money[0]
    dp[1] = max(money[0], money[1])
  
    for i in range(2, N):
        dp[i] = max(dp[i-1], dp[i-2]+money[i])

    return max(dp)

def solution(money):
    answer = 0
    
    N = len(money)
    return max(go_dp(len(money[0:N-1]), money[0:N-1]), go_dp(len(money[1:N]), money[1:N]))