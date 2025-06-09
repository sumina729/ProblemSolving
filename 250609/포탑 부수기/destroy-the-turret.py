
from collections import deque

def get_top_cnt(gongguk_pan, N, M):
    cnt = 0
    for y in range(N):
        for x in range(M):
            if gongguk_pan[y][x] > 0:
                cnt+=1
    # print("포탑수:", cnt)
    return cnt

'''
1. 공격자 선정

- gongguk_pan[y][x]가 0보다 큰 탑중에, gongguk_pan[y][x] 가 가장 작은공
- 여러개이면, turn_pan[y][x]가 가장 큰
- 여러개이면, 그중 y+x 값이 가장 큰
- 여러개이면, 그중 x가 가장 큰

선탠된  gx, gy 위치의 탑은 gongguk_pan[gy][gx] + (N+M) 로 공격력은 얻는다

'''
def get_gygx(gongguk_pan, turn_pan, N, M):

    live_potop_list = []
    for y in range(N):
        for x in range(M):
            if gongguk_pan[y][x] > 0:
                live_potop_list.append([y, x])
    
    # print(live_potop_list)
    live_potop_list = sorted(live_potop_list, key=lambda a: (gongguk_pan[a[0]][a[1]], -turn_pan[a[0]][a[1]], -(a[0]+a[1]), -a[1]))

    return live_potop_list[0][0], live_potop_list[0][1]


'''
1. 당하는 포탑 선정
- 공격자 가 아닌것중에
- gongguk_pan[y][x]가 0보다 큰 탑중에, gongguk_pan[y][x] 가 가장 큰
- 여러개이면, turn_pan[y][x]가 가장 작은
- 여러개이면, 그중 y+x 값이 가장 작은
- 여러개이면, 그중 x가 가장 작은

선탠된  gx, gy 위치의 탑은 gongguk_pan[gy][gx] + (N+M) 로 공격력은 얻는다

'''
def get_hyhx(gongguk_pan, turn_pan, N, M, gy, gx):

    live_potop_list = []
    for y in range(N):
        for x in range(M):
            if gongguk_pan[y][x] > 0 and not (y == gy and x == gx): # 사라진거 아니면서, 공격자 아닌
                live_potop_list.append([y, x])
    
    live_potop_list = sorted(live_potop_list, key=lambda a: (-gongguk_pan[a[0]][a[1]], turn_pan[a[0]][a[1]], (a[0]+a[1]), a[1]))

    return live_potop_list[0][0], live_potop_list[0][1]


def bfs(gy, gx, hy, hx, gongguk_pan, N, M):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # print(gy, gx, "->",hy, hx, "경로찾기")
    visited = [[-1 for _ in range(M)] for _ in range(N)]
    conected = [[[] for _ in range(M)] for _ in range(N)]

    path = deque()

    que = deque()
    que.append((gy, gx))
    visited[gy][gx] = 0

    while que:
        cy, cx = que.popleft()

        for i in [0, 1, 2, 3]: #우하좌상 우선순위
            ny = (cy+dy[i])%N #경계뚫기
            nx = (cx+dx[i])%M

            if gongguk_pan[ny][nx] > 0 and visited[ny][nx] == -1:
                que.append((ny, nx))
                visited[ny][nx] = visited[cy][cx] +1
                conected[ny][nx] = [cy, cx]
    
    # print()
    # for y in range(N):
    #     print(visited[y])
    
    # print()
    # for y in range(N):
    #     print(conected[y])
    
    if visited[hy][hx] == -1: #갈 수 있는 경로 없음
        return -1

    
    cy, cx = hy, hx
    while True:

        if cy == gy and cx == gx:
            break

        path.appendleft([cy, cx])
        cy, cx = conected[cy][cx]
    
    return path
    

    

            

