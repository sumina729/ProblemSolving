import sys


sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


def is_end(man_yx):
    global N, M, K
    for i in range(M):
        y, x = man_yx[i]
        if y > -1:
            return False

    return True

def dist(y1, x1, y2, x2):
    return abs(x1 - x2) + abs(y1 - y2)

def is_in_pan(y, x):
    global N, M, K

    return -1<y<N and -1<x<N

def move_men(y, x, exit_y, exit_x, pan):
    # 상, 하, 좌, 우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    min_l = dist(y, x, exit_y, exit_x)
    my = y
    mx = x
    mn = 0

    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]

        if is_in_pan(ny, nx) and pan[ny][nx] == 0: # 빈칸만 이동
            l = dist(ny, nx, exit_y, exit_x)
            if l < min_l:
                min_l = l
                my = ny
                mx = nx
                mn = 1

    # print(y, x, "->", my, mx, "이동칸수", mn)
    if my == exit_y and mx == exit_x:
        my = -1
        mx = -1
        # print("탈출 ~")

    return my, mx, mn

def is_men_in_pan(man_yx, sy, sx, min_l):
    global N, M, K
    for i in range(min_l+1):
        for j in range(min_l+1):
            ny = sy+i
            nx = sx+j

            if [ny, nx] in man_yx:
                # print("범위안에 사람있음")
                return True

    return False

def get_pan_sysx(pan, man_yx, exit_y, exit_x):
    global N, M, K

    min_l = N

    #가장작은 l 찾기
    for i in range(M):
        y, x = man_yx[i]

        if y > -1: # 탈출 못한 사람이면
            yl = abs(exit_y-y)
            xl = abs(exit_x-x)

            l = max(yl,xl)
            min_l = min(min_l, l)

    # print("반지름:", min_l+1,"이동거리:", min_l)

    #죄측위부터
    ty = exit_y-min_l
    tx = exit_x-min_l

    for i in range(min_l+1):
        for j in range(min_l+1):
            sy = ty+i
            sx = tx+j

            # print(sy, sx)
            if not is_in_pan(sy, sx):
                continue

            if is_men_in_pan(man_yx, sy, sx, min_l):
                return sy, sx, min_l+1

    print("이거 나오면 논리오류")
    return -1, -1, -1

def rotate_(sy, sx, sl, pan, exit_y, exit_x, man_yx):
    global N, M, K
    tmp_pan = [pan[i][:] for i in range(N)]
    tmp_man_yx = [man_yx[i][:] for i in range(M)]
    tmp_exit_y = -1
    tmp_exit_x = -1

    for y in range(sl):
        for x in range(sl):
            pan[sy+x][sx+sl-y-1] = max(0, tmp_pan[sy+y][sx+x]-1)
            if sy+y == exit_y and sx+x == exit_x:
                tmp_exit_y = sy+x
                tmp_exit_x = sx+sl-y-1

                # print("출구도 회전:", tmp_exit_y,tmp_exit_x)

            for i in range(M):
                my, mx = man_yx[i]
                if sy+y == my and sx+x == mx:  # 탈출 못한 사람이면 비교 빠피 못함
                    tmp_man_yx[i] = [sy+x, sx+sl-y-1]
                    # print("사람도 회전:", tmp_man_yx[i])


    return tmp_exit_y, tmp_exit_x, tmp_man_yx

N, M, K = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(N)]
man_yx = [list(map(int, input().split())) for _ in range(M)]
exit_y, exit_x = map(int, input().split())

#0,0 기준으로 변경
man_yx = [ [man_yx[m][0]-1, man_yx[m][1]-1] for m in range(M)]
exit_y-=1
exit_x-=1

ans_l = 0


# print("초기 입력후, 0, 0 기준으로 위치변경")
# print("N, M, K:", N, M, K)
# print("pan")
# for y in range(N):
#     print(pan[y])
#
# print("man_yx[y, x]:", man_yx)
# print("exit_y, exit_x:", exit_y, exit_x)

for k in range(K): # K초 반복

    #종료조건 확인
    if is_end(man_yx):
        # print("!사람 다 탈출함, 종료!")
        break

    # print("=============", k+1,"초 시작=============")

    #참가자 이동
    for i in range(M):
        y, x = man_yx[i]

        if y > -1: # 탈출 못한 사람이면
            my, mx, mn = move_men(y, x, exit_y, exit_x, pan)
            ans_l+=mn #이동 거리 갱신
            man_yx[i] = [my, mx] #움직임 갱신

    # print("man_yx[y, x]:", man_yx, ans_l)

    #판 회전
    sy, sx, sl = get_pan_sysx(pan, man_yx, exit_y, exit_x)
    # print("sy, sx, sl:", sy, sx, sl)

    #판회전
    exit_y, exit_x , man_yx = rotate_(sy, sx, sl, pan, exit_y, exit_x, man_yx)
    # for y in range(N):
    #     print(pan[y])

    # print("회전후 출구화 사람", exit_y, exit_x, man_yx)
    #
    # print(ans_l)
    # print(exit_y+1, exit_x+1)

    # if k == 6:
    #     break
print(ans_l)
print(exit_y+1, exit_x+1)