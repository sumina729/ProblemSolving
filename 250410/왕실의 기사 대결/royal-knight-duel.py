from collections import deque

#위 오 아래 왼
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def start_xy(pan, n):
    global L

    for y in range(L):
        for x in range(L):
            if pan[y][x] == n:
                return x, y

def bfs(x, y, gisa_num, d):
    '''
        1. d 방향이면 방패면 갈수 있음.방문처리
        2. 방패 아닌데 d 방향에 하나라도 벽이 있는지 체크
        3. 그외 방향으로는 같은 번호일떄면
        리턴, -1 이면 안움직이고, 아니면 옴직일 전사들 리스트
    '''

    global gisa_pan, pan
    visited = [[0 for _ in range(L)] for _ in range(L)]

    que = deque()
    que.append((x, y, gisa_num))
    visited[y][x] = 1
    is_go = 1

    go_list = set()
    go_list.add(gisa_num)

    while que:
        x, y, gisa_num = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if i == d:
                # 방패이면 무조건 감
                if -1<nx<L and -1<ny<L and gisa_pan[ny][nx] > -1 and visited[ny][nx] == 0: # 즉 범위내에있는 방패들이면
                    go_list.add(gisa_pan[ny][nx])
                    que.append((nx, ny, gisa_pan[ny][nx]))
                    visited[ny][nx] = 1
                elif not (-1<nx<L and -1<ny<L) or pan[ny][nx] == 2: #벽이면
                    # is_go = 0
                    return -1
            else: #다른 방향이면 자기 방패만
                if -1<nx<L and -1<ny<L and gisa_pan[ny][nx] == gisa_num and visited[ny][nx] == 0: # 즉 범위내에있는 방패들이면
                    que.append((nx, ny, gisa_pan[ny][nx]))
                    visited[ny][nx] = 1


    # if is_go == 0:
    #     return -1
    # else:
    #     return go_list
    return go_list

def move_gosa(gisa_num, d):
    global gisa_pan

    sx, sy = start_xy(gisa_pan, gisa_num)
    move_gisa_list = bfs(sx, sy, gisa_num, d) #한번에 움직일 기사들 리스트 반환 # 셋

    #이동 못함
    if move_gisa_list == -1:
        return gisa_pan, -1

    new_gisa_pan = [[-1 for _ in range(L)] for _ in range(L)]
    for y in range(L):
        for x in range(L):
            if gisa_pan[y][x] in move_gisa_list:
                # print(x, y, x+dx[d], y+dy[d])
                new_gisa_pan[y+dy[d]][x+dx[d]] = gisa_pan[y][x]
            elif gisa_pan[y][x] > -1:
                new_gisa_pan[y][x]= gisa_pan[y][x]

    return new_gisa_pan, move_gisa_list

#함정에 빠진 전사 체크하기
def attack_gisa(gisa_pan, move_gisa_list, pan, gisa_k):
    for i in move_gisa_list:
        for y in range(L):
            for x in range(L):
                if gisa_pan[y][x] == i and pan[y][x] == 1: #체크할 기사이면서, 함정이면
                    gisa_k[i] = max(0, gisa_k[i]-1)

#죽은 전사 지우는 함수
def remove_junsa(gisa_pan, i):
    for y in range(L):
        for x in range(L):
            if gisa_pan[y][x] == i:
                gisa_pan[y][x] = -1



L, N, K = map(int, input().split()) #체스판, 기사수, 왕 명갯수
pan =  [list(map(int, input().split())) for _ in range(L)]
gisa_pan = [[-1 for _ in range(L)] for _ in range(L)]
gisa_k = []

for n in range(N):
    y, x, h, w, k = map(int, input().split())
    for i in range(h):
        for j in range(w):
            gisa_pan[y-1+i][x-1+j] = n
    gisa_k.append(k)

first_gisa_k = gisa_k[:]
king_mlist = []
for i in range(K):
    gisa_i, d = map(int, input().split())
    king_mlist.append([gisa_i-1, d]) #기사 0번부터



for gisa_i, d in king_mlist:
    if gisa_k[gisa_i] < 1: #죽은 기사이면 넘어감
        continue

    #전사이동
    gisa_pan, move_gisa_list = move_gosa(gisa_i, d)
    if move_gisa_list == -1:
        # 이동 못함 턴 다시 처음부터
        continue

    # 움직인 전사에 대해서 함정 체크
    move_gisa_list.remove(gisa_i) #명령 받은 전사는 빼기
    attack_gisa(gisa_pan, move_gisa_list, pan, gisa_k)

    # 목숨 0 인거 전사 판에서 지우기
    for i in range(len(gisa_k)):
        if gisa_k[i] == 0:
            remove_junsa(gisa_pan, i)


#살아있는 전사들 수와 비교하기
ans = 0
for i in range(len(gisa_k)):
    if gisa_k[i] > 0:
        ans += first_gisa_k[i] - gisa_k[i]

print(ans)