'''
(y, x)
한 칸에는 물고기가 한 마리 존재한다.
1보다 크거나 같고, 16보다 작거나 같은 자연수

청소년 상어는 (0, 0)에 있는 물고기를 먹고
(0, 0)에 들어가게 된다
상어의 방향은 (0, 0)에 있던 물고기의 방향과 같음

물고기이동
- 번호가 작은 물고기부터 순서대로
- 물고기는 한 칸을 이동
    이동할 수 있는 칸: 빈 칸과 다른 물고기가 있는 칸
    이동할 수 없는 칸: 상어가 있거나, 공간의 경계를 넘는 칸
- 물고기는 방향이 이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계 회전시킨다. 
- 만약 이동할 수 있는 칸이 없으면 이동을 하지 않는다
- 그 외의 경우에는 그 칸으로 이동을 한다. 
    - 물고기가 다른 물고기가 있는 칸으로 이동할 때는 서로의 위치를 바꾸는 방식으로 이동한다.

상어이동
- 상어는 방향에 있는 칸으로 이동할 수 있는데
- 한 번에 여러 개의 칸을 이동할 수 있다. (가고싶은데 모든 경우의수)
    - 이동하는 중에 지나가는 칸에 있는 물고기는 먹지 않는다.
- 물고기가 없는 칸으로는 이동할 수 없다. 
- 상어가 물고기가 있는 칸으로 이동했다면, 
    그 칸에 있는 물고기를 먹고, 
    그 물고기의 방향을 가지게 된다.

- 상어가 이동할 수 있는 칸이 없으면 공간에서 벗어나 집으로 간다.

=> 근데 상어가 가장 많이 먹을 수 있는 경로로

'''

import copy

# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

def get_xy(n, pan):
    for y in range(4):
        for x in range(4):
            if pan[y][x][0] == n:
                return x, y
            
    return -1, -1 # 없음

def move_f(n, pan):
    #i번 상어가 있는 죄표 구하기
    cx, cy = get_xy(n, pan) 

    if cx == -1: # 상어 없으면 리턴
        return
    
    # 있으면 이동 
    cd = pan[cy][cx][1]-1
    for i in range(8):
        # print()
        nd = (cd+i)%8 #시계반대방향
        nx = cx+dx[nd]
        ny = cy+dy[nd]

        if -1<nx<4 and -1<ny<4 and not pan[ny][nx][0] == 0: # 경계 이내이면서 상어가 없으면
            #위치 바꾸기
            pan[cy][cx][1] = nd+1

            tmp = pan[ny][nx]
            pan[ny][nx] = pan[cy][cx]
            pan[cy][cx] = tmp

            return


def dfs_move_s(cx, cy, pan, cd, sum):

    global ans
    
    l = 1
    is_end = True
    while True:
        nx = cx+dx[cd-1]*l
        ny = cy+dy[cd-1]*l

        if not (-1<nx<4 and -1<ny<4): # 범위를 벗어나면 이 뱡향으로 가는건 끝
            break

        if  pan[ny][nx][0] > 0: #가는 곳에 물고기 있으면
            # new_pan = copy.deepcopy(pan)
            new_pan =  [[c[:] for c in r ] for r in pan]

            #상어이동
            nd = new_pan[ny][nx][1]
            ni = new_pan[ny][nx][0]
            new_pan[ny][nx] = [0, nd]
            new_pan[cy][cx] = [-1, -1]

            #물고기 이동
            for n in range(1, 17):
                move_f(n, new_pan)
            
            sx, sy = get_xy(0, new_pan) 
            dfs_move_s(sx, sy, new_pan, new_pan[sy][sx][1], sum+ni)

            is_end = False  

        l+=1
    
    if is_end:
        ans = max(ans,sum)

    
    
ans = 0
pan = []
for _ in range(4):
    intput_list = list(map(int, input().split()))
    tmp = []
    for i in range(0, 8, 2):
        tmp.append([intput_list[i], intput_list[i+1]])

    pan.append(tmp)


ni = pan[0][0][0]
pan[0][0][0] = 0 # 상어로 변경

#물고기 이동 1~16
for n in range(1, 17):
    move_f(n, pan)

# 상어 이동
sx, sy = get_xy(0, pan) 
dfs_move_s(sx, sy, pan, pan[sy][sx][1], ni)

print(ans)