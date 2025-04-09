from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

#짧은 결로 찾기
def bfs(x, y):
    global visit, pan, ex,ey, mx, my
    que = deque()
    que.append((x, y))


    # tmp_pan = [[[] for _ in range(N)] for _ in range(N)]
    tmp_pan = [[None for _ in range(N)] for _ in range(N)]
    visit[y][x] = 1

    while que:
        x , y = que.popleft()

        if x == ex and y == ey:
            break
        for i in [0, 1, 2, 3]:
            nx = x + dx[i]
            ny = y + dy[i]

            if -1<nx<N and -1<ny<N and visit[ny][nx] == 0 and pan[ny][nx] == 0:
                visit[ny][nx] = 1
                que.append((nx, ny))
                tmp_pan[ny][nx] = [x, y]

    path = []
    x, y = ex,ey

    if visit[y][x] == 0:
        return -1

    while True:
        if x == mx and y == my:
            break
        path.append((x, y))
        x, y = tmp_pan[y][x]

    path.reverse()

    return path

def junsa_check(jx, jy, d, see_pan):
    global mx, my

    sx =jx
    sy =jy
    n = 1
    # print("메두사2", jx, jy, mx, my, d)
    if d == 0 or d == 1:
        if jx == mx:
            #방향 한줄만체크
            while True:
                sx = sx + dx[d]
                sy = sy + dy[d]
                if -1 < sx < N and -1 < sy < N:
                    # print(sx, sy)
                    see_pan[sy][sx] = -1
                else:
                    break
        elif jx < mx:
            while True:
                sx = sx + dx[d]
                sy = sy + dy[d]
                if -1 < sx < N and -1 < sy < N:
                    see_pan[sy][sx] = -1
                else:
                    break

                for i in range(1, n + 1):
                    # 왼쪽
                    sxx = sx + dx[2] * i
                    syy = sy + dy[2] * i
                    # print("옆1", sxx, syy)
                    if -1 < sxx < N and -1 < syy < N and not see_pan[syy][sxx] == -1:
                        see_pan[syy][sxx] = -1

                n += 1
        elif jx > mx:
            while True:
                sx = sx + dx[d]
                sy = sy + dy[d]
                if -1 < sx < N and -1 < sy < N:
                    see_pan[sy][sx] = -1
                else:
                    break

                for i in range(1, n + 1):
                    # 왼쪽
                    sxx = sx + dx[3] * i
                    syy = sy + dy[3] * i
                    # print("옆1", sxx, syy)
                    if -1 < sxx < N and -1 < syy < N and not see_pan[syy][sxx] == -1:
                        see_pan[syy][sxx] = -1

                n += 1



    elif d == 2 or d == 3:
        # 방향 한줄만체크
        if jy == my:
            while True:
                sx = sx + dx[d]
                sy = sy + dy[d]
                if -1 < sx < N and -1 < sy < N:
                    see_pan[sy][sx] = -1
                else:
                    break
        elif jy < my:
            while True:
                sx = sx + dx[d]
                sy = sy + dy[d]
                if -1 < sx < N and -1 < sy < N:
                    see_pan[sy][sx] = -1
                else:
                    break

                for i in range(1, n + 1):
                    # 왼쪽
                    sxx = sx + dx[0] * i
                    syy = sy + dy[0] * i
                    # print("옆1", sxx, syy)
                    if -1 < sxx < N and -1 < syy < N and not see_pan[syy][sxx] == -1:
                        see_pan[syy][sxx] = -1

                n += 1
        elif jy > my:
            while True:
                sx = sx + dx[d]
                sy = sy + dy[d]
                if -1 < sx < N and -1 < sy < N:
                    see_pan[sy][sx] = -1
                else:
                    break

                for i in range(1, n + 1):
                    # 왼쪽
                    sxx = sx + dx[1] * i
                    syy = sy + dy[1] * i
                    # print("옆1", sxx, syy)
                    if -1 < sxx < N and -1 < syy < N and not see_pan[syy][sxx] == -1:
                        see_pan[syy][sxx] = -1

                n += 1

