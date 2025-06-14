#8:55

import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

#상, 우, 하, 좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def is_in_pan(y, x):
    global N, M, K

    return -1<y< N and -1<x<N

def move_men(my, mx, md):
    global N, M, K

    ny = my + dy[md]
    nx = mx + dx[md]
    nd = md

    if is_in_pan(ny, nx):
        return ny, nx, nd

    # print("방향 바꿈")
    md = (md+2)%4

    ny = my + dy[md]
    nx = mx + dx[md]
    nd = md

    if is_in_pan(ny, nx):
        return ny, nx, nd

    print("이거 나오면 논리오류")
    return -1,-1,-1


def get_gi(cy, cx, ci, men_xyd_list):
    global N, M, K

    # cy, cx, cd = men_xyd_list[ci]

    for i in range(M):
        if i == ci: #자기 는 빼기
            continue

        y, x, d = men_xyd_list[i]
        if y == cy and x == cx: #무조건 한면 밖에 없음
            return i

    return -1

def get_chong(i, ny, nx, chong_pan, men_gong_list):
    global N, M, K

    chongs = chong_pan[ny][nx] #총이 무조건 있음.
    if men_gong_list[i][1] > 0: #사람이 총을 가지고 있으면
        chongs.append(men_gong_list[i][1]) #총 내려놓게

    chongs.sort()
    men_gong_list[i][1] = chongs.pop() #가장 큰거 하나얻기
    chong_pan[ny][nx] = chongs #가장큰거 하나뺸 리스트 바닥에

    # print(i, "사람이 얻은총 최종(자신, 총):", men_gong_list[i])
    # print(ny, nx, "바닥에 있는 총:",chong_pan[ny][nx])


def fight_m1_m2(m1, m2, men_xyd_list, men_gong_list, men_point_list, chong_pan, cy, cx):
    global N, M, K

    m1_gong = sum(men_gong_list[m1])
    m2_gong = sum(men_gong_list[m2])

    # print(m1, "번 공격력", men_gong_list[m1])
    # print(m2, "번 공격력", men_gong_list[m2])

    win_m = -1
    lose_m = -1

    if m1_gong > m2_gong:
        win_m = m1
        lose_m = m2
    elif m1_gong < m2_gong:
        win_m = m2
        lose_m = m1
    else: #같을때
        if men_gong_list[m1][0] > men_gong_list[m2][0]:
            win_m = m1
            lose_m = m2
        elif men_gong_list[m1][0] < men_gong_list[m2][0]:
            win_m = m2
            lose_m = m1

    if win_m == -1:
        print("논리오류")

    # print("이긴사람:", win_m)
    # print("진사람:", lose_m)

    # men_point_list[win_m] = abs(m1_gong-m2_gong)
    men_point_list[win_m] = men_point_list[win_m]+abs(m1_gong-m2_gong)
    # print(win_m,"번 사람 포인트 획득", men_point_list)



    #진사람 총두기
    if men_gong_list[lose_m][1] > 0: #총 있으면
        chong_pan[cy][cx].append(men_gong_list[lose_m][1])
        men_gong_list[lose_m][1] = 0

        # print(cy, cx, "위치의 총등", chong_pan[cy][cx])
        # print(lose_m, "번 사람의 총 ",men_gong_list[lose_m])
    # else:
        # print("진사람 총없음")

    #진사람 이동
    ly, lx,ld  = men_xyd_list[lose_m]
    for i in range(4):
        ndi  = (ld+i)%4
        ny = ly + dy[ndi]
        nx = lx + dx[ndi]

        if is_in_pan(ny, nx) and get_gi(ny, nx, lose_m, men_xyd_list) ==  -1:

            men_xyd_list[lose_m] = [ny, nx, ndi]
            # print(ly, lx, ld, "에서 진사람 이동완료", men_xyd_list[lose_m])

            if len(chong_pan[ny][nx]) > 0: #이동칸에 총있으면
                get_chong(lose_m, ny, nx, chong_pan, men_gong_list)
            break

    #이긴사람
    wy, wx, wd = men_xyd_list[win_m]
    if len(chong_pan[wy][wx]) > 0:  # 이동칸에 총있으면
        get_chong(win_m, wy, wx, chong_pan, men_gong_list)







#격자, 사람수, 라운드
N, M, K =  map(int, input().split())
tmp_pan = [list(map(int, input().split()))for _ in range(N)]
tmp_men = [list(map(int, input().split()))for _ in range(M)]


# print("N, M, K: ", N, M, K)

chong_pan = [[[] for _ in range(N)]for _ in range(N)]
# print("총 이 있는 판")
for y in range(N):
    for x in range(N):
        if tmp_pan[y][x] ==  0:
            continue
        chong_pan[y][x] = [tmp_pan[y][x]]
    # print(chong_pan[y])

men_xyd_list = []
men_gong_list = []
men_point_list = [0 for _ in range(M)]

for i in range(M):
    my,mx,md,ms = tmp_men[i]
    men_xyd_list.append([my-1, mx-1, md])
    men_gong_list.append([ms, 0])

# print("사람 위치[y, x, d]")
# print(men_xyd_list)
# print("사람 공격[초기능력, 총능력(총없으면0)]")
# print(men_gong_list)
# print("사람 포인트")
# print(men_point_list)


for k in range(K):
    # print("===============", k+1, "라운드 시작 ===============")

    for i in range(M): #1번부터 순서대로 이동

        # print("----",i, "번 사람이동----")
        my, mx, md = men_xyd_list[i]

        # print("이동전(my, mx, md):", my, mx, md)
        cy, cx, cd = move_men(my, mx, md)
        men_xyd_list[i] = [cy, cx, cd]
        # print("이동후(cy, cx, cd):", cy, cx, cd)

        #i사람 위치에 있는 플레이어 구하기
        gi = get_gi(cy, cx, i, men_xyd_list)

        if gi == -1: # 위치에 사람 없음
            if len(chong_pan[cy][cx]) > 0: #총이 한개 이상 있음
                get_chong(i, cy, cx, chong_pan, men_gong_list)
        else: # 위치에 사람 있음
            fight_m1_m2(i, gi, men_xyd_list, men_gong_list, men_point_list, chong_pan,cy, cx)







        # break
    # break

print(*men_point_list)


