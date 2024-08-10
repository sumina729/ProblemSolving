import sys
N = int(sys.stdin.readline())
lists = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
maps = [[0 for j in range(100)] for i in range(100)]
count = 0

for n in range(N):
    for i in range(10):
        for j in range(10):
            maps[lists[n][1]+i-1][lists[n][0]+j-1] = 1


for i in range(100):
    for j in range(100):
        if(maps[i][j]==1): count +=1

print(count)