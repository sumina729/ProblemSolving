from collections import deque
import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def  make_gisa_pan(gisa, pan):
    global L, N, Q

    tmp_pan = [[0 for _ in range(L)] for _ in range(L)]

    for i in range(N):
        gy, gx, gh, gw, gk = gisa[i]
        if gk > 0: #살아있는 기사만

            for y in range(gh):
                for x in range(gw):
                    tmp_pan[gy+y][gx+x] = i + 1  # 나중에주의


    for y in range(L):
        for x in range(L):
            if pan[y][x] == 2:
                tmp_pan[y][x] =  -1

    return tmp_pan

def is_in_pan(y, x):
    global L, N, Q
    return -1 < y < L and -1 < x < L

def move_bfs(gisa_pan, y, x, move_di, gisa_i):
    global L, N, Q
    visited = [[0 for _ in range(L)] for _ in range(L)]
    move_gisa_i = set()

    que = deque()
    que.append((y, x))
    visited[y][x] = 1

    while que:
        cy, cx = que.popleft()

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if i == move_di:
                if not is_in_pan(ny, nx) or gisa_pan[ny][nx] == -1: #즉 벽이면
                    return -1

                elif gisa_pan[ny][nx] > 0: #그 방향으로난 다른 기사로 이동
                    que.append((ny, nx))
                    if not gisa_i == gisa_pan[ny][nx]-1:
                        move_gisa_i.add(gisa_pan[ny][nx]-1)
                    visited[ny][nx] = 1
            else:
                if is_in_pan(ny, nx) and visited[ny][nx] == 0 and gisa_pan[cy][cx] == gisa_pan[ny][nx]:
                    que.append((ny, nx))
                    if not gisa_i == gisa_pan[ny][nx]-1:
                        move_gisa_i.add(gisa_pan[ny][nx]-1)
                    visited[ny][nx] = 1

    return move_gisa_i

def move_gisa(move_gisa_list, gisa, pan, move_di, gisa_i):
    global L, N, Q

    for i in range(N):
        if i in move_gisa_list:  # 움직이는 기사만

            gy, gx, gh, gw, gk = gisa[i]
            gy += dy[move_di]
            gx += dx[move_di]

            if not gisa_i == i:
                cnt = 0
                for y in range(gh):
                    for x in range(gw):
                        if pan[gy + y][gx + x] ==  1:
                            cnt+=1
                gk-=cnt

            gisa[i] = [gy, gx, gh, gw, gk]

L,N,Q = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(L)]

gk_list = []
gisa = []
for _ in range(N):
    y, x, h, w, k = map(int, input().split())
    y-=1
    x-=1
    gk_list.append(k)
    gisa.append([y, x, h, w, k])

go_list = []
for _ in range(Q):
    i, d = map(int, input().split())
    i-=1
    go_list.append([i, d])

for q in range(Q):

    gisa_i, move_di = go_list[q]

    if gisa[gisa_i][4] < 1:
        # print("체스판에서 사라진 기사임!")
        continue

    gisa_pan = make_gisa_pan(gisa, pan)

    move_gisa_list = move_bfs(gisa_pan, gisa[gisa_i][0], gisa[gisa_i][1], move_di, gisa_i)
    if move_gisa_list == -1:
        continue

    move_gisa(move_gisa_list, gisa, pan, move_di, gisa_i)
    gisa_pan = make_gisa_pan(gisa, pan)

ans = 0
for i in range(N):
    gy, gx, gh, gw, gk = gisa[i]
    if gk > 0:
        ans += (gk_list[i]-gk)
print(ans)