def raiser_gonguk(gy, gx, hy, hx, gongguk_pan, related_pan, N, M):

    go_path = bfs(gy, gx, hy, hx, gongguk_pan, N, M) 
    # print("최종루트")
    # print(go_path)

    if go_path == -1:
        return False
    
    power = gongguk_pan[gy][gx]

    for y,x in go_path:
        related_pan[y][x] = 1
        if y == hy and x == hx:
            gongguk_pan[y][x] = max(0, gongguk_pan[y][x]-power)
        else:
            gongguk_pan[y][x] = max(0, gongguk_pan[y][x]-(power//2))
    
    # print("레이저 공격후 현재 포탑")
    # for y in range(N):
    #     print(gongguk_pan[y])
    # print("레이저 공격후 턴 관련 포탑")
    # for y in range(N):
    #     print(related_pan[y])

    return True
    

def potna_gonguk(gy, gx, hy, hx, gongguk_pan, related_pan, N, M):
    dx = [1, 0, -1, 0, -1, 1, -1, 1]
    dy = [0, 1, 0, -1, -1, -1, 1, 1]

    power = gongguk_pan[gy][gx]

    gongguk_pan[hy][hx] = max(0, gongguk_pan[hy][hx]-power)

    for i in [0, 1, 2, 3, 4, 5, 6, 7]: #우하좌상 우선순위
        ny = (hy+dy[i])%N #경계뚫기
        nx = (hx+dx[i])%M

        if ny == gy and nx == gx:
            continue
        
        related_pan[ny][nx] = 1
        gongguk_pan[ny][nx] = max(0, gongguk_pan[ny][nx]-(power//2))
    
    # print("포탄 공격후 현재 포탑")
    # for y in range(N):
    #     print(gongguk_pan[y])
    # print("포탄 공격후 턴 관련 포탑")
    # for y in range(N):
    #     print(related_pan[y])


N, M, K = map(int, input().split())
gongguk_pan = [list(map(int, input().split())) for _ in range(N)]
turn_pan = [[0 for _ in range(M)] for _ in range(N)]

# print(N, M, K)
# print(gongguk_pan)
# print(turn_pan)

for turn_i in range(1, K+1):

    if get_top_cnt(gongguk_pan, N, M) < 2:
        #답 프린스 적기 나중에
        #남은 포탑중 가장 강한 공격력
        # print(max(max(gongguk_pan[y]) for y in range(N)))
        break
    
    related_pan = [[0 for _ in range(M)] for _ in range(N)]
    # print("최근에 공격한 턴 판")
    # for y in range(N):
    #    print(turn_pan[y])
     
    #공격자 찾기
    gy, gx = get_gygx(gongguk_pan, turn_pan, N, M)
    related_pan[gy][gx] = 1
    # print()
    # print("공격자 포탑(y, x)", gy, gx)

    #공격자에게 공경력 추기
    gongguk_pan[gy][gx] += (N+M)

    #공격자 턴 체크 1부터
    turn_pan[gy][gx] = turn_i

    #당하는 포탑 찾기
    hy, hx = get_hyhx(gongguk_pan, turn_pan, N, M, gy, gx)
    related_pan[hy][hx] = 1
    # print("당하는 포탑(y, x)", hy, hx )

    # print("현제 포탑")
    # for y in range(N):
    #     print(gongguk_pan[y])

    # 레이저 공격
    '''
     1. 공격자에서, 당하는자 까지 최단 경로 구하기 2개 이면 상하좌우순 ()
     2. 레이저 공격 하기
    '''
    if raiser_gonguk(gy, gx, hy, hx, gongguk_pan, related_pan, N, M) ==  False:
        potna_gonguk(gy, gx, hy, hx, gongguk_pan, related_pan, N, M)
    
    for y in range(N):
        for x in range(M):
            if related_pan[y][x] == 0 and gongguk_pan[y][x] > 0: #관련 없으면서 살아있는 포탑
                gongguk_pan[y][x] +=1
    

    # print("공격력 +1 조정후 현재 포탑")
    # for y in range(N):
    #     print(gongguk_pan[y])

    # break

print(max(max(gongguk_pan[y]) for y in range(N)))