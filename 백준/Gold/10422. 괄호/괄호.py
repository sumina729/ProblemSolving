dp  = [0 for _ in range(5001)]

dp[0] = 1

for l in range(2, 5001, 2):
    for in_cnt in range(0, l, 2):
        out_cnt = l-2-in_cnt
        dp[l] += dp[in_cnt]*dp[out_cnt]
        dp[l] %= 1000000007
        # print('in_cnt, out_cnt:', in_cnt, out_cnt)
    


T = int(input())
for _ in range(T):
    l = int(input())
    print(dp[l])