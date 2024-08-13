import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
maps = [list(map(int, (str(sys.stdin.readline()).strip())))for _ in range(N)]

def bfs(start_x, start_y):
    q = deque()
    q.append((start_x, start_y))

    while(len(q)!=0):
       
        
        x, y = q.popleft()
        if x == M-1 and y == N-1:
            print(maps[y][x])
            break
        elif not maps[y][x] ==0:
            if y+1 < N and  maps[y+1][x] == 1 : 
                q.append((x, y+1))
                maps[y+1][x] = maps[y][x]+1

            if x+1 < M and  maps[y][x+1] == 1 :  
                q.append((x+1, y))
                maps[y][x+1] = maps[y][x]+1

            if y-1 >= 0 and  maps[y-1][x] == 1 :  
                q.append((x, y-1))
                maps[y-1][x] = maps[y][x]+1

            if x-1 >= 0 and  maps[y][x-1] == 1 :  
                q.append((x-1, y))
                maps[y][x-1] = maps[y][x]+1
        

bfs(0,0)