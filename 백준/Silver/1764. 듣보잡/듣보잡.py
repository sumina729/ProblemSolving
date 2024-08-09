import sys

N,M = map(int, sys.stdin.readline().split())
name_n = set([sys.stdin.readline() for i in range(N)])
name_m = set([sys.stdin.readline() for i in range(M)])
# name_n = [sys.stdin.readline() for i in range(N)]
# name_m = [sys.stdin.readline() for i in range(M)]
name_mn = []

for i in name_n:
    if i in name_m : name_mn.append(i)
        

name_mn.sort()
print(len(name_mn))
for i in name_mn:
    print(i, end="")