from collections import deque

#상하좌우 0, 1, 2, 3
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

lrd_lisr = [[2, 3], [3, 2], [1, 0], [0, 1]] #방향별 좌우

def get_path(Sx,Sy, Ex, Ey, pan, N):
    global dx, dy

    visited = [[-1 for _ in range(N)]for _ in range(N)]
    next_xy = [[[] for _ in range(N)]for _ in range(N)]

    que = deque()
    que.append((Sx, Sy))
    visited[Sy][Sx] = 0

    while que:
        cx, cy = que.popleft()
        
        for i in [0,1, 2, 3]: #상, 하, 좌, 우
            nx = cx+dx[i]
            ny = cy+dy[i]

            if -1<nx<N and -1<ny<N and pan[ny][nx] == 0 and visited[ny][nx]  == -1: #먼저 간거가 방분(상하죄우)
                que.append((nx, ny))
                visited[ny][nx] = visited[cy][cx]+1
                next_xy[ny][nx] = (cx, cy)
    
    if visited[Ey][Ex] == -1:
        return -1
    
    path_tmp = deque()
    cx, cy = Ex, Ey

    while True:
        cx, cy = next_xy[cy][cx]

        if cx == Sx and cy == Sy:
            break

        path_tmp.appendleft((cx, cy))

    return list(path_tmp)

def get_bang(sx, sy, tmp_pan, N, sd, lr):
    global lrd_lisr, dx, dy

    sn = 0
    while True:
        sx = sx+ dx[sd]
        sy = sy+ dy[sd]
        sn +=1

        if not (-1<sx<N and -1<sy<N):
            break

        tmp_pan[sy][sx] = 2

        #좌, 우
        if lr == 1 or lr == 2:
            lrd = lrd_lisr[sd][lr-1]
            for i in range(1, sn+1):
                nx = sx + i*dx[lrd]
                ny = sy + i*dy[lrd]

                if -1<nx<N and -1<ny<N:
                    tmp_pan[ny][nx] = 2
    
def get_sisun_pan_n(mx, my, N, sd, junsa_xy_list):
    global lrd_lisr, dx, dy

    tmp_pan = [[0 for _ in range(N)]for _ in range(N)]
    dol_js_list = []

    sx, sy = mx, my
    sn = 0

    while True:
        sx = sx+ dx[sd]
        sy = sy+ dy[sd]
        sn +=1

        if not (-1<sx<N and -1<sy<N):
            break
        
        if tmp_pan[sy][sx] == 0:
            tmp_pan[sy][sx] = 1
            for tjx, tjy in junsa_xy_list:
                if sx == tjx and sy == tjy:
                    dol_js_list.append((sx, sy))
                    get_bang(sx, sy, tmp_pan, N, sd, 0)
        
        #좌, 우
        for di in range(2):
            lrd = lrd_lisr[sd][di]
            for i in range(1, sn+1):
                nx = sx + i*dx[lrd]
                ny = sy + i*dy[lrd]

                if -1<nx<N and -1<ny<N:
                    if tmp_pan[ny][nx] == 0:
                        tmp_pan[ny][nx] = 1
                        for tjx, tjy in junsa_xy_list:
                            if nx == tjx and ny == tjy:
                                dol_js_list.append((nx, ny))
                                get_bang(nx, ny, tmp_pan, N, sd, di+1)

    for y in range(N):
        for x in range(N): 
            if tmp_pan[y][x] == 2:
                tmp_pan[y][x] = 0

    return tmp_pan, dol_js_list

def get_sisun_pan(mx, my, pan, junsa_xy_list, N):
    sisun_pan = [[[]]for _ in range(4)]
    dol_js_list = [[]for _ in range(4)]

    #수 같으면 상하좌우선순위
    for i in range(4):
        sisun_pan[i], dol_js_list[i] = get_sisun_pan_n(mx, my, N, i, junsa_xy_list)

    js_anc_list = [len(dol_js_list[i]) for i in range(4)]
    sort_list = [0, 1, 2, 3]
    sort_list = sorted(sort_list, key = lambda i:(-js_anc_list[i], i))
    
    return sisun_pan[sort_list[0]], dol_js_list[sort_list[0]]

def move_junsa(jx, jy, mx, my, N, cnt, sisun_pan):
    dxdy =[
        [0, 1, 2, 3],
        [2, 3, 0, 1]
    ]

    cl = abs(jx-mx) + abs(jy-my)
    cx = jx
    cy = jy
    for i in dxdy[cnt]:
        nx = jx+dx[i]
        ny = jy+dy[i]

        if -1<nx<N and -1<ny<N and sisun_pan[ny][nx] == 0:
            nl = abs(nx-mx) + abs(ny-my)
            if nl < cl:
                cl = nl
                cx = nx
                cy = ny

    return cx, cy

def move_junsas(junsa_xy_list, dol_js_list, N, mx, my, sisun_pan):
    gong_n = 0
    move_n = 0
    new_junsa_xy_list = []

    for jx, jy in junsa_xy_list:

        if (jx, jy) in dol_js_list: #돌 됐으면 이동 x
            new_junsa_xy_list.append((jx, jy))
            continue
    
        for cnt in range(2):
            jnx, jny = move_junsa(jx, jy, mx, my, N, cnt, sisun_pan)
            
            if jnx == jx and jny == jy: 
                break

            jx = jnx
            jy = jny
            move_n+=1

        if jnx == mx and jny == my:
            # 메두사 잡음
            gong_n+=1
        else:
            new_junsa_xy_list.append((jnx, jny))

    return new_junsa_xy_list, gong_n, move_n

def gong_m(mx, my, junsa_xy_list):
    new_junsa_xy_list = []
    for jx, jy in junsa_xy_list:
        if jx == mx and jy == my:
            continue
        new_junsa_xy_list.append((jx, jy))

    return new_junsa_xy_list

# 입력
N, M = map(int, input().split()) #마을크기, 전사수
Sy, Sx, Ey, Ex = map(int, input().split())
rici_list = list(map(int, input().split()))
pan = [list(map(int, input().split())) for _ in range(N)]
junsa_xy_list = []
for i in range(M):
    junsa_xy_list.append((rici_list[i*2+1], rici_list[i*2])) #(x, y)

#메두사 경로 찾기
path_xy = get_path(Sx,Sy, Ex, Ey, pan, N)

if path_xy == -1:
    print("-1")
else:
    for mx, my in path_xy:
        # 메두사 이동후, 잡힌거 체크
        junsa_xy_list = gong_m(mx, my, junsa_xy_list)
        
        #메두사 시선
        sisun_pan, dol_js_list = get_sisun_pan(mx, my, pan, junsa_xy_list, N)

        #전사 이동
        junsa_xy_list, gn, mn = move_junsas(junsa_xy_list, dol_js_list, N, mx, my, sisun_pan)
        print(mn, len(dol_js_list), gn)

    print(0)