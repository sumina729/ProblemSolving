import sys
input = sys.stdin.readline

N = int(input()) 
A = list(map(int, input().split()))
A.insert(0, 0)

dp = [-1000 for _ in range(N+1)]
dp[1] = A[1]

for i in range(2, N+1):
    dp[i] = max(A[i], A[i]+dp[i-1])

print(max(dp))