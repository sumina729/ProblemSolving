import sys
input = sys.stdin.readline

N, B = input().split()
N = list(N)
B = int(B)

arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

resert = 0
up = 0

while N:
    resert = resert + (arr.index(N[-1])*(B**up))
    N.pop()
    up+=1

print(resert)