'''
- 상어에는 1 이상 M 이하의 자연수 번호(모든 번호는 서로 다르다.)
- 1의 번호를 가진 어른 상어는 가장 강력해서 나머지 모두를 쫓아낼 수 있다.

1. 맨 처음에는 모든 상어가 '자신의 위치'에 자신의 냄새를 뿌린다.
2.  1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동 후 자신의 냄새를 그 칸에 뿌린다
    - 인접한 칸 중 
        - 아무 냄새가 없는 칸의 방향으로 잡는다.
        - 자신의 냄새가 있는 칸의 방향
        - 여러개면 우선순위따른다 (상어가 맨 처음에 보고 있는 방향은 입력으로 주어지고, 그 후에는 방금 이동한 방향이 보고 있는 방향이 된다.)
3. 모든 상어가 이동한 후 한 칸에 여러 마리의 상어가 남아 있으면, 가장 작은 번호를 가진 상어를 제외하고 모두 격자 밖으로 쫓겨난다.
4. 냄새는 상어가 k번 이동하고 나면 사라진다.

5. 1번 상어만 격자에 남게 되기까지 몇 초가 걸리는지
    - 1000초가 넘어도 다른 상어가 격자에 남아 있으면 -1

1, 2, 3, 4는 각각 위, 아래, 왼쪽, 오른쪽 (0, 1, 2, 3 으로 계산 요망)
'''

def dbug_print(s_pan, k_pan, N):
    print()
    print("상어위치 [상어번호, 방향]")
    for y in range(N):
        print(s_pan[y])
    print()
    print("상어냄새 [상어번호, 냄새시간]")
    for y in range(N):
        print(k_pan[y])

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
    '''
    1. 아무 냄새가 없는 칸의 방향으로 잡는다.
    2. 자신의 냄새가 있는 칸의 방향
    3. 여러개면 우선순위따른다
    '''
    sd_list = spd[sn-1][sd]
    # print(sn,sd, sd_list)
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

    print("이거 나오면 논리 이상한거임")
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
                # print(sn, "의 이동위치", x, y, "->", nx, ny)
                
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
#1, 2, 3, 4는 각각 위, 아래, 왼쪽, 오른쪽 (0, 1, 2, 3 으로 계산 요망)
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

for y in range(N):
    for x in range(N):
        if input_pan[y][x] == 0:
            s_pan[y][x] = [0, 0]
        else:
            n = input_pan[y][x]
            nd = input_cd[input_pan[y][x]-1]-1
            s_pan[y][x] = [n, nd]

# print()
# print("상어방향 우선순위 0, 1, 2, 3 -> 상, 하, 죄, 우")
# for i in range(M):
#     print(spd[i])
# print()
# print()
# print("초기입력")
# dbug_print(s_pan, k_pan, N)

#1 현재위치에 냄새두기
set_k(s_pan, k_pan, N, K)
# dbug_print(s_pan, k_pan, N)

ans = 0
while True:
    ans+=1

    # print()
    # print()
    # print("물고기 이동 후 냄새")
    s_pan = move_s(s_pan, k_pan, spd, N)
    
    reduce_k(k_pan, N)
    set_k(s_pan, k_pan, N, K)
    # dbug_print(s_pan, k_pan, N)

    if is_only_1(s_pan, N):
        print(ans)
        break
    if ans >= 1000:
        print(-1)
        break
