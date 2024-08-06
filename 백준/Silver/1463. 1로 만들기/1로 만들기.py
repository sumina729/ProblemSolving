dp = [0] * 1000001
number = int(input())

for i in range(2, number+1):
    dp[i] = dp[i-1] + 1
    if i%3 == 0: dp[i] = min(dp[i], dp[int(i/3)]+1)
    if i%2 == 0: dp[i] = min(dp[i], dp[int(i/2)]+1)

print(dp[number])