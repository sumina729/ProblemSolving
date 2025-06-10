#am 8:30 ~ pm 12:56
def is_end(santa_list):
    global N, M, P, C, D

    for i in range(P):
        sn, sy, sx, sj, sg = santa_list[i]
        if sg > -1:
            return False

    return True

def adjust_sg(santa_list):
    global N, M, P, C, D

    for i in range(P):
        sn, sy, sx, sj, sg = santa_list[i]
        if sg > -1: #탈락 안한거만
            sg = max(0, sg-1)
            santa_list[i] = [sn, sy, sx, sj, sg]

def dist(y1, x1, y2, x2):
    return (x1 - x2)**2 + (y1 - y2)**2

def is_in_pan(y, x):
    global N

    if -1<x<N and -1<y<N:
        return True
    else:
        return False

def move_ryrx(ry, rx, santa_list):
    global N, M, P, C, D

    santa_lyx = []
    for i in range(P):
        sn, sy, sx, sj, sg = santa_list[i]
        if sg > -1:  # 탈락 안한거만
            l = dist(ry, rx, sy, sx)
            santa_lyx.append([l, sy, sx])

    santa_lyx.sort(key=lambda x: (x[0], -x[1], -x[2]))

    go_sy = santa_lyx[0][1]
    go_sx = santa_lyx[0][2]

    dy = [1, -1, 0, 0, 1, -1, 1, -1]
    dx = [0, 0, -1, 1, -1, -1, 1, 1]

    min_l = (N+N)**2
    go_ry = -1
    go_rx = -1
    go_rd = -1
    for i in range(8):
        ny = ry+dy[i]
        nx = rx+dx[i]

        if is_in_pan(ny, nx):
            l = dist(go_sy, go_sx, ny, nx)
            if min_l > l:
                min_l = l
                go_ry = ny
                go_rx = nx
                go_rd = i

    return go_ry, go_rx, go_rd

def conplict_from_ryrx_to_sysx(ry, rx, santa_list, rd):
    global N, M, P, C, D

    for i in range(P):
        sn, sy, sx, sj, sg = santa_list[i]
        if sg > -1:  # 탈락 안한거만
            if ry == sy and rx == sx:
                # print(sn, "번 상타와 충돌(루->산)(함수구현하기)")
                conplict(i, sn, sy, sx, sj, sg, 0, rd, santa_list)
                return

def conplict_from_sysx_to_ryrx(i, sn, sy, sx, sj, sg, ry, rx, santa_list, sd):
    global N, M, P, C, D
    if ry == sy and rx == sx:
        # print(sn, "번 산타가 루돌푸와 충돌(산->루)(함수구현하기)")
        sd = (sd+2)%4
        conplict(i, sn, sy, sx, sj, sg, 1, sd, santa_list)

    else:
        santa_list[i] = [sn, sy, sx, sj, sg]

def conplict(i, sn, sy, sx, sj, sg, C_or_D, di, santa_list):
    global N, M, P, C, D
    if C_or_D == 0: #C 사용
        rdy = [1, -1, 0, 0, 1, -1, 1, -1]
        rdx = [0, 0, -1, 1, -1, -1, 1, 1]

        ny = sy+rdy[di]*C
        nx = sx+rdx[di]*C

        sj += C
    else:
        sdy = [-1, 0, 1, 0]
        sdx = [0, 1, 0, -1]

        ny = sy + sdy[di] * D
        nx = sx + sdx[di] * D

        sj += D

    if is_in_pan(ny, nx):
        if is_not_in_santa(sn, ny, nx, santa_list):  # 다른거 없으면
            santa_list[i] = [sn, ny, nx, sj, 2]  # 기절
        else:
            santa_list[i] = [sn, sy, sx, sj, 2]  # 점수랑, 기절만 먼저 갱신
            sanghojangyuong(i, sn, ny, nx, sj, sg, santa_list, C_or_D, di)
    else:
        # print(sn, "번 탈락")
        santa_list[i] = [sn, -1, -1, sj, -1]  # 탈락

    return

