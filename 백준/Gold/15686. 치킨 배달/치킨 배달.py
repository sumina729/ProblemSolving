import sys
import copy
N, M = map(int, sys.stdin.readline().split())
map = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
min_num = 100000000000

home = []
chicken = []
for y in range(N) : 
    for x in range(N) :
        if(map[y][x] == 1): 
            array=[y, x, N+N]
            home.append(array)
        if(map[y][x] == 2): 
            array=[y, x]
            chicken.append(array)

def chicken_dist(i):
    global home
    for j in range(len(home)):
        home[j][2] = min(home[j][2], abs(chicken[i][0]-home[j][0])+abs(chicken[i][1]-home[j][1])) 

def dfs(m, idx):

    global home
    global min_num
    if(m == M):
        dist = 0
        for i in range(len(home)):
            dist+=home[i][2]
        min_num = min(min_num, dist)
        return
    
    for i in range(idx, len(chicken)):
        tmp = copy.deepcopy(home)
        chicken_dist(i)
        dfs(m+1, i+1)
        home = copy.deepcopy(tmp)
dfs(0, 0)
print(min_num)