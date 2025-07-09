from collections import deque

import sys
input = sys.stdin.readline

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]
    
def dfs(cy, cx):
    global visited, N, M, pan


    for i in range(4): 
        ny = cy+dy[i]
        nx = cx+dx[i]

        # print(cy, cx, '->', ny, nx, pan[ny][nx], pan[cy][cx])
        if -1<ny<N and -1<nx<M and pan[ny][nx] == pan[cy][cx]: 

            if visited[ny][nx] == 0:
                visited[ny][nx] = visited[cy][cx]+1
                dfs(ny, nx)


N, M = map(int, input().split())
pan = [list(input().strip()) for _ in range(N)]


for y in range(N):
    for x in range(M):
        visited = [[0 for _ in range(M)]for _ in range(N)]
        visited[y][x] = 1
        dfs(y, x)

        for i in range(4): 
            ny = y+dy[i]
            nx = x+dx[i]

            if -1<ny<N and -1<nx<M and visited[y+dy[i]][x+dx[i]] > 3:
                print("Yes")
                exit()
        
        visited[y][x] = 0


print("No")
