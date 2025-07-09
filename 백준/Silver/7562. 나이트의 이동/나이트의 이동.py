from collections import deque

import sys
input = sys.stdin.readline

from collections import deque

import sys
input = sys.stdin.readline


dy = [-1, -2, -2, -1, 1, 2, 2, 1]
dx = [-2, -1, 1, 2, -2, -1, 1, 2]

def bfs(sy, sx, ey, ex):
    global visited, N

    que = deque()
    que.append([sy, sx])
    visited[sy][sx] = 0

    if sy == ey and sx == ex:
        return 0
    
    while que:
        cy, cx = que.popleft()
        
        for i in range(8):
            
            ny = cy+dy[i]
            nx = cx+dx[i]

            if -1<ny<N and -1<nx<N and visited[ny][nx] == -1:
                que.append([ny, nx])
                visited[ny][nx] = visited[cy][cx]+1

                if ny == ey and nx == ex:
                    return visited[ny][nx]
    

T = int(input()) 
for _ in range(T):

    N = int(input())
    visited = [[-1 for _ in range(N)]for _ in range(N)]

    sy, sx = map(int, input().split())
    ey, ex = map(int, input().split())

    print(bfs(sy, sx, ey, ex))