def see(mx, my, d):

    see_pan = [[0 for _ in range(N)] for _ in range(N)]
    junsa_dol = []

    n  = 1
    cnt = 0

    sx = mx
    sy = my

    if d == 0: d_both = [2, 3]
    if d == 1: d_both = [2, 3]
    if d == 2: d_both = [0, 1]
    if d == 3: d_both = [0, 1]

    while True:

        #방향대로 직진.
        sx = sx+ dx[d]
        sy = sy+ dy[d]

        # print(sx, sy)
        if -1<sx<N and -1<sy<N:
            if not see_pan[sy][sx] == -1:
                see_pan[sy][sx] = 1
                if [sx, sy] in m_list:
                    cnt+=1
                    see_pan[sy][sx] = 2
                    junsa_dol.append([sx, sy])
                    junsa_check(sx, sy, d, see_pan)
                    # see_pan[sy][sx] = 2

        else:
            break

        for i in range(1, n+1):
            #왼쪽
            sxx = sx + dx[d_both[1]]*i
            syy = sy + dy[d_both[1]]*i
            # print("옆1", sxx, syy)
            if -1 < sxx < N and -1 < syy < N and not see_pan[syy][sxx] == -1:
                see_pan[syy][sxx] = 1
                if [sxx, syy] in m_list:
                    cnt += 1
                    see_pan[syy][sxx] = 2
                    junsa_dol.append([sxx, syy])
                    # print("메두사1", sxx, syy)
                    junsa_check(sxx,syy, d, see_pan)
                    # see_pan[syy][sxx] = 2

            #오른쪽
            sxx = sx + dx[d_both[0]]*i
            syy = sy + dy[d_both[0]]*i
            # print("옆2", sxx, syy)
            if -1 < sxx < N and -1 < syy < N and not see_pan[syy][sxx] == -1:
                see_pan[syy][sxx] = 1
                if [sxx, syy] in m_list:
                    cnt += 1
                    see_pan[syy][sxx] = 2
                    junsa_dol.append([sxx, syy])
                    # print("메두사1", sxx, syy)
                    junsa_check(sxx,syy, d, see_pan)

        n+=1

    # print("시선", d, "개수", cnt)
    # for y in see_pan:
    #     print(y)
    return cnt, junsa_dol, see_pan

def see_all(x, y):
    max_cnt = -1
    max_d = -1
    junsa_dol = [[]]
    see_pan = [[]]
    for i in range(4):
        n, tmp1, tmp2 = see(x, y, i)
        if max_cnt<n:
            max_cnt = n
            max_d =i
            junsa_dol = tmp1[:]
            see_pan = tmp2[:]


    # print(max_d, max_cnt, junsa_dol)
    return max_cnt, junsa_dol, see_pan
    #가장 많이 돌 되는거


def move_junsa(x, y, see_sun):
    global mx, my

    # print("전사 이동 시작", x, y)

    move_n = 0

    min_x = x
    min_y = y
    min_d = abs(x-mx)+abs(y-my)


    for i in [0, 1, 2, 3]:
        nx = x + dx[i]
        ny = y + dy[i]

        if -1<nx<N and -1<ny<N and not (see_sun[ny][nx]==1 or see_sun[ny][nx]==2):
            d = abs(nx-mx)+abs(ny-my)
            if d<min_d:
                move_n+=1
                min_x = nx
                min_y = ny
                min_d = d
    x = min_x
    y = min_y


    for i in [2, 3, 0, 1]:
        nx = x + dx[i]
        ny = y + dy[i]

        if -1 < nx < N and -1 < ny < N and not (see_sun[ny][nx] == 1 or see_sun[ny][nx] == 2):
            d = abs(nx - mx) + abs(ny - my)
            if d < min_d:
                move_n += 1
                min_x = nx
                min_y = ny
                min_d = d
    x = min_x
    y = min_y


    if min_x == mx and min_y == my:
        # print("전사 이동:", [min_x, min_y], "움직임수:", move_n, "메두사위치: ", mx, my, "메두사 공격여뷰", 0, "메두사에서 거리", min_d)
        return 1,  move_n, [min_x, min_y]
    else:
        # print("전사 이동:", [min_x, min_y], "움직임수:", move_n, "메두사위치: ", mx, my, "메두사 공격여뷰", 1, "메두사에서 거리", min_d)
        return 0, move_n, [min_x,min_y]



