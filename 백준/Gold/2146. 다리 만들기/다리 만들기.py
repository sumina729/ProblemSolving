import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

pan = [list(map(int, input().split())) for _ in range(N)]

g_pan = [[0 for _ in range(N)] for _ in range(N)]
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

def bfs(y, x, cnt):
    global pan, g_pan

    que = deque()
    que.append([y, x])
    g_pan[y][x] = cnt

    while que:
        cy, cx =  que.popleft()

        for i in range(4):
            ny = cy+dy[i]
            nx = cx+dx[i]

            if -1<ny<N and  -1<nx<N and g_pan[ny][nx] == 0 and pan[ny][nx] == 1:
                g_pan[ny][nx] = cnt
                que.append([ny, nx])

cnt = 0
for y in range(N):
    for x in range(N):
        if g_pan[y][x] == 0 and pan[y][x] > 0:
            cnt+=1
            bfs(y, x, cnt)


def is_go(cy, cx):
    global g_pan

    for i in range(4):
        ny = cy+dy[i]
        nx = cx+dx[i]

        if -1<ny<N and  -1<nx<N and g_pan[ny][nx] == 0:
            return True
        
    return False


def bfs2(y, x, cnt):
    global pan, g_pan, min_l
    visited = [[-1 for _ in range(N)] for _ in range(N)]

    que = deque()
    que.append([y, x])
    visited[y][x] = 0

    while que:
        cy, cx =  que.popleft()

        for i in range(4):
            ny = cy+dy[i]
            nx = cx+dx[i]

            if -1<ny<N and  -1<nx<N and not g_pan[ny][nx] == cnt and visited[ny][nx] == -1:
                if not g_pan[ny][nx] == 0: # 자기 아디고 다른섬 있으면
                    return visited[cy][cx]

                if visited[cy][cx] == min_l:
                    return min_l
                
                visited[ny][nx] = visited[cy][cx]+1
                que.append([ny, nx])

    return min_l

min_l = N*N
for y in range(N):
    for x in range(N):
        if g_pan[y][x] > 0 and is_go(y, x):
            min_l = min(min_l, bfs2(y, x, g_pan[y][x]))

print(min_l)



