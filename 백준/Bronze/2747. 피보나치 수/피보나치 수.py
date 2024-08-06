num = int(input())
dp = [0]*(num+1)

for i in range(num+1):
    if i == 0: dp[i] = 0
    elif i == 1: dp[i] = 1
    else : dp[i] = dp[i-1] + dp[i-2]


print(dp[num])