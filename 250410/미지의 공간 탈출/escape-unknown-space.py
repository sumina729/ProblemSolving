
from collections import defaultdict
from collections import deque

def add_edge(grahp, a, b):
    grahp[a].append(b)
    grahp[b].append(a)

def make_connect(sx, sy): #정육면체 시작 위치 왼쪽위
    global pan, buk, N, M


    '''
        connect_grahp: (벽번호, x, y) -> [(벽번호, x, y), (벽번호, x, y), (벽번호, x, y)]
        0, 1, 2, 3, 4 : 동 서 남 북 위
        5: 바닥 판
        총 6가지 반 종류
    '''
    connect_grahp = defaultdict(list)

     # 0, 1, 2, 3 => 동서남북
    buk_num = [0, 3, 1, 2]
    for i in range(4):
        for y in range(M):
            for x in range(M):
                # buk 0,1,2,3, 양옆 연결
                if x == M-1:
                    add_edge(connect_grahp, (buk_num[i], x, y), (buk_num[(i+1)%4], 0, y))

                # buk 0,1,2,3, 과 바닥 연경
                if y == M-1:
                    if buk_num[i] == 0: add_edge(connect_grahp, (buk_num[i], x, y), (5, sx+M, sy+M-x-1))
                    if buk_num[i] == 1: add_edge(connect_grahp, (buk_num[i], x, y), (5, sx-1, sy+x))
                    if buk_num[i] == 2: add_edge(connect_grahp, (buk_num[i], x, y), (5, sx+x, sy+M))
                    if buk_num[i] == 3: add_edge(connect_grahp, (buk_num[i], x, y), (5, sx+M-x-1, sy-1))


    # 위판이 양옆 연결
    for y in range(M):
        for x in range(M):
            # 0, 1, 2, 3 => 동서남북

            #동 0번 연결
            if x == M-1: add_edge(connect_grahp, (4, x, y), (0, M-y-1, 0))

            #서 1번 연결
            if x == 0: add_edge(connect_grahp, (4, x, y), (1, y, 0))

            #남 2번연결
            if y == M-1: add_edge(connect_grahp, (4, x, y), (2, x, 0))

            # 북 3번연결
            if y == 0: add_edge(connect_grahp, (4, x, y), (3, M-x-1, 0))

    return connect_grahp

def start_xy(pan, n):
    for y in range(len(pan)):
        for x in range(len(pan)):
            if pan[y][x] == n:
                return x, y


def time_check(visited, gumong, turm):

    new_gumong = []
    for tx, ty, td, tv in gumong:
        if turm % tv == 0: #배수이면
            nx = tx + dx[td]
            ny = ty + dy[td]

            if -1<nx<N and -1<ny<N and (pan[ny][nx] == 0):
                visited[5][ny][nx] = -2
                new_gumong.append([nx, ny, td, tv]) # 갱신되면 새롭개
            else:
                new_gumong.append([tx, ty, td, tv])
        else:
            new_gumong.append([tx, ty, td, tv])

    return new_gumong



def bfs(buk_num, x, y):
    global pan, buk, N, M, edge_connect, ex, ey, gumong #[x, y, d, v]
    visited = []

    for i in range(5):
        visited.append([[-1 for _ in range(M)]for _ in range(M)])
    visited.append([[-1 for _ in range(N)] for _ in range(N)])


    #시간의 벽 체크
    for tx, ty, td, tv in gumong:
        visited[5][ty][tx] = -2

    que = deque()
    que.append((buk_num, x, y))
    visited[buk_num][y][x] = 0

    while que:
        buk_num, x, y = que.popleft()
        turn = visited[buk_num][y][x] + 1

        #이동하기전에 시간의 벽 이 및 체크 -2로 지정
        gumong = time_check(visited, gumong, turn)

        #범위 내 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if buk_num == 5 and -1<nx<N and -1<ny<N and visited[buk_num][ny][nx] == -1 and (pan[ny][nx] == 0 or pan[ny][nx] == 4): #바닥판 내에서 이동
                que.append((buk_num, nx, ny))
                visited[buk_num][ny][nx] = turn

            elif not buk_num == 5 and -1<nx<M and -1<ny<M and visited[buk_num][ny][nx] == -1 and buk[buk_num][ny][nx] == 0: #벽들 내에서 이동
                que.append((buk_num, nx, ny))
                visited[buk_num][ny][nx] = turn

        #벽이면 엣지 이동
        if not buk_num == 5:
            #벽인데 엣지 이면
            if x == 0 or x == M-1 or y == 0 or y == M-1:
                if (buk_num, x, y) in edge_connect:
                    edge_connect_list = edge_connect[(buk_num, x, y)]

                    for tb, tx, ty in edge_connect_list:
                        # print(tb, tx, ty)
                        if visited[tb][ty][tx] == -1:
                            if (not tb == 5 and buk[tb][ty][tx] == 0) or (tb == 5 and (pan[ty][tx] == 0 or pan[ty][tx] == 4)) :
                                que.append((tb, tx, ty))
                                visited[tb][ty][tx] = turn


    # print("윗판")
    # for y in visited[4]:
    #     print(y)
    #
    # print("남쪽판")
    # for y in visited[2]:
    #     print(y)
    #
    # print("동쪽판")
    # for y in visited[0]:
    #     print(y)
    #
    # print("바닥판")
    # for y in visited[5]:
    #     print(y)

    return visited[5][ey][ex]








# 0, 1, 2, 3 => 동서남북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N, M, F = map(int, input().split()) #평면, 벽, 이상현상
pan = [list(map(int, input().split())) for _ in range(N)] #평면도 판
buk = []

for _ in range(5): #벽 5개
    tmp = [list(map(int, input().split())) for _ in range(M)]  #벽 하나 입력받기
    buk.append(tmp) # 0, 1, 2, 3 => 동서남북

gumong = []
for _ in range(F):
    y, x, d, v = map(int, input().split())
    gumong.append([x, y, d, v])

# print()

ex, ey = start_xy(pan, 4)
#판에서 정육각형 시작 구해주기
sx, sy = start_xy(pan, 3)
# print("판(5번): ",sx, sy)

#엣지 연결하기
edge_connect = make_connect(sx, sy)

sx, sy = start_xy(buk[4], 2)
# print("벽(4번): ",sx, sy)

#탐색하기
ans = bfs(4, sx, sy)
print(ans)