def is_in_santa(n, y, x, santa_list):
    global N, M, P, C, D

    for i in range(P):
        sn, sy, sx, sj, sg = santa_list[i]
        if sg > -1:  # 탈락 안한거만
            if not sn == n and y == sy and x == sx:
                return i

    return -1

def sanghojangyuong(si, sn, ny, nx, sj, sg, santa_list, C_or_D, di):
    global N, M, P, C, D

    ci = si

    if C_or_D == 0: #C 사용
        dy = [1, -1, 0, 0, 1, -1, 1, -1]
        dx = [0, 0, -1, 1, -1, -1, 1, 1]

    else:
        dy = [-1, 0, 1, 0]
        dx = [0, 1, 0, -1]

    while True:
        if not is_in_pan(ny, nx):
            santa_list[ci] = [sn, -1, -1, santa_list[ci][3], -1]
            break

        nsi = is_in_santa(sn, ny, nx, santa_list)
        if nsi ==  -1: #
            santa_list[ci] = [santa_list[ci][0], ny, nx, santa_list[ci][3], santa_list[ci][4]]
            break
        else:
            santa_list[ci] = [santa_list[ci][0], ny, nx, santa_list[ci][3], santa_list[ci][4]]

            ci = nsi
            sn, ny, nx = santa_list[ci][0],  santa_list[ci][1]+dy[di],  santa_list[ci][2]+dx[di]

def is_not_in_santa(n, y, x, santa_list):
    global N, M, P, C, D

    for i in range(P):
        sn, sy, sx, sj, sg = santa_list[i]
        if sg > -1:  # 탈락 안한거만
            if not sn == n and y == sy and x == sx:
                return False

    return True

def move_sysx_sn(sn, sy, sx, ry, rx, santa_list):
    global N, M, P, C, D

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    min_l = dist(sy, sx, ry, rx)
    go_sy = sy
    go_sx = sx
    go_sd = -1

    for i in range(4):
        ny = sy + dy[i]
        nx = sx + dx[i]

        if is_in_pan(ny, nx) and is_not_in_santa(sn, ny, nx, santa_list):
            l = dist(ny, nx, ry, rx)
            if min_l > l:
                min_l = l
                go_sy = ny
                go_sx = nx
                go_sd = i

    return go_sy, go_sx,go_sd

def move_sysx(ry, rx, santa_list):
    global N, M, P, C, D

    santa_list.sort(key=lambda x: (x[0]))
    # print("번호순 산타솔팅 ", santa_list)

    for i in range(P):
        sn, sy, sx, sj, sg = santa_list[i]
        if sg == 0: #탈락 아니면서, 기절 아닌거만
            sy, sx, sd = move_sysx_sn(sn, sy, sx, ry, rx, santa_list)
            if not sd == -1:
                conplict_from_sysx_to_ryrx(i, sn, sy, sx, sj, sg, ry, rx, santa_list, sd) # 여기서 이동까지

N, M, P, C, D = map(int, input().split())

ry, rx = map(int, input().split())
santa_list = [] # [sn, sy, sx, sj, sg] -> [번호, y, x, 점수, 기절 및 탈락(-1 탈락)]
for _ in range(P):
    sn, sy, sx = map(int, input().split())
    santa_list.append([sn, sy-1, sx-1, 0, 0])
ry-=1
rx-=1

for turn in range(1, M+1):

    #모튼 산타가 탈락이면 끝
    if is_end(santa_list):
        break

    #루돌푸 움직임
    ry, rx, rd = move_ryrx(ry, rx, santa_list)
    conplict_from_ryrx_to_sysx(ry, rx, santa_list, rd)

    move_sysx(ry, rx, santa_list)

    #살아있는 루돌푸에게 점수
    for i in range(P):
        sn, sy, sx, sj, sg = santa_list[i]
        if sg > -1:  # 탈락 안한거만
            santa_list[i] = [sn, sy, sx, sj+1, sg]

    # 턴 끝나고 기절 체크
    adjust_sg(santa_list)

#정답출력
santa_list.sort(key=lambda x: x[0])
for sn, sy, sx, sj, sg in santa_list:
    print(sj, end=" ")