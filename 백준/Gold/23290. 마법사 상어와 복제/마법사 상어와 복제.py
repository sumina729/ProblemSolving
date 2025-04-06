'''
격자에는 물고기 M마리가 있다.
    - 각 물고기는 격자의 칸 하나에 들어가 있으며, 이동 방향을 가지고 있다.
    -이동 방향은 8가지 방향(상하좌우, 대각선) 중 하나이다.
    - 마법사 상어도 연습을 위해 격자에 들어가있다. 상어도 격자의 한 칸에 들어가있다.
    - 둘 이상의 물고기가 같은 칸에 있을 수도 있으며, 마법사 상어와 물고기가 같은 칸에 있을 수도 있다.

상어의 마법 연습 한 번은 다음과 같은 작업이 순차적으로 이루어진다.
    1. 상어가 모든 물고기에게 복제 마법을 시전한다. (복제 마법은 시간이 조금 걸리기 때문에, 아래 5번에서 물고기가 복제되어 칸에 나타난다.)
    2. 모든 물고기가 한 칸 이동한다.
        - 상어가 있는 칸, 물고기의 냄새가 있는 칸, 격자의 범위를 벗어나는 칸으로는 이동할 수 없다.
        - 각 물고기는 자신이 가지고 있는 이동 방향이 이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계 회전시킨다.
            - 만약, 이동할 수 있는 칸이 없으면 이동을 하지 않는다.
            - 그 외의 경우에는 그 칸으로 이동을 한다.
    3. 상어가 연속해서 3칸 이동한다.
        - 상어는 현재 칸에서 상하좌우로 인접한 칸으로 이동할 수 있다
        - 연속해서 이동하는 칸 중에 격자의 범위를 벗어나는 칸이 있으면, 그 방법은 불가능한 이동 방법이다.
        - 연속해서 이동하는 중에 상어가 물고기가 있는 같은 칸으로 이동하게 된다면,
            - 그 칸에 있는 모든 물고기는 격자에서 제외되며
            - 제외되는 모든 물고기는 물고기 냄새를 남긴다.
        - 가능한 이동 방법 중에서 제외되는 물고기의 수가 가장 많은 방법으로 이동하며,
        - 그러한 방법이 여러가지인 경우 사전 순으로 가장 앞서는 방법을 이용한다.
    4. 두 번 전 연습에서 생긴 물고기의 냄새가 격자에서 사라진다.
    5. 1에서 사용한 복제 마법이 완료된다. 모든 복제된 물고기는 1에서의 위치와 방향을 그대로 갖게 된다.

함수1 모든 물고기 이동 함수
    -
함수2 상어이동함수
함수3. 물고기의 냄새삭제

0~7 물고기(방향)


'''

import copy
from operator import is_not
from os import remove


def moveFish(copyPan):

    global sx, sy, blood
    tmp_pan = [[[]for i in range(4)] for j in range(4)]
    # ←, ↖, ↑, ↗, →, ↘, ↓, ↙
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, -1, -1, -1, 0, 1, 1, 1]

    for y in range(4):
        for x in range(4):
            if len(copyPan[y][x]) > 0: #물고기가 있으면
                for fd in copyPan[y][x]: #물고기 한마리씩 꺼내기
                    #y, x, fd 물고기 이동시키기
                    is_not_go = 1 # 갈수 있는 칸 있는지 없는지
                    for i in range(8): #반시계로 45도 회던
                        nx = x + dx[(fd-i)%8]
                        ny = y + dy[(fd-i)%8]

                        if -1<nx<4 and -1<ny<4 and not (nx == sx and ny == sy): #경계아니고, 상어위치 아니고
                            is_not_b = 1
                            for bx, by, bs in blood: # 위치가 피인지 아닌지 찾기
                                if nx == bx and ny == by:
                                    # print(fd, x, y, nx, ny, bx, by, bs)
                                    is_not_b = 0 # 피가 있으면 0
                                    break

                            if is_not_b: # 피 위치 아니면
                                is_not_go = 0 # 갈 자리 있음
                                tmp_pan[ny][nx].append((fd-i)%8)
                                # print(x, y, nx, ny)
                                break
                    if is_not_go: #갈수 있는 곳 없으면 제자리
                        tmp_pan[y][x].append(fd)
    return tmp_pan



