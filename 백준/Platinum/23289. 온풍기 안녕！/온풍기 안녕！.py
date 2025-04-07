'''
- (r, c)는 r행 c열을 의미 -> 즉 y, x
- 가장 처음에 모든 칸의 온도는 0
. 온풍기는 바람이 나오는 방향: 오른쪽, 왼쪽, 위, 아래

- 성능 테스트는 다음과 같은 작업이 순차적
    1. 집에 있는 모든 온풍기에서 바람이 한 번 나옴

    2. 온도가 조절됨
    3. 온도가 1 이상인 가장 바깥쪽 칸의 온도가 1씩 감소
    4. 초콜릿을 하나 먹는다.
    5. 조사하는 모든 칸의 온도가 K 이상이 되었는지 검사.
        - 모든 칸의 온도가 K이상이면 테스트를 중단하고
        - 아니면 1부터 다시

0: 빈 칸
1: 방향이 오른쪽인 온풍기가 있음
2: 방향이 왼쪽인 온풍기가 있음
3: 방향이 위인 온풍기가 있음
4: 방향이 아래인 온풍기가 있음
5: 온도를 조사해야 하는 칸
'''

from collections import deque

def is_go(sx, sy, ex, ey):

    # print(sx, sy, ex, ey, w_list)
    if (sx, sy, ex, ey) in w_list:
        return False
    elif (ex, ey, sx, sy) in w_list:
        return False
    else:
        return True


def run_onponggi(x, y, d):

    global pan
    visit = [[0 for _ in range(M)] for _ in range(N)]

    que = deque()
    go = []

    if d == 0 or d == 1:
        go = [2, 3]
    else:
        go = [0, 1]

    #처음 1개
    if is_go(x, y, x+dx[d], y+dy[d]):
        pan[y+dy[d]][x+dx[d]] = pan[y+dy[d]][x+dx[d]]+5
        que.append((x + dx[d], y + dy[d], 4))
        visit[y][x] = 1

    while que:
        x, y, n = que.popleft()

        if n == 0:
            continue

        #갈수 있다면 양쪽
        go3 = set()
        go3.add((x, y))
        if is_go(x, y, x+dx[go[0]], y+dy[go[0]]):
            go3.add((x+dx[go[0]], y+dy[go[0]]))
        if is_go(x, y, x + dx[go[1]], y + dy[go[1]]):
            go3.add((x+dx[go[1]], y+dy[go[1]]))

        for nx, ny in go3:
            nnx = nx + dx[d]
            nny = ny + dy[d]
            if -1 < nnx < M and -1 < nny < N and visit[nny][nnx] == 0 and is_go(nx, ny, nnx, nny):
                pan[nny][nnx] = pan[nny][nnx] + n  # 온도 올리기
                que.append((nnx, nny, n - 1))  # 온도 낮추기
                visit[nny][nnx]= 1  # 방문처리

def comput(x, y, nx, ny, tmp_pan):
    global pan
    cnt = abs(pan[y][x]-pan[ny][nx])//4
    if pan[ny][nx] < pan[y][x]:
        tmp_pan[ny][nx] = tmp_pan[ny][nx] + cnt
        tmp_pan[y][x] = tmp_pan[y][x] - cnt


def adjust_ondo():
    global pan
    tmp_pan = [[pan[y][x] for x in range(M)] for y in range(N)]

    for y in range(N):
        for x in range(M):
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if -1<nx<M and -1<ny<N and is_go(x, y, nx, ny):
                    #계산
                    comput(x, y, nx, ny, tmp_pan)
    return tmp_pan




dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

N, M, K = map(int, input().split()) # 모든 칸이 K 이상이면 끝
pan = [list(map(int, input().split())) for _ in range(N)] # -1 계산해줘야함
W = int(input())
w_list = set()
for _ in range(W):
    y, x, t = map(int, input().split())
    if t == 0:
        w_list.add((x-1, y-1, x-1, y-2)) #y-1-1  위에
    else:
        w_list.add((x-1, y-1, x, y-1)) #x-1+1 오른쪽



onponggi = set()
check_ondo = set()
for y in range(N):
    for x in range(M):
        if 0 < pan[y][x] < 5:
            onponggi.add((x, y, pan[y][x]-1))
            pan[y][x] = 0
        elif pan[y][x] ==5:
            check_ondo.add((x, y))
            pan[y][x] = 0


# 여기서 반복
ans = 0
while True:

    is_end = 1
    for x, y in check_ondo:
        if pan[y][x] < K:
            is_end = 0

    if is_end or ans>100:
        print(ans)
        break

    # for y in pan:
    #     print(y)

    # print()
    # print(w_list)
    # run_onponggi(4, 1, 3)
    # run_onponggi(4, 6, 2)
    for x, y, d in onponggi:
        # print(x, y, d)
        run_onponggi(x, y, d)

    # print("=====> 1. 온풍기 작동")
    # for y in pan:
    #     print(y)


    pan = adjust_ondo()
    # print("=====> 3. 온도 계산")
    # for y in pan:
    #     print(y)



    visit = [[0 for _ in range(M)] for _ in range(N)]
    for y in range(N):
        for x in range(M):
            if (x == 0 or y == 0 or x == M-1 or y == N-1) and visit[y][x]== 0:
                pan[y][x] = max(pan[y][x]-1, 0)
                visit[y][x] = 1

    # print("=====> 3. 외곽선 온도계산")
    # for y in pan:
    #     print(y)

    ans += 1





