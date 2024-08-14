import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())
maps = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)]for _ in range(H)]
visited = [[[-1 for _ in range(M)]for _ in range(N)]for _ in range(H)]
resert = 0

def bfs():
    global resert
    q = deque()
    for k in range(H):
        for i in range(N):
            for j in range(M):
                    if maps[k][i][j] == 1:
                        q.append((j, i, k))
                        visited[k][i][j] = 0

    while(len(q)!=0):
        x, y, h= q.popleft()
        dx, dy, dh= [0,0,-1,1, 0, 0], [-1,1,0,0, 0, 0], [0, 0, 0, 0, 1, -1]

        for i in range(6):
            nx, ny, nh = dx[i] + x, dy[i] + y, dh[i] + h
            if 0 <= nx < M and 0 <= ny < N and 0 <= nh < H and visited[nh][ny][nx] == -1:
                if maps[nh][ny][nx] == -1:
                    visited[nh][ny][nx] = -2
                elif maps[nh][ny][nx] == 1:
                    visited[nh][ny][nx] = visited[nh][ny][nx]
                elif maps[nh][ny][nx] == 0:
                    visited[nh][ny][nx] = visited[h][y][x] + 1
                    maps[nh][ny][nx] = 1
                    resert = visited[nh][ny][nx]
                    q.append((nx,ny, nh))
    

bfs()
is_no = False
for k in range(H):
        for i in range(N):
            for j in range(M):
                if maps[k][i][j] == 0 :
                        is_no = True
                        break

if is_no : print(-1)
else : print(resert)