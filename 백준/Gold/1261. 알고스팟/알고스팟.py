from collections import deque

M, N = map(int, input().split())
pan = [list(map(int, input())) for _ in range(N)]
pan_v = [[-1 for _ in range(M)] for _ in range(N)]


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs():
    global N, M

    que = deque()
    que.append([0, 0])
    pan_v[0][0] = 0

    while que:
        cy, cx = que.popleft()

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if -1<ny<N and -1<nx<M and pan_v[ny][nx] ==  -1: # 방분 안하면서

                if pan[ny][nx] == 0: # 벽 아니면
                    que.appendleft([ny, nx])
                    pan_v[ny][nx] = pan_v[cy][cx]

                else: #벽이면
                    que.append([ny, nx])
                    pan_v[ny][nx] = pan_v[cy][cx]+1
    return pan_v[N-1][M-1]
     

print(bfs())

