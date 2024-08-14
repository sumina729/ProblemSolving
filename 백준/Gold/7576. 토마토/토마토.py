import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[-1 for _ in range(M)]for _ in range(N)]
resert = 0
def bfs():
    global resert
    q = deque()
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 1:
                q.append((j, i))
                visited[i][j] = 0
 
    while(len(q)!=0):
        
        x, y = q.popleft()
        dx, dy = [0,0,-1,1], [-1,1,0,0]

        for i in range(4):
                    nx, ny = dx[i] + x, dy[i] + y
                    
                    if 0 <= nx < M and 0 <= ny < N and visited[ny][nx] == -1:
                        if maps[ny][nx] == -1:
                            visited[ny][nx] = -2
                        elif maps[ny][nx] == 1:
                            visited[ny][nx] = visited[ny][nx]
                        elif maps[ny][nx] == 0:
                            visited[ny][nx] = visited[y][x] + 1
                            maps[ny][nx] = 1
                            resert = visited[ny][nx]
                            q.append((nx,ny))
    

bfs()
is_no = False
for i in range(N):
    for j in range(M):
        if maps[i][j] == 0 : 
            is_no = True
            break
if is_no : print(-1)
else : print(resert)