'''
pm 4:00: 문제풀이 시작
pm 4:51: 코드 시작
pm 7:08: 코드 다짬, 제출 : 시간초과남..
'''

import sys
sys.stdin = open('input.txt')


def move_man():
    global N, M, man_list, exit_y, exit_x, pan, ans
    new_man_list = []
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for m in range(len(man_list)):
        mx, my = man_list[m]

        min_dist = abs(exit_x-mx) + abs(exit_y-my) # 현재 출구와의 거리 계산
        # print(exit_x, exit_y, "까지의 원래 거리", min_dist)
        min_x = mx
        min_y = my
        is_go = 0

        #갈 수 있는 방향 찾기
        for i in [0, 1, 2, 3]:
            nx = mx+dx[i]
            ny = my+dy[i]

            if -1<nx<N and -1<ny<N and pan[ny][nx] == 0: #범위 안이고, 벽이 없으면
                tmp_dist = abs(exit_x-nx) + abs(exit_y-ny)
                if min_dist > tmp_dist:
                    is_go = 1
                    min_dist = tmp_dist
                    min_x = nx
                    min_y = ny

        # print(mx, my, "=>", min_x, min_y)
        if not (min_x == exit_x and min_y == exit_y):
            new_man_list.append((min_x, min_y))

        if is_go:
            ans+=1

    # print(new_man_list)
    return new_man_list

#왼쪽위 찾기
def search_rect(mx, my, exit_x, exit_y, dist_r):
    global N

    for i in range(dist_r, -1, -1):
        sy = max(my, exit_y)-i
        if -1<sy<N:
            break

    for i in range(dist_r, -1, -1):
        sx = max(mx, exit_x)-i
        if -1<sx<N:
            break

    return sx, sy

def make_rect():
    global N, man_list, exit_y, exit_x, pan

    min_r = N+1
    min_sy = N
    min_sx = N

    for mx, my in man_list:
        dist_x = abs(exit_x-mx)
        dist_y = abs(exit_y-my)

        dist_r = max(dist_x, dist_y) # 사람과 출구릐 직사형 거리

        #dist_x, dist_y, exit_x, exit_y 포함하는 사각형중 위 -> 왼 에 있는거
        sx, sy = search_rect(mx, my, exit_x, exit_y, dist_r)
        # print(mx, my, "과의 출구 직사각형중 가장 왼쪽 위: ", sx, sy, dist_r+1)

        if min_r > dist_r:
            min_r = dist_r
            min_sy = sy
            min_sx = sx
        elif min_r == dist_r and min_sy > sy:
            min_r = dist_r
            min_sy = sy
            min_sx = sx
        elif min_r == dist_r and min_sy == sy and min_sx > sx:
            min_r = dist_r
            min_sy = sy
            min_sx = sx


    return  min_sx, min_sy, min_r+1

def rotate_man_exit(sx, sy, r):
    global man_list, exit_y, exit_x
    # 출구 90도 회전

    # print(exit_x-sx, exit_y-sy)
    tmp_x = sx + (r-1)-(exit_y-sy)
    tmp_y = sy + (exit_x-sx)

    exit_x = tmp_x
    exit_y = tmp_y
    # print("출구이동: ", exit_x, exit_y)

    # 사각형 안에 있는 사람 체크 해서 90도 회전
    for i in range(len(man_list)):
        mx, my = man_list[i]
        if  sx<=mx<sx+r and sy<=my<sy+r:
            tmp_x = sx + (r - 1) - (my - sy)
            tmp_y = sy + (mx - sx)

            mx = tmp_x
            my = tmp_y
            man_list[i] = [mx, my]
            # print("사람이동: ", mx, my)

def rotate_pan(sx, sy, r):
    global N, pan
    tmp_pan = [[pan[y][x] for x in range(N)] for y in range(N)]

    for y in range(r):
        for x in range(r):
            # print(sy+x, sx+(r-y-1))
            tmp_pan[sy+x][sx+(r-y-1)] = pan[sy+y][sx+x]

    return tmp_pan

def remove_buk(sx, sy, r):
    for y in range(sy, sy+r):
        for x in range(sx, sx+r):
            if pan[y][x] > 0:
                pan[y][x]-=1

N,M,K = map(int, input().split()) #판크기, 사람수, 개임횟수
pan = [list(map(int, input().split())) for _ in range(N)]
man_list = []
for _ in range(M):
    y, x = map(int, input().split())
    man_list.append((x-1, y-1))

exit_y, exit_x = map(int, input().split())
exit_y -=1
exit_x -=1

ans = 0

for _ in range(K): #K번 진행
    if len(man_list) == 0:
        # print("사람들 모두 출구로 빠져나감")
        break

    man_list = move_man() #사람 이동 시키기
    sx, sy, r = make_rect()
    # print("최종 결정 사각형: ", sx, sy, r)

    rotate_man_exit(sx, sy, r)
    # print("출구이동", exit_x, exit_y)
    # print("사람이동", man_list)

    pan = rotate_pan(sx, sy, r)
    # print("판회전")
    # for y in pan:
    #     print(y)

    remove_buk(sx, sy, r)
    # print("벽부수기")
    # for y in pan:
    #     print(y)
    #
    # print("*********************총 이동수: ", ans)

print(ans)
print(exit_y+1, exit_x+1)
    # break