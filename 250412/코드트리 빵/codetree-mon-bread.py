import sys
sys.stdin = open("input.txt","r")


def get_dist(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

def go_basecamp(man_i):
    global N, pan, want_store_list

    min_dist = N+N
    min_y = -1
    min_x = -1
    #가장 가까운 베이스 캠프 챁기
    for y in range(N):
        for x in range(N):
            if pan[y][x] == 1: #못가는 베이으 캠프는 2
                sx, sy = want_store_list[man_i][0], want_store_list[man_i][1]
                dist = get_dist(sx, sy, x, y)

                if min_dist > dist:
                    min_dist = dist
                    min_y = y
                    min_x = x
                elif dist == min_dist and min_y > y:
                    min_dist = dist
                    min_y = y
                    min_x = x
                elif dist == min_dist and min_y == y and min_x > x:
                    min_dist = dist
                    min_y = y
                    min_x = x

    pan[min_y][min_x] = 2 #베이스 캠프 더이상 못감
    pan_man[man_i] = [min_x, min_y] #사람 초기 위치

#상좌우하
dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]
def move_man(man_i):
    global N, pan_man, want_store_list, pan
    min_dist = N + N
    di = -2
    sx, sy = pan_man[man_i][0], pan_man[man_i][1]

    for i in range(4):
        nx = sx+dx[i]
        ny = sy+dy[i]

        if -1<nx<N and -1<ny<N and not pan[ny][nx] ==2:
            dist = get_dist(nx, ny, want_store_list[man_i][0], want_store_list[man_i][1]) #원하는 편의점과의 거리
            if min_dist > dist:
                min_dist = dist
                di = i

    if not di == -2:
        go_x = sx+dx[di]
        go_y = sy+dy[di]
        pan_man[man_i] = [go_x, go_y]
        # print(man_i, "번 사람 ", pan_man[man_i], "로 이동")



    return go_x, go_y

def move_all_man():
    global N, pan, want_store_list, pan_man_i_list, pan_man
    dochak_list = []

    for i in pan_man_i_list:
        go_x, go_y = move_man(i)

        # 간 곳이 편의점이면
        if go_x == want_store_list[i][0] and go_y == want_store_list[i][1]:
            pan_man_i_list.remove(i) # 판에서 빼기
            dochak_list.append(i) # 도착에 넣게

    for i in dochak_list:
        x, y = pan_man[i][0], pan_man[i][1]
        pan[y][x] = 2



N, M = map(int, input().split()) #판크기, 사람수
pan = [list(map(int, input().split())) for _ in range(N)] # 막힌 부분은 2, 1 배이스 캠프
want_store_list = []
for _ in range(M):
    y, x = map(int, input().split())
    want_store_list.append([x-1, y-1])
pan_man = [[-1, -1] for _ in range(M)] # 위치 저장
pan_man_i_list = [] #현재 판에 있는 사람 넘버


turn = -1
while True:
    turn +=1 #0턴 부터 시작

    move_all_man()


    if turn < M:
        # 3이동
        pan_man_i_list.append(turn)
        go_basecamp(turn)
        # print(turn, "의 초기 위치", pan_man[turn])

    # print("판에 있는 사람 번호등", pan_man_i_list)
    # print("판에 있는 사람 위치득", pan_man)
    # for y in pan:
    #     print(y)

    # print()

    if turn >= M and len(pan_man_i_list) == 0:
        print(turn)
        break

    # if turn == 7:
    #     break