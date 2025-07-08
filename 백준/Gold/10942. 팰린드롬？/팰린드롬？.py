import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
M = int(input())
m_list = [list(map(int, input().split())) for _ in range(M)]

# print(N)
# print(num_list)
# print(M)
# print(m_list)

dp = [[0 for _ in range(N+1)]for _ in range(N+1)]
for l in range(1, N+1):
    for s in range(1, N+1):
        e = s+l-1
        
        if e > N:
            continue

        
        if l == 1:
            dp[s][e] = 1
        
        elif l == 2:
            if num_list[s-1] == num_list[e-1]:
                dp[s][e] = 1
            else:
                dp[s][e] = 0
        else:
            if num_list[s-1] == num_list[e-1] and dp[s+1][e-1] == 1:
                dp[s][e] = 1
            else:
                dp[s][e] = 0

        
for s, e in m_list:
    print(dp[s][e])