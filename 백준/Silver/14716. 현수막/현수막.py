import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
resert = 0

def bfs(sx, sy):
    global resert
    q = deque()
    q.append((sx, sy))
    maps[sy][sx] = 0

    while(len(q)!=0):
        x, y = q.popleft()        
        dx, dy = [0,0,-1,1, -1, 1, -1, 1], [-1,1,0,0, -1, -1, 1, 1]

        for i in range(8):
            nx, ny = dx[i] + x, dy[i] + y
            
            if 0 <= nx < M and 0 <= ny < N and maps[ny][nx] == 1:
                maps[ny][nx] = 0
                q.append((nx, ny))               

for i in range(N):
    for j in range(M):
        if maps[i][j] == 1:
            bfs(j, i)
            resert+=1
print(resert)