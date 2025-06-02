
def set_k(s_pan, k_pan, N, K):
    for y in range(N):
        for x in range(N):
            if s_pan[y][x][0] > 0:
                k_pan[y][x] = [s_pan[y][x][0], K]

def reduce_k(k_pan, N):
    for y in range(N):
        for x in range(N):
            n = k_pan[y][x][0]
            nk = k_pan[y][x][1]
            if n > 0:
                nk = nk-1
                if nk == 0:
                    k_pan[y][x] = [0, 0]
                else: 
                    k_pan[y][x] = [n, nk]
                             
def get_nxny(cx, cy, sn,sd, k_pan, spd, N):
    sd_list = spd[sn-1][sd]

    for nd in sd_list: # 아무 냄새가 없는 칸의 방향으로 잡는다.
        nx = cx+dx[nd]
        ny = cy+dy[nd]
        if -1<nx<N and -1<ny<N and k_pan[ny][nx][0] == 0:
            return nx, ny, nd
        
    for nd in sd_list: #자신의 냄새가 있는 칸의 방향
        nx = cx+dx[nd]
        ny = cy+dy[nd]
        if -1<nx<N and -1<ny<N and k_pan[ny][nx][0] == sn:
            return nx, ny, nd

    return 

def move_s(s_pan, k_pan, spd, N):
    new_s_pan =  [[[0, 0] for _ in range(N)]for _ in range(N)]

    for y in range(N):
        for x in range(N):
            sn = s_pan[y][x][0]
            sd = s_pan[y][x][1]
            if sn > 0: # 상어이면
                #1. 이동방향 및 위치 찾기
                nx, ny, nd = get_nxny(x, y, sn, sd, k_pan, spd, N)
                
                #2. 이동+그곳이 이미 상어 있으면 수가 큰 물고기가 쫒겨남
                if new_s_pan[ny][nx][0] > 0: #다른 상어 있는지
                    if new_s_pan[ny][nx][0] > sn:
                        new_s_pan[ny][nx] = [sn, nd]
                else:
                    new_s_pan[ny][nx] = [sn, nd]

    return new_s_pan
              
def is_only_1(s_pan, N):
    for y in range(N):
        for x in range(N):
            if s_pan[y][x][0] > 1:
                return False
    return True

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N, M, K = map(int, input().split())
input_pan = [list(map(int, input().split())) for _ in range(N)]
input_cd = list(map(int, input().split()))
input_sd = [list(map(int, input().split())) for _ in range(M*4)]
for i in range(M*4):
    for j in range(4):
        input_sd[i][j] = input_sd[i][j]-1

s_pan = [[[]for _ in range(N)]for _ in range(N)]
k_pan = [[[0, 0]for _ in range(N)]for _ in range(N)]
spd = [[ input_sd[i*4+j] for j in range(4)]for i in range(M)]
ans = 0

for y in range(N):
    for x in range(N):
        if input_pan[y][x] == 0:
            s_pan[y][x] = [0, 0]
        else:
            n = input_pan[y][x]
            nd = input_cd[input_pan[y][x]-1]-1
            s_pan[y][x] = [n, nd]

#현재위치에 냄새두기
set_k(s_pan, k_pan, N, K)

while True:
    ans+=1

    s_pan = move_s(s_pan, k_pan, spd, N)
    
    reduce_k(k_pan, N)
    set_k(s_pan, k_pan, N, K)


    if is_only_1(s_pan, N):
        print(ans)
        break

    if ans >= 1000:
        print(-1)
        break
