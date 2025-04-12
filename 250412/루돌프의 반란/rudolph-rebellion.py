'''
8시 50분 시작
9시 10분 코드 시작
'''

import sys
sys.stdin = open('input.txt', 'r')

def search_santa(ry, rx):
    global santa_nxy, tarak_santa_n, N, P

    min_dist = N**2+N**2
    min_n = -1
    max_y = -1
    max_x = -1
    for n in range(P):
        x, y = santa_nxy[n]
        if n not in tarak_santa_n:
            dist = abs(rx-x)**2+abs(ry-y)**2

            if dist < min_dist:
                min_dist = dist
                min_n = n
                max_y = y
                max_x = x
            elif dist == min_dist and max_y < y:
                min_dist = dist
                min_n = n
                max_y = y
                max_x = x
            elif dist == min_dist and max_y == y and max_x < x:
                min_dist = dist
                min_n = n
                max_y = y
                max_x = x

    return min_n, max_x, max_y

def sang_ho(santa_n, cx, cy, d_i):
    N, santa_nxy, tarak_santa_n
    n = santa_n

    # print(santa_n, "번 싼타 밀쳐짐", d_i)
    for i in range(P):
        sx, sy = santa_nxy[i]
        if not n == i and cx == sx and cy == sy: #자기자신이 아닌 다른게 들어가 있으면
            # print(i, "번 그자리에 있음")
            nx = santa_nxy[i][0] +dx[d_i]
            ny = santa_nxy[i][1] +dy[d_i]
            # print(i, "번 ", nx, ny, "로 밀림")

            if -1 < nx < N and -1 < ny < N:
                santa_nxy[i][0] = nx
                santa_nxy[i][1] = ny
                # 상호작용
                sang_ho(i, nx, ny, d_i)
            else:
                # print(i, "번 싼타 탈락")
                santa_nxy[i][0] = -1
                santa_nxy[i][1] = -1
                tarak_santa_n.add(i)
            break



def dump(santa_n, d_i, jumsu):
    global N, santa_nxy, santa_jumsu, gijul_santa, tarak_santa_n

    #점수 얻기
    santa_jumsu[santa_n] += jumsu

    #이동하기 d_i방향으로 jumsu 만큼
    nx = santa_nxy[santa_n][0] + dx[d_i]*jumsu
    ny = santa_nxy[santa_n][1] + dy[d_i]*jumsu

    # 기절하기
    gijul_santa[santa_n] = 2

    if -1<nx<N and -1<ny<N:
        santa_nxy[santa_n][0] = nx
        santa_nxy[santa_n][1] = ny

        #상호작용
        sang_ho(santa_n, nx, ny, d_i)

    else:
        #탈락
        # print(santa_n, "번 싼타 탈락")
        # print(santa_n, "번 싼타 밀쳐텨 탈락")
        santa_nxy[santa_n][0] = -1
        santa_nxy[santa_n][1] = -1
        gijul_santa[santa_n] = 0
        tarak_santa_n.add(santa_n)


#상우하좌
dx = [0, 1, 0, -1, -1, 1, 1, -1]
dy = [-1, 0, 1, 0,  1, -1, 1, -1]

def search_d_i(ry, rx, santa_x, santa_y):
    global N
    min_dist = N**2 + N**2
    d_i = -2

    for i in range(8):
        ny = ry+dy[i]
        nx = rx + dx[i]

        if -1<nx<N and -1<ny<N:
            dist = abs(santa_x-nx)**2+abs(santa_y-ny)**2
            if dist < min_dist:
                min_dist = dist
                d_i = i
    return d_i

def move_rudolpu():
    global N, santa_nxy, ry, rx, C

    #탈락 하지 않은 산타 중에서 가장 가까운 싼타 번호 찾기
    santa_n, santa_x, santa_y = search_santa(ry, rx)
    # print("루돌푸랑 가장 가까운 싼타: ", santa_n, santa_x, santa_y)

    d_i = search_d_i(ry, rx, santa_x, santa_y)

    #방향으로 이동
    ry = ry + dy[d_i]
    rx = rx + dx[d_i]
    # print("방향으로 이동: ", d_i, rx, ry, santa_x, santa_y)

    #만약 산타 밀쳐지기
    if ry == santa_y and rx == santa_x:
        # print(santa_n, "번 싼타 밀쳐짐")
        dump(santa_n, d_i, C)

def is_no_snata(santa_n, nx, ny):
    global santa_nxy, P

    for i in range(P):
        sx, sy = santa_nxy[i][0], santa_nxy[i][1]
        # print(i, "번 싼타 있는지 확인", nx, ny, sx, sy)
        if nx == sx and ny == sy:
            # print(i,"번 싼타 때문에 못감", nx, ny, sx, sy)
            return False

    return True

