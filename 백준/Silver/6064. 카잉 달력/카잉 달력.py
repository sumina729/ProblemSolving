import sys
import math
input = sys.stdin.readline


#1 100 2 50 60 3 5 6 7 8 
for_n = int(input())

for _ in range(for_n):
    M, N, x, y = map(int, input().split())

    is_good = False
    cnt = x
    while cnt <=  M*N:
        # print(cnt, cnt-x, cnt-y)
        if (cnt-x) % M == 0 and (cnt-y) % N == 0:
            is_good = True
            break
        cnt+=M

    if is_good:
        print(cnt)
    else:
        print(-1)
