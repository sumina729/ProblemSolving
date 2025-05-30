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

def is_in(pan, i, N):
    for p in pan:
        if i in p:
            return True

    return False

def ok(new_pan, pan, mxl, myl, N, i):
    
    for y in range(N):
        for x in range(N):
            if  pan[y][x] == i:
                nx = x+mxl
                ny = y+myl
                if not (-1<nx<N and -1<ny<N) or not new_pan[ny][nx] == 0: #하나라도 범위에 넘어가거나, 다른 미생물이 있가면
                    return False
    return True
            
def get_sxsy(new_pan, N, ix, iy, i):
    for x in range(N):
        for y in range(N-1, -1, -1):
            if new_pan[y][x] == 0:
                mxl = x-ix
                myl = y-iy
                if ok(new_pan, pan, mxl, myl, N, i):
                    return x, y
    return -1, -1

def get_ixiy(pan, i, N):
    min_x = N
    max_y = -1

    for y in range(N):
        for x in range(N):
            if pan[y][x] == i:
                if (min_x, -max_y) > (x, -y):
                    min_x = x
                    max_y = y
    # print("가장 왼쪽 아래", min_x, max_y)
    return min_x, max_y #가장 왼쪽중, 가장 아래 죄표


def move_pan(new_pan, pan, mxl, myl, N, i):
    for y in range(N):
        for x in range(N):
            if pan[y][x] == i:
                nx = x+mxl
                ny = y+myl
                # if not new_pan[ny][nx] == 0:
                #     print("!!!!!!!이상한 위치 잡음 코드 다시보거나, 논리 다시 생각")
                new_pan[ny][nx] = i

def set_pan(pan, order_i, N):
    new_pan = [[0 for _ in range(N)] for _ in range(N)]

    '''
    옮기기
    - 형태 유지, 범위 벗어나지x, 
    - 최대한 x가 잔으 왼쪽 위치  -> 가장 왼쪽
    - 여러개이면 y작은위치 -> 가장 아래
    - 둘곳 없으면 사라짐
    '''
    for i in order_i: #순서대로 집어넣기
        #i 미생물의 가장 왼쪽이면서 왼쪽중에 가장 아래 좌표
        ix, iy = get_ixiy(pan, i, N) 
        sx, sy = get_sxsy(new_pan, N, ix, iy, i)

        # print(ix, iy, "->", sx, sy)
        if sx == -1:
            continue 
        mxl = sx-ix
        myl = sy-iy

        # print(sx, sy, ix, iy, mxl, myl, lx, ly)
        move_pan(new_pan, pan, mxl, myl, N, i)
        

    return new_pan

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

    #배양용기에 투입
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
    for i in range(1, qn): # 1번 부터 현재 들어온거 보다 전에 있는 거들 중
        remove_tong(pan, i, N)
    

    ############디버깅용##########  
    # print()
    # print("분리된 배양 용기 찾아서 지우기")
    # for y in range(N):
    #     print(pan[y])
    ############디버깅용########## 
    
    
    #배양용기 이동
    sum_list = [sum_(i, pan, N) for i in range(qn+1)] #0~qn
    order_i = []
    for i in range(1, qn+1): #1~qn 중에 
        if is_in(pan, i, N): #현제 용기에 있는 미생물 고르고 넣기
            order_i.append(i)

    order_i = sorted(order_i, key=lambda i: (-sum_list[i], i))

    ############디버깅용##########  
    # print()
    # print("배양용기 이동 순서")
    # print(sum_list)
    # print(order_i)
    ############디버깅용##########

    pan = set_pan(pan, order_i, N)

    ############디버깅용##########  
    # print()
    # print("새로운 배양용기로 이동")
    # for y in range(N):
    #     print(pan[y])
    ############디버깅용########## 

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

