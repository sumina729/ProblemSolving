import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


#상 우 하 죄
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def is_move_ok(y, x, pan, d):
    if d == 0:
        ny = [y+1, y+2, y+1]
        nx = [x-1, x, x+1]
    elif d == 1:
        ny = [y - 1, y, y + 1, y + 1, y + 2]
        nx = [x - 1, x - 2, x - 1, x - 2, x - 1]
    else:
        ny = [y - 1, y, y + 1, y + 1, y + 2]
        nx = [x + 1, x + 2, x + 1, x + 2, x + 1]

    for i in range(len(ny)):
        if -1 < ny[i] < N and -1 < nx[i] < M:
            if pan[ny[i]][nx[i]] > 0:
                return False
        if not ny[i] < N or not -1 < nx[i] < M: #위에 범위는 신경 x
            return False

    return True


def move_golem(gy, gx, pan, di):
    global N, M, K
    cy, cx, ci = gy, gx, di
    # print("초기위치", cy, cx)
    while True:
        if is_move_ok(cy, cx, pan, 0):
            cy+=1
            # print("아래로 이동함", cy, cx, ci)
        elif is_move_ok(cy, cx, pan, 1):
            cx-=1
            cy+=1
            ci=(ci-1)%4
            # print("왼쪽 아래로 회전함 이동함", cy, cx, ci)
        elif is_move_ok(cy, cx, pan, 2):
            cx += 1
            cy += 1
            ci = (ci + 1) % 4
            # print("오른쪽 아래로 회전함 이동함", cy, cx, ci)
        else:
            break

    if cy < 1:
        return -1, -1

    #pan에 두기
    pan[cy][cx] = 4 # 가운데
    for i in range(4):
        ny = cy+dy[i]
        nx = cx+dx[i]

        if i == ci:
            pan[ny][nx] = 2
        else:
            pan[ny][nx] = 1

    return cy, cx


def bfs(pan, gy, gx):
    global N, M, K
    visited = [[0 for _ in range(M)]  for _ in range(N)]


    # print("정령 이동시장 위치:", gy, gx)
    que = deque()
    que.append((gy, gx))
    visited[gy][gx] = 1
    max_y = gy + 1

    while que:
        cy, cx = que.popleft()

        for i in range(4):
            ny = cy+dy[i]
            nx = cx+dx[i]

            if -1<ny<N and -1<nx<M and visited[ny][nx] == 0:
                if pan[cy][cx] == 4: #4방향 모두 이동 가능
                    que.append((ny, nx))
                    visited[ny][nx] = 1
                    max_y = max(ny + 1, max_y)

                elif pan[cy][cx] == 2:
                    if pan[ny][nx] > 0: #1, 2, 4 이동 가능
                        que.append((ny, nx))
                        visited[ny][nx] = 1
                        max_y = max(ny + 1, max_y)

                elif pan[cy][cx] == 1:
                    if pan[ny][nx] == 4: #가운데로만 이동가능
                        que.append((ny, nx))
                        visited[ny][nx] = 1
                        max_y = max(ny + 1, max_y)
                else:
                    print("논리 이상함")

    # print("정령이동결로 판", max_y)
    # for y in range(N):
    #     print(visited[y])

    return max_y

N, M, K = map(int, input().split())
k_list = []
for _ in range(K):
    fx, di = map(int, input().split())
    fx -=1
    k_list.append([fx, di])

pan = [[0 for _ in range(M)] for _ in range(N)]

# print("초기입력")
# print("N, M, K", N, M, K)
# print("[x, i]:", k_list)

ans = 0
for fx, di in k_list:
    # print("===============정령정보[fx, di]", fx, di, "==================")

    gy, gx =  move_golem(-1, fx, pan, di)

    #이동
    if gy ==  -1:
        #이동했는데 범위밖이면 패스
        # print("!!이동했는데 범위밖!! 판 초기화")
        pan = [[0 for _ in range(M)] for _ in range(N)]
        continue

    # print("골룸 안착")
    # for y in range(N):
    #     print(pan[y])


    #정령 가장 아래로 이동
    ans+=bfs(pan, gy, gx)

    # break

print(ans)