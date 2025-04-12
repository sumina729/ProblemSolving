#상우하좌
dx = [0, 1, 0, -1, -1, 1, 1, -1]
dy = [-1, 0, 1, 0,  1, -1, 1, -1]

#사슴이랑 가장 가까운 산타계산, 가장 가까운 싼타의 번호 및 위치 리턴
def search_santa(ry, rx):
    global santa_nxy, tarak_santa_n, N, P

    min_dist = N**2+N**2
    min_n = -1
    max_y = -1
    max_x = -1
    for n in range(P):
        x, y = santa_nxy[n]
        if n not in tarak_santa_n: #탈란 하지 않은 산타 중에서 만 확인
            dist = abs(rx-x)**2+abs(ry-y)**2 #거리 계싼

            #우선순위 계산
            if (dist < min_dist) or (dist == min_dist and max_y < y) or (dist == min_dist and max_y == y and max_x < x):
                min_dist = dist
                min_n = n
                max_y = y
                max_x = x

    return min_n, max_x, max_y

# 그 위치에 산타가 있는지 체크하고 상호작용 하는 함수
def sang_ho(santa_n, cx, cy, d_i):
    N, santa_nxy, tarak_santa_n
    n = santa_n

    for i in range(P):
        sx, sy = santa_nxy[i]
        if not n == i and cx == sx and cy == sy: # 이동한 cx, cy 위치에 다른게 있는지 확인

            # 그럼 한칸 미룸
            nx = santa_nxy[i][0] +dx[d_i]
            ny = santa_nxy[i][1] +dy[d_i]

            if -1 < nx < N and -1 < ny < N: #범위 내에 있으면, 그자 다른 산카가 있는지 확인하고 이 반복 계속

                # 범위 내이면 넣어주기
                santa_nxy[i][0] = nx
                santa_nxy[i][1] = ny

                sang_ho(i, nx, ny, d_i)

            else: #밀쳐지고 범위내에 없으면  타락
                santa_nxy[i][0] = -1
                santa_nxy[i][1] = -1
                gijul_santa[i] = 0
                tarak_santa_n.add(i)

            break #1개 밖에 없으니깐 한번 찾으면 즉시 종룍

#충동 함수
def dump(santa_n, d_i, jumsu):
    global N, santa_nxy, santa_jumsu, gijul_santa, tarak_santa_n

    #충동한 싼타 점수 얻기
    santa_jumsu[santa_n] += jumsu

    #이동하기 d_i방향으로 jumsu 만큼
    nx = santa_nxy[santa_n][0] + dx[d_i]*jumsu
    ny = santa_nxy[santa_n][1] + dy[d_i]*jumsu

    # 기절하기
    gijul_santa[santa_n] = 2

    if -1<nx<N and -1<ny<N: # 이동 한곳이 범위 내이면 이동
        santa_nxy[santa_n][0] = nx
        santa_nxy[santa_n][1] = ny

        #상호작용
        sang_ho(santa_n, nx, ny, d_i)

    else: # 범위 밖이면 탈란

        #탈락 체크 세팅
        santa_nxy[santa_n][0] = -1
        santa_nxy[santa_n][1] = -1
        gijul_santa[santa_n] = 0
        tarak_santa_n.add(santa_n)

# 싼타에게 가장 가까이 갈 수 있는 방향 받기
def search_d_i(ry, rx, santa_x, santa_y):
    global N
    min_dist = N**2 + N**2
    d_i = -2

    for i in range(8):
        ny = ry+dy[i]
        nx = rx + dx[i]

        if -1<nx<N and -1<ny<N: #범위 체크
            dist = abs(santa_x-nx)**2+abs(santa_y-ny)**2
            if dist < min_dist:
                min_dist = dist
                d_i = i
    return d_i

#루돌푸 이동 함수
def move_rudolpu():
    global N, santa_nxy, ry, rx, C

    #탈락 하지 않은 산타 중에서 가장 가까운 싼타 번호 찾기
    santa_n, santa_x, santa_y = search_santa(ry, rx)

    #가까운 싼타에게 가장 가까이 갈 수 있는 방향 받기
    d_i = search_d_i(ry, rx, santa_x, santa_y)

    #방향으로 이동
    ry = ry + dy[d_i]
    rx = rx + dx[d_i]

    #만약 사슴이 간 곳에 싼타가 있으면, 산타 밀쳐지기
    if ry == santa_y and rx == santa_x:
        #충동 함수
        dump(santa_n, d_i, C)

def is_no_snata(santa_n, nx, ny):
    global santa_nxy, P

    for i in range(P):
        sx, sy = santa_nxy[i][0], santa_nxy[i][1]
        if nx == sx and ny == sy:
            return False

    return True

def move_santa(santa_n, santa_x, santa_y):
    global N, ry, rx, D, santa_nxy

    min_dist = abs(rx-santa_x)**2+abs(ry-santa_y)**2
    d_i = -1

    for i in range(4):
        nx = santa_x+dx[i]
        ny = santa_y+dy[i]


        if -1<nx<N and -1<ny<N and is_no_snata(i, nx, ny):

            dist = abs(rx-nx)**2+abs(ry-ny)**2

            if dist < min_dist:
                min_dist = dist
                d_i = i

    if d_i > -1:
        santa_nxy[santa_n][0] = santa_x = santa_x + dx[d_i]
        santa_nxy[santa_n][1] = santa_y = santa_y + dy[d_i]

    if ry == santa_y and rx == santa_x:

        #반대방향 계산
        if d_i == 0 : d_i = 2
        elif d_i == 1: d_i = 3
        elif d_i == 2: d_i = 0
        else: d_i = 1

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

    #다 차락이면 즉시 종료
    if len(tarak_santa_n) == P:
        break

    #기절한거 시간계산
    for i in range(P):
        gijul_santa[i] = max(0, gijul_santa[i] -1)

    #사슴이동
    move_rudolpu()

    #산타이동
    move_all_santa()

    #남은 산타 점수 계산
    for i in range(P):
        if not i in tarak_santa_n:
            santa_jumsu[i]+=1

print(*santa_jumsu)