visited = [[0 for i in range(4)] for j in range(4)]
msn = []
msd = []
max_n = -1

# ↑, ←, ↓, →
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def dfs(x, y, d, n):

    global msn, msd, max_n

    if len(d) == 3:
        # print(x, y, d, n)
        if max_n < n:
            max_n = n
        msd.append(copy.deepcopy(d))
        msn.append(n)
        return


    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if -1<nx<4 and -1<ny<4:
            d.append(i)
            if visited[ny][nx] == 1:
                dfs(nx, ny, d, n)
            else:
                visited[ny][nx] = 1
                dfs(nx, ny, d, n + len(copyPan[ny][nx]))
                visited[ny][nx] = 0

            d.pop()




def moveSak():
    global sx, sy, msn, msd, max_n, blood, copyPan
    visited = [[0 for i in range(4)] for j in range(4)]
    msn = []
    msd = []
    max_n = -1

    visited[sy][sx] = 1
    dfs(sx, sy, [], 0) # 가능한 이동 방향 찾기
    # print(msn)
    # print(msd)

    #방향하나 정하기
    select_d = []

    # print("물고기최대수", max_n)
    for i in range(len(msn)): #가능한 이동 방향 갯수
        if msn[i] == max_n: #그중에 max_n 값인거 중에 첫째가 사전순으로 높은거
            select_d = copy.deepcopy(msd[i])
            break

    # print("상어이동경로", select_d)

    for i in range(len(blood)): #피 아나씩 줄이기
        blood[i][2] = blood[i][2] - 1  # 이전꺼 다 하나씩 약하게

    for i in select_d: # 3방얄으로 가기
        sx = sx+dx[i]
        sy = sy+dy[i]

        if len(copyPan[sy][sx]) > 0: #물고기 있으면
            copyPan[sy][sx].clear() #지우기 #물고기 지우기
            blood.append([sx, sy, -1]) #새로운피남기기






M, S = map(int, input().split())
pan = [[[]for _ in range(4)] for _ in range(4)]

f_xyd = []
for i in range(M):
    y, x, s = map(int, input().split())
    f_xyd.append((x-1, y-1, s-1))
    pan[y-1][x-1].append(s-1)

sy,sx = map(int, input().split())
sx = sx-1
sy = sy-1
blood = [] #bx, by, bs


for q in range(S):
    # print("========== 이동시작", q+1)
    # print("========== 이동시작", q+1)
    # for i in range(4):
    #     print(pan[i])

    copyPan = copy.deepcopy(pan)

    # 1. 모든 물고기 이동 함수
    copyPan = moveFish(copyPan)
    # print("===> 물고기 이동")
    # for i in range(4):
    #     print(copyPan[i])

    # 2. 상어이동
    # print("===> 상어 이동", sx, sy)
    moveSak()
    # for i in range(4):
    #     print(copyPan[i])
    # print(sx, sy)


    # -3 인 피 지우기
    # print(blood)

    newblood= []
    for i in range(len(blood)):
        if blood[i][2] > -3:
            newblood.append(blood[i])
    blood = copy.deepcopy(newblood)
    # print("==> 피")
    # print(blood)

    #복제하기
    # print("==>물로기 복제")
    for x in range(4):
        for y in range(4):
            pan[y][x] = copy.deepcopy(pan[y][x] +copyPan[y][x])

    # for i in range(4):
    #     print(pan[i])

ans = 0
for x in range(4):
    for y in range(4):
        ans += len(pan[y][x])

print(ans)
