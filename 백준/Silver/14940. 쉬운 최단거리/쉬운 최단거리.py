import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[-1 for _ in range(M)]for _ in range(N)]

def bfs(start_x, start_y):
    q = deque()
    q.append((start_x, start_y))
    visited[start_y][start_x] = 0

    while(len(q)!=0):
        
        x, y = q.popleft()
    
        if y+1 < N and visited[y+1][x] == -1: 
            if maps[y+1][x] == 0 :
                visited[y+1][x] = 0
            else :
                visited[y+1][x] = visited[y][x]+1
                q.append((x, y+1))

        if x+1 < M and  visited[y][x+1] == -1:  
            if maps[y][x+1] == 0 :
                visited[y][x+1] = 0
            else :
                visited[y][x+1] = visited[y][x]+1
                q.append((x+1, y))

        if y-1 >= 0 and  visited[y-1][x] == -1:  
            if maps[y-1][x] == 0 :
                visited[y-1][x] = 0
            else :
                visited[y-1][x] = visited[y][x]+1
                q.append((x, y-1))

        if x-1 >= 0 and  visited[y][x-1] == -1:  
            if maps[y][x-1] == 0 :
                visited[y][x-1] = 0
            else :
                visited[y][x-1] = visited[y][x]+1
                q.append((x-1, y))



is_end = False
for i in range(N):
    for j in range(M):
        if maps[i][j] == 2:
            bfs(j, i)
            is_end = True
            break
    if is_end:
        break

for i in range(N):
    for j in range(M):
        if maps[i][j] == 0:
            print(0, end=' ')
        else :
            print(visited[i][j], end = " ")
    print()
