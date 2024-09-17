import sys
input = sys.stdin.readline

#1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19)
E, S, M = map(int, input().split())


count = 0
e,s,m = 0, 0, 0
while(True):
    count +=1

    e+=1
    s+=1
    m+=1

    if e >15: e = 1
    if s >28: s = 1
    if m >19: m = 1

    if e == E and s == S and m == M:
        break

print(count)