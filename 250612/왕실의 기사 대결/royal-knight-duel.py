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
                # print(i, gisa_pan[ny][nx])
                if not is_in_pan(ny, nx) or gisa_pan[ny][nx] == -1: #즉 벽이면
                    # print("이동못함")
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

    # print("이동해야 하는 블럭들")
    # for y in range(L):
    #     print(visited[y])

    return move_gisa_i

def move_gisa(move_gisa_list, gisa, pan, move_di, gisa_i):
    global L, N, Q

    for i in range(N):
        if i in move_gisa_list:  # 움직이는 기사만
            cnt = 0
            gy, gx, gh, gw, gk = gisa[i]
            gy += dy[move_di]
            gx += dx[move_di]
            for y in range(gh):
                for x in range(gw):
                    if pan[gy + y][gx + x] ==  1:
                        cnt+=1
            gk-=cnt
            # print(i, gy, gx, gh, gw, gk)
            gisa[i] = [gy, gx, gh, gw, gk]
        elif gisa_i == i:
            gy, gx, gh, gw, gk = gisa[i]
            gy += dy[move_di]
            gx += dx[move_di]
            # print("민거는 노노:", i, gy, gx, gh, gw, gk)
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

# print("초기세팅")
# print("L,N,Q", L,N,Q)
# print("pan")
# for y in range(L):
#     print(pan[y])
# print("gisa[y, x, h, w, k]", gisa)
# print("go_list", go_list)


for q in range(Q):

    # print("==========",q+1, "번째 명령 시작 ==========")
    gisa_i, move_di = go_list[q]
    # print(gisa_i,"번", move_di,"방향")

    if gisa[gisa_i][4] < 1:
        # print("체스판에서 사라진 기사임!")
        continue

    gisa_pan = make_gisa_pan(gisa, pan)
    # print("기사판 만들기(벽 포함)")
    # for y in range(L):
    #     print(gisa_pan[y])

    move_gisa_list = move_bfs(gisa_pan, gisa[gisa_i][0], gisa[gisa_i][1], move_di, gisa_i)
    if move_gisa_list == -1:
        # break
        continue

    # print(move_gisa_list)
    move_gisa(move_gisa_list, gisa, pan, move_di, gisa_i)
    gisa_pan = make_gisa_pan(gisa, pan)
    # print("이동후")
    # for y in range(L):
    #     print(gisa_pan[y])

    # print("gisa[y, x, h, w, k]", gisa)



    # break


ans = 0
for i in range(N):
    gy, gx, gh, gw, gk = gisa[i]
    if gk > 0:
        ans += (gk_list[i]-gk)
print(ans)
