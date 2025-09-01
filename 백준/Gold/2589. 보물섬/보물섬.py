from collections import deque

N, M = map(int, input().split())
pan = [ list(input().strip()) for _ in range(N) ]


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(y, x):
    global N, M, pan
    visited = [[-1 for _ in range(M)] for _ in range(N)]


    que = deque()
    que.append([y, x])
    visited[y][x] = 0

    while que:
        cy, cx = que.popleft()

        for i in range(4):
            ny = cy+dy[i]
            nx = cx+dx[i]

            # print(ny, nx)
            if -1 < ny < N and -1 < nx < M and pan[ny][nx] == 'L' and visited[ny][nx] == -1:
                que.append([ny, nx])
                visited[ny][nx] = visited[cy][cx]+1
        

    # print()
    # for v in visited:
    #     print(v)


    mxa_n = max(max(v) for v in visited)
    # print(">",  mxa_n)

    return mxa_n



ans = 0

for y in range(N):
    for x in range(M):
        if pan[y][x] == 'L':

            n = bfs(y, x)
            if ans < n:
                ans = n

print(ans)