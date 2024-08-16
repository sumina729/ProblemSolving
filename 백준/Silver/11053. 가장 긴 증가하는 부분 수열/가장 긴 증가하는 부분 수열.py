import sys
input = sys.stdin.readline

N = int(input()) 
A = list(map(int, input().split()))
A.insert(0, 0)

dp = [1 for _ in range(N+1)]
dp[1] = 1

for i in range(2, N+1):
    for j in range(i-1, 0, -1):
        if A[i] > A[j] : 
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