def move_All_junsa(dol, see_sun):

    new_m_list = []
    move_n = 0
    atec_n = 0

    # print("최종 시선", )
    global m_list
    for x, y in m_list:
        if not [x, y] in dol:
            # print("이동할 전사:", x, y)
            a, n, tmpl = move_junsa(x, y,see_sun)

            move_n+=n
            atec_n+=a

            if a==0:
                new_m_list.append(tmpl)
                # print("전사추가", new_m_list)

        else:
            # print("돌되서 못움직인 전사 전사:", x, y)
            new_m_list.append([x,y])
            # print("전사추가", new_m_list)

    # print("최종전사", new_m_list)
    return new_m_list, move_n, atec_n


#초기 입력
N, M = map(int, input().split()) #크기, 전사수
my, mx, ey, ex = map(int, input().split())
tmp = list(map(int, input().split()))

m_list = []
for i in range(M):
    # m_list.append(tmp[i*2: i*2+2]) #y, x 순
    m_list.append([tmp[i*2+1], tmp[i*2]])

pan = [list(map(int, input().split())) for _ in range(N)]
visit = [[0 for _ in range(N)] for _ in range(N)]

m_route = []
m_route_n = N*N
dol = [[]]

#입력확인
# print(N, M)
# print(my, mx, ey, ex)
# print(m_list)
# for y in pan:
#     print(y)

# 경로 찾기
path = bfs(mx, my)
if path == -1:
    print("-1")

# print("공원가는 경로")
# print(len(path), path)

for mx, my in path:

    # print()
    # print()
    # print("턴 시작", mx, my)

    if mx == ex and my == ey:
        print(0)
        break
    ans_move = 0
    ans_dol = 0
    ans_atec = 0

    nuw_m = []
    for i in range(len(m_list)):
        ax, ay = m_list[i]
        if not (mx==ax and my ==ay):
            nuw_m.append([ax,ay])
    m_list = nuw_m[:]
    # print("메두사 욺직이고 최종 전사")
    # print(m_list)


    #메두사 회전 하며서 돌로 만들수 있는 거 확인
    dol_n, dol, see_sun = see_all(mx, my)
    # print("돌된 매두사 개수랑 배열: ",dol_n, dol)
    ans_dol+=dol_n

    # print("메두사와 전사 위치")
    # for y in range(N):
    #     for x in range(N):
    #         if y == my and x == mx:
    #             print(3, end=" ")
    #         elif [x, y] in m_list:
    #             print(2, end=" ")
    #         elif see_sun[y][x] == 1:
    #             print(1, end=" ")
    #         else:
    #             print(0, end=" ")
    #     print()

    #전시 욺직이기,
    # print('총전사', m_list)
    m_list, m, a = move_All_junsa(dol, see_sun) #new_m_list, move_n, atec_n
    # print("최최종 저사", m_list)
    ans_move+=m
    ans_atec+=a

    # print("================답")
    # print("욺직인 전사수:", ans_move)
    # print("돌이 된 전사수:", ans_dol)
    # print("메두사를 공격한 전사수:", ans_atec)
    # print("================")
    print(ans_move, ans_dol, ans_atec)
    # break

# dol_n, dol = see_all(2, 0) # 될된 수, 돌외 있는 전사 위치
