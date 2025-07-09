from collections import deque

import sys
input = sys.stdin.readline


dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]

def bfs(y, x):
    global pan, visited

    que = deque()
    que.append([y, x])
    visited[y][x] = 1

    while que:
        cy, cx = que.popleft()

        for i in range(8):
            
            ny = cy+dy[i]
            nx = cx+dx[i]

            if -1<ny<h and -1<nx<w and visited[ny][nx] == 0 and pan[ny][nx] == 1:
                que.append([ny, nx])
                visited[ny][nx] = 1
    
while True:

    w, h = map(int, input().split())

    if w == 0 or h == 0:
        break
    
    pan = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0 for _ in range(w)]for _ in range(h)]

    ans = 0
    for y in range(h):
        for x in range(w):
            if pan[y][x] == 1 and visited[y][x] == 0:
                ans+=1
                bfs(y, x)

    print(ans)