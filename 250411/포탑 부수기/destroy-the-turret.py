# import sys
# sys.stdin = open("input.txt", "r")

from collections import deque

#남아있는 포탑 구하는 함수
def potop_pan_cnt(potop_pan):
    cnt = 0
    for y in range(N):
        for x in range(M):
            if potop_pan[y][x] > 0:
                cnt+=1
    # print("남은 포탑 수: ",cnt)
    return cnt

#공경포탑, 공경받는포탑 구하는 함수
def search_attack(potop_pan, potop_pan_go_num, chek):
    global N, M, K
    if chek == 0:
        m_n = 5001
        m_gn = -1
        m_xy = -1
        m_x = -1
        m_y = -1
    else:
        m_n = -1
        m_gn = K+1
        m_xy = M+N
        m_x = M
        m_y = N

    for y in range(N):
        for x in range(M):
            n = potop_pan[y][x]
            gn = potop_pan_go_num[y][x]
            tmp_xy = x+y
            tmp_x = x

            if n > 0:
                if chek == 0:
                    if m_n > n or (m_n == n and m_gn < gn) or (m_n == n and m_gn == gn and m_xy < tmp_xy) or (m_n == n and m_gn == gn and m_xy == tmp_xy and m_x < tmp_x): #공격이 작으면
                        m_n = n
                        m_gn = gn
                        m_xy = tmp_xy
                        m_x = tmp_x
                        m_y = y
                elif chek == 1:
                    if m_n < n or (m_n == n and m_gn > gn) or (m_n == n and m_gn == gn and m_xy > tmp_xy) or (m_n == n and m_gn == gn and m_xy == tmp_xy and m_x > tmp_x): #공격이 작으면
                        m_n = n
                        m_gn = gn
                        m_xy = tmp_xy
                        m_x = tmp_x
                        m_y = y

    return m_x, m_y

#공격경로 구하는 함수
def bfs(sx, sy, ex, ey):
    #우하좌상, 포탑이 0보다 큰곳, 방문 안한곳, 벽끼리 이어져있음
    global N, M, potop_pan
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # 우하좌상
    visited = [[0 for _ in range(M)] for _ in range(N)]
    prve = [[[] for _ in range(M)] for _ in range(N)]
    peth = []

    que = deque()
    que.append((sx, sy))
    visited[sy][sx] = 1

    while que:
        x, y = que.popleft()

        for i in [0, 1, 2, 3]:

            #범위체크 따로 필요 없음
            nx = (x+dx[i])%M
            ny = (y+dy[i])%N

            if potop_pan[ny][nx] > 0 and visited[ny][nx] == 0:
                que.append((nx, ny))
                visited[ny][nx] = visited[y][x]+1
                prve[ny][nx] = [x, y]
    #경로 없으면 리턴
    if visited[ey][ex] == 0:
        return -1

    peth.append((ex, ey))
    while True:
        ex, ey = prve[ey][ex]
        if ex == sx and ey == sy:
            break
        peth.append((ex, ey))

    peth = peth[::-1]

    return peth

#레이저 공격 함수
def reiser_att(sx, sy, ex, ey, path):
    global N, M, potop_pan
    att_list = set()

    # print("레이저 공격")
    a = potop_pan[sy][sx]
    for nx, ny in path:
        if nx == ex and ny == ey:
            potop_pan[ny][nx] = potop_pan[ny][nx]-a
        else:
            potop_pan[ny][nx] = potop_pan[ny][nx] - a//2

        att_list.add((nx, ny))

    return att_list

#포탄공격 함수
def potop_att(sx, sy, ex, ey):
    global N, M, potop_pan
    dx = [1, 0, -1, 0, -1, 1, -1, 1]
    dy = [0, 1, 0, -1, -1, 1, 1, -1]

    att_list = set()
    a = potop_pan[sy][sx]

    # print("포탑 공격")
    potop_pan[ey][ex] = potop_pan[ey][ex] - a
    att_list.add((ex, ey))
    for i in range(8):
        # 범위체크 따로 필요 없음
        nx = (ex + dx[i]) % M
        ny = (ey + dy[i]) % N

        if not (ny == sy and nx == sx)and potop_pan[ny][nx] > 0:
            potop_pan[ny][nx] = potop_pan[ny][nx] - a // 2
            att_list.add((nx, ny))

    return att_list

#공격 함수
def potop_attack(s_x, s_y, e_x, e_y):
    #레이저 공격 가능한지 체크
    path = bfs(s_x, s_y, e_x, e_y)
    if path == -1:
        #2. 포탑 공격
        att_list = potop_att(s_x, s_y, e_x, e_y)
    else:
        #1레이저 공격
        att_list = reiser_att(s_x, s_y, e_x, e_y, path)

    return att_list

#탑정비, 공력력 추가해주는 함수
def add_gonguk(att_list, sx, sy):
    global N, M, potop_pan

    for y in range(N):
        for x in range(M):
            if not (y == sy and x == sx) and not (x, y) in att_list and potop_pan[y][x] > 0:
                potop_pan[y][x] = potop_pan[y][x]+1

#탑 최대 갯수 구하는 함수
def max_potop():
    global N, M, potop_pan
    ans = 0
    for y in range(N):
        for x in range(M):
            ans = max(potop_pan[y][x], ans)

    return ans


#메인
N, M, K = map(int, input().split())
potop_pan = [list(map(int, input().split()))for i in range(N)]
potop_pan_go_num = [[0 for _ in range(M)] for _ in range(N)]

for k in range(K):
    if potop_pan_cnt(potop_pan) == 1:
        # 1개 이므로 즉시 종료
        break

    s_x, s_y  = search_attack(potop_pan, potop_pan_go_num, 0) #공격포탑 찾기
    e_x, e_y = search_attack(potop_pan, potop_pan_go_num, 1) #공격당할 포탑 찾기

    #공격자에게 공경력 추가
    potop_pan[s_y][s_x] = potop_pan[s_y][s_x]+N+M

    #공격
    att_list = potop_attack(s_x, s_y, e_x, e_y) # s_x, s_y =>e_x, e_y

    #포탄정비
    add_gonguk(att_list, s_x, s_y)

    #공격날 갱신
    potop_pan_go_num[s_y][s_x] = k+1 #k번쨰 턴에 공격함

print(max_potop())