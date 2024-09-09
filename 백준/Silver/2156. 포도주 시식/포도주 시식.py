import sys
input = sys.stdin.readline


M = int(input())
N = []
dp = [0]*M

for _ in range(M):
    N.append(int(input()))


if M > 0: dp[0] = N[0]
if M > 1: dp[1] = N[1]+N[0]
if M > 2: dp[2] = max(N[0]+N[1], N[1]+N[2], N[0]+N[2])

for i in range(3, M):
    dp[i] = max(N[i]+dp[i-2], N[i]+N[i-1]+dp[i-3], dp[i-1]) #안쓰는 경우동 있음.;;

print(max(dp))