def move_santa(santa_n, santa_x, santa_y):
    global N, ry, rx, D, santa_nxy

    min_dist = abs(rx-santa_x)**2+abs(ry-santa_y)**2
    # print(santa_n, "번싼타", "처음 누돌푸와 거리", min_dist)
    d_i = -1
    # print("이동전: ", santa_x, santa_y)
    for i in range(4):
        nx = santa_x+dx[i]
        ny = santa_y+dy[i]


        if -1<nx<N and -1<ny<N and is_no_snata(i, nx, ny):

            dist = abs(rx-nx)**2+abs(ry-ny)**2
            # print(santa_n, "번싼타", i, "방향 체크", dist)

            if dist < min_dist:
                min_dist = dist
                d_i = i

    if d_i > -1:
        santa_nxy[santa_n][0] = santa_x = santa_x + dx[d_i]
        santa_nxy[santa_n][1] = santa_y = santa_y + dy[d_i]

    # print("이동후: ", santa_x, santa_y)
    # print(rx, ry, santa_x, santa_y)
    if ry == santa_y and rx == santa_x:

        #반대방향 계산
        if d_i == 0 : d_i = 2
        elif d_i == 1: d_i = 3
        elif d_i == 2: d_i = 0
        else: d_i = 1

        # print("밀쳐지자")
        dump(santa_n, d_i, D)



def move_all_santa():
    global santa_nxy, P, tarak_santa_n, gijul_santa

    for i in range(P):

        #탈락한 산타이거나, 기절이면 이동 x
        if i in tarak_santa_n or gijul_santa[i]>0:
            # print(i, "산타 이동 X")
            continue
        else:
            # print(i, "산타 이동")
            move_santa(i, santa_nxy[i][0], santa_nxy[i][1])

#판, 턴, 산타, 점수1, 점수2
N, M, P, C, D = map(int, input().split())
ry, rx = map(int, input().split())
ry -=1
rx -=1

santa_nxy = [[] for _ in range(P)]
santa_jumsu = [0 for _ in range(P)] #0번 인덱스 사용 안함
gijul_santa = [0 for _ in range(P)]

for _ in range(P):
    n, y, x = map(int, input().split())
    santa_nxy[n-1] = [x-1, y-1]

tarak_santa_n = set()


for m in range(M):
    # print()
    # print()

    # print("==초기산타 상태==")
    # print("루돌푸: ", rx, ry)
    # print("산타점수: ", santa_jumsu)
    # print("산타위치: ", santa_nxy)
    # print("산타기절: ", gijul_santa)
    # print("산타탈락: ", tarak_santa_n)
    if len(tarak_santa_n) == P:
        break

    # for y in range(N):
    #     for x in range(N):
    #         if [x,y] in santa_nxy:
    #             for i in range(P):
    #                 if santa_nxy[i][0] == x and santa_nxy[i][1] == y:
    #                     print(i, end=" ")
    #         elif rx == x and ry==y:
    #             print("R", end=" ")
    #         else:
    #             print("-", end=" ")
    #     print()

    for i in range(P):
        gijul_santa[i] = max(0, gijul_santa[i] -1)

    # print("==루돌푸 이동후 산타 상태==")
    move_rudolpu()

    # print("루돌푸: ", rx, ry)
    # print("산타점수: ", santa_jumsu)
    # print("산타위치: ", santa_nxy)
    # print("산타기절: ", gijul_santa)
    # print("산타탈락: ", tarak_santa_n)

    # for y in range(N):
    #     for x in range(N):
    #         if [x, y] in santa_nxy:
    #             for i in range(P):
    #                 if santa_nxy[i][0] == x and santa_nxy[i][1] == y:
    #                     print(i, end=" ")
    #         elif rx == x and ry==y:
    #             print("R", end=" ")
    #         else:
    #             print("-", end=" ")
    #
    #     print()

    # print("==산타 이동후 산타 상태==")
    move_all_santa()
    # print("루돌푸: ", rx, ry)
    # print("산타점수: ", santa_jumsu)
    # print("산타위치: ", santa_nxy)
    # print("산타기절: ", gijul_santa)
    # print("산타탈락: ", tarak_santa_n)

    # for y in range(N):
    #     for x in range(N):
    #         if [x, y] in santa_nxy:
    #             for i in range(P):
    #                 if santa_nxy[i][0] == x and santa_nxy[i][1] == y:
    #                     print(i, end=" ")
    #         elif rx == x and ry==y:
    #             print("R", end=" ")
    #         else:
    #             print("-", end=" ")
    #     print()

    for i in range(P):
        if not i in tarak_santa_n:
            santa_jumsu[i]+=1

    # print(santa_jumsu)

print(*santa_jumsu)

    # break