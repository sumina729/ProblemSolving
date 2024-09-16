import sys
input = sys.stdin.readline

n = int(input())
num = 1

for i in range(n, 0, -1):
    num*=i

print(num)