import sys
input = sys.stdin.readline

#1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19)
num = int(input())
b_n = int(input())
b_list = list(map(int, input().split()))


min_num = abs(100-num)
for i in range(num):
    chnnel = str(i)

    for j in range(len(chnnel)):
        if int(chnnel[j]) in b_list:
            break

        elif j == len(chnnel) - 1:
            min_num = min(min_num, len(chnnel)+abs(int(chnnel)-num))

for i in range(num, num+min_num):
    chnnel = str(i)

    for j in range(len(chnnel)):
        if int(chnnel[j]) in b_list:
            break

        elif j == len(chnnel) - 1:
            min_num = min(min_num, len(chnnel)+abs(int(chnnel)-num))

print(min_num)