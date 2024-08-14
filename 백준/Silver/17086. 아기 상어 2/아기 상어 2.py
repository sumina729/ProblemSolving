import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[-1 for _ in range(M)]for _ in range(N)]
max_n = 0

def bfs(start_x, start_y):
    global max_n

    q = deque()
    q.append((start_x, start_y))
    visited[start_y][start_x] = 0
    is_stop = False
    while(len(q)!=0):
        
        x, y = q.popleft()
        dx, dy = [0,0,-1,1, -1, 1, -1, 1], [-1,1,0,0, -1, -1, 1, 1]

        for i in range(8):
                    nx, ny = dx[i] + x, dy[i] + y
                    
                    if 0 <= nx < M and 0 <= ny < N and visited[ny][nx] == -1:
                        if maps[ny][nx] == 1:
                            visited[ny][nx] = visited[y][x] + 1
                            max_n = max(max_n, visited[ny][nx])
                            is_stop = True
                            # q.append((nx,ny))
                        elif maps[ny][nx] == 0:
                            visited[ny][nx] = visited[y][x] + 1
                            q.append((nx,ny))
                            
        if is_stop : break

    
        

is_end = False
for i in range(N):
    for j in range(M):
        if maps[i][j] == 0:
            visited = [[-1 for _ in range(M)]for _ in range(N)]
            bfs(j, i)
print(max_n)