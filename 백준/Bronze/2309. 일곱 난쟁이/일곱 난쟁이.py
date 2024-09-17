import sys
input = sys.stdin.readline

N = [int(input()) for _ in range(9)]

sum_all = sum(N)
is_stop = False

for i in range(9):
    for j in range(9):
        if j == i: 
            continue

        tmp1 = N[i]
        tmp2 = N[j]
        if sum_all-tmp1-tmp2 == 100:
            N.remove(tmp1)
            N.remove(tmp2)
            # print(tmp1, tmp2)
            is_stop = True
            break

    if is_stop:
        break

N.sort()
for i in range(7):
    print(N[i])