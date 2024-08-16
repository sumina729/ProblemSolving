import sys
input = sys.stdin.readline

N = int(input()) 
A = list(map(int, input().split()))
A.insert(0, 0)
resert = []

dp = [1 for _ in range(N+1)]
dp[1] = 1

for i in range(2, N+1):
    for j in range(i-1, 0, -1):
        if A[i] > A[j] : 
            dp[i] = max(dp[i], dp[j]+1)

resert = max(dp)
print(resert)

n = resert
resert2 = []
for i in range(N, 0, -1):
    if dp[i] == n :
        resert2.append(A[i])
        n-=1

print(*resert2[::-1])
