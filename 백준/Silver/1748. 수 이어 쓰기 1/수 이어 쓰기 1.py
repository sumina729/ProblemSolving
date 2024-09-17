import sys
input = sys.stdin.readline

N = int(input())
count = 0

n = len(str(N))

for i in range(1, n):
    count += ((10**(i-1))*9)*i
    N -= (10**(i-1))*9

count += N*n
print(count)