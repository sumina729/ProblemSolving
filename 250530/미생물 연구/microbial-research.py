'''
N*N 크기
죄측하단 -> 0, 0
우측상단 N, N

Q 번의 실행

1. 미생물 투입
- 죄측하단, 우측상단 의 직사각형 미샐물 투입
- 만약에 역역 내이 이미 다름 미생물 있으면 잡아먹음
- 만약에 이전 무리가 둘 이상의 영역으로나뉘게 된마녀 모드 사라짐

2. 배양용기 이동

미생물 옮기는 순서
- 새로운 배양 용기 크기 같음
- 가장 넓은 무리 선택
- 만약 같다면, 가장 먼저 투입된 미생물선택

옮기기
- 형태 유지, 범위 벗어나지x, 
- 최대한 x가 잔으 왼쪽 위치
- 여러개이면 y작은위치
- 둘곳 없으면 사라짐

3. 실험결과 기록
- 인접한 무리 끼리 넓이*넚이, 인접한 두 무리는 한번만 계싼
그리고 그 곱합 값 들의 합

'''
from collections import deque


def bfs(x, y, visited, i, N, pan):

    que = deque()
    que.append((x, y))
    visited[y][x] = 1

    while que:
        x, y = que.popleft()
        for dx, dy in [(0, 1), (0, -1), (1,0), (-1, 0)]:
            nx = x+dx
            ny = y+dy

            if -1<nx<N and -1<ny<N and visited[ny][nx] == 0 and pan[ny][nx] == i:
                que.append((nx, ny))
                visited[ny][nx] = 1 


def remove_(N, i, pan):
    for y in range(N):
        for x in range(N):
            if pan[y][x] == i:
                pan[y][x] = 0

def remove_tong(pan, i, N):

    visited = [[0 for _ in range(N)]for _ in range(N)]
    cnt = 0
    for y in range(N):
        for x in range(N):
            if pan[y][x] == i and visited[y][x] == 0:
                cnt+=1
                if cnt>1:
                    remove_(N, i, pan)
                    ############디버깅용##########  
                    # print()
                    # print(i,"번 지움")
                    ############디버깅용##########
                    return
                bfs(x, y, visited, i, N, pan)

    ############디버깅용##########  
    # print()
    # print(i,"번 안지움")
    ############디버깅용##########

def sum_(i, pan, N):
    if i == 0:
        return 0

    cnt = 0
    for y in range(N):
        for x in range(N):    
            if pan[y][x] == i:
                    cnt+=1

    return cnt


def get_sxsy(new_pan, N, lx, ly, ix, iy, i):
    for x in range(N):
        for y in range(N-1, -1, -1):
            if new_pan[y][x] == 0 and x+lx-1 < N and y-ly+1 > -1:
                mxl = x-ix
                myl = y-iy
                if ok(new_pan, pan, mxl, myl, N, i):
                    return x, y
    return -1, -1
            
def get_ixiy(pan, i, N):
    min_x, max_x = N, -1
    min_y, max_y = N, -1

    for y in range(N):
        for x in range(N):
            if pan[y][x] == i:
                min_x = min(min_x, x)
                max_x = max(max_x, x)
                min_y = min(min_y, y)
                max_y = max(max_y, y)

    return min_x, max_y, max_x-min_x+1, max_y-min_y+1

def ok(new_pan, pan, mxl, myl, N, i):
    for y in range(N):
        for x in range(N):
            if pan[y][x] == i and not new_pan[y+myl][x+mxl] == 0:
                return False
            
    return True

def move_pan(new_pan, pan, mxl, myl, N, i):
    for y in range(N):
        for x in range(N):
            if pan[y][x] == i:
                new_pan[y+myl][x+mxl] = i



def set_pan(pan, order_i, N):
    new_pan = [[0 for _ in range(N)] for _ in range(N)]

    for i in order_i:
        ix, iy, lx, ly = get_ixiy(pan, i, N)
        sx, sy = get_sxsy(new_pan, N, lx, ly, ix, iy, i)
        
        if sx == -1:
            continue

        mxl = sx-ix
        myl = sy-iy

        # print(sx, sy, ix, iy, mxl, myl, lx, ly)
        move_pan(new_pan, pan, mxl, myl, N, i)




    return new_pan


def is_in(pan, i, N):
    for p in pan:
        if i in p:
            return True

    return False

N, G = map(int, input().split())
r1c1r2c2 = [list(map(int, input().split())) for _ in range(G)]

# print(N, G)
# print(r1c1r2c2)

pan = [[0 for _ in range(N)] for _ in range(N)]
qn = 0
for r1, c1, r2, c2 in r1c1r2c2:
    qn+=1

    ly, lx = c2-c1, r2-r1
    sy, sx = N-(c1+ly), r1

    # print(sx, sy, lx, ly)

    #배양용기 이동
    for y in range(ly):
        for x in range(lx):
            pan[sy+y][sx+x] = qn


    ############디버깅용##########  
    # print()
    # print("배양용기에 집어넣기")
    # for y in range(N):
    #     print(pan[y])
    ############디버깅용########## 

    #분리된 배양 용기 찾아서 지우기
    for i in range(1, qn): # 현재 들어온거 보다 전에 있는 거들 중
        remove_tong(pan, i, N)
    

    ############디버깅용##########  
    # print()
    # print("분리된 배양 용기 찾아서 지우기")
    # for y in range(N):
    #     print(pan[y])
    ############디버깅용########## 
    
    
    #배양용기 이동
    sum_list = [sum_(i, pan, N) for i in range(qn+1)]
    order_i = []
    for i in range(qn):
        if is_in(pan, i+1, N):
            order_i.append(i+1)

    order_i = sorted(order_i, key=lambda i: (-sum_list[i], i))

    ############디버깅용##########  
    # print()
    # print("배양용기 이동 순서")
    # print(order_i)
    ############디버깅용##########  

    pan = set_pan(pan, order_i, N) #여기서 둘곳 없으면 지워집

    ############디버깅용##########  
    # print()
    # print("새로운 배양용기로 이동")
    # for y in range(N):
    #     print(pan[y])
    ############디버깅용########## 
    

    #실험결과 기록
    tu = set()
    sum = 0
    for y in range(N):
        for x in range(N):
            for dx, dy in [(0, 1), (0, -1), (1,0), (-1, 0)]:
                nx = x+dx
                ny = y+dy

                if -1<nx<N and -1<ny<N and not pan[y][x] == pan[ny][nx]:
                    i1 = pan[y][x]
                    i2 = pan[ny][nx]
                    if not (i1, i2) in tu:
                        tu.add((i1, i2))
                        tu.add((i2, i1))
                        sum+= (sum_list[i1]*sum_list[i2])
    # print("답")
    print(sum)

    # break

