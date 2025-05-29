from collections import deque

def go(golem):
    global pan, M, N, d

    # 남쪽
    go_d = [1, 2, 3]
    is_god = 1
    for i in go_d:
        nx = golem[i][0]
        ny = golem[i][1]+1

        if ny == N or (-1<nx<M and -1<ny<N and pan[ny][nx] > 0): #벽이거나
            is_god = 0 # 1개다로 갈수 없으면

    if is_god: #갈 수 있으면
        for i in range(5):
            golem[i][1] = golem[i][1] + 1
        return 1

    #서쪽 아래
    go_d = [0, 2, 3]
    is_god = 1
    for i in go_d:
        nx = golem[i][0]-1
        ny = golem[i][1]

        if nx == -1 or (-1<nx<M and -1<ny<N and pan[ny][nx] > 0): #벽이거나
            is_god = 0 # 1개다로 갈수 없으면
    go_d = [1, 2, 3]

    for i in go_d:
        nx = golem[i][0] -1
        ny = golem[i][1] + 1

        if ny == N or nx == -1 or (-1 < nx < M and -1 < ny < N and pan[ny][nx] > 0):  # 벽이거나
            is_god = 0  # 1개다로 갈수 없으면

    if is_god:
        d = (d-1)%4#갈 수 있으면
        for i in range(5):
            golem[i][0] = golem[i][0] -1
            golem[i][1] = golem[i][1] +1
        return 1

    # 동 아래
    go_d = [0, 1, 2]
    is_god = 1
    for i in go_d:
        nx = golem[i][0] + 1
        ny = golem[i][1]

        if nx == M or (-1 < nx < M and -1 < ny < N and pan[ny][nx] > 0):  # 벽이거나
            is_god = 0  # 1개다로 갈수 없으면
    go_d = [1, 2, 3]
    for i in go_d:
        nx = golem[i][0] + 1
        ny = golem[i][1] + 1

        if ny == N or nx == M or (-1 < nx < M and -1 < ny < N and pan[ny][nx] > 0):  # 벽이거나
            is_god = 0  # 1개다로 갈수 없으면

    if is_god:
        d = (d + 1) % 4# 갈 수 있으면
        for i in range(5):
            golem[i][0] = golem[i][0] + 1
            golem[i][1] = golem[i][1] + 1
        return 1

    return 0

def dfs(x, y):
    global pan, M, N
    visit = [[0 for _ in range(M)] for _ in range(N)]
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    my = -1

    que = deque()
    que.append((x, y))
    visit[y][x] = 1
    my = max(my, y)

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if -1<nx<M and -1<ny<N and visit[ny][nx] == 0 :
            
                if pan[y][x] == 1 and pan[ny][nx] == 3:
                    my = max(my, ny)
                    que.append((nx, ny))
                    visit[ny][nx] = 1
                elif pan[y][x] > 1 and pan[ny][nx] > 0:
                    my = max(my, ny)
                    que.append((nx, ny))
                    visit[ny][nx] = 1

    return my+1

N, M, K = map(int, input().split())
g_cd = []
for i in range(K):
    g_cd.append(list(map(int, input().split()))) # 사용 할때 d-i
pan = [[0 for _ in range(M)] for _ in range(N)]
ans = 0

for c, d in g_cd:
    c = c-1
    golem = [
        [c, -3],
        [c+1, -2],
        [c, -1],
        [c-1, -2],
        [c, -2]
    ]

    while True: # 골룸 갈수 있을 만큼 가기
        n = go(golem)
        # print(n)
        if n == 0:
            break

    is_reset = 0
    for i in range(5):
        x = golem[i][0]
        y = golem[i][1]

        if y < 0:
            is_reset = 1
            break
        if i == 4:
            pan[y][x] = 3
        elif i == d:
            pan[y][x] = 2
        else:
            pan[y][x] = 1

    if is_reset:
        pan = [[0 for _ in range(M)] for _ in range(N)]
        continue
        # break

    ans += dfs(golem[4][0], golem[4][1])

print(ans)