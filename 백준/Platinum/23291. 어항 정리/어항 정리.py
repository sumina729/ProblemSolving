from collections import deque
import copy

def pile(t1, t2):  # t2 위에 t1쌓기
    # 이중, 이중
    pile_t = t1+t2
    return pile_t


def degree90(b):
    degree_t = [[0 for _ in range(len(b))] for _ in range(len(b[0]))]

    for y in range(len(b)):
        for x in range(len(b[0])):
            degree_t[x][len(b)-1-y] = b[y][x]

    return degree_t


def levitation1():
    global  bol, N
    tmp_bol1 = [[bol[0]]] #이중 배열
    tmp_bol2 = deque(bol[1:N])#이중 배열

    while True:
        l = len(tmp_bol1)
        if l <= len(tmp_bol2):

            #1. tmp_bol1 반시계 90 회전시키기
            tmp_bol1 = degree90(tmp_bol1)

            #2. 쌓기
            tmp_bol3 = []
            tmp_bol3.append([]) # 이중 배열로 바꾸기
            for _ in range(l):
                tmp_bol3[0].append(tmp_bol2.popleft())

            tmp_bol1 = pile(tmp_bol1, tmp_bol3) # tmp_bol3위에 tmp_bol1 쌓기

        else:
            break

    if tmp_bol2:
        tmp_bol1[len(tmp_bol1) - 1] = tmp_bol1[len(tmp_bol1) - 1] + list(tmp_bol2)

        l = len(tmp_bol2)
        for y in range(len(tmp_bol1)-1):
            for _ in range(l):
                tmp_bol1[y].append(0)

    return tmp_bol1

dx, dy = [1,  0], [0, 1]
def moovFish():
    global bol
    tmp_bol = copy.deepcopy(bol)

    n , m = len(bol), len(bol[0])
    visited = [[ 0 for _ in range(m)] for _ in range(n)]
    xynxny = []
    for y in range(n):
        for x in range(m):
            for i in range(2):
                nx = x + dx[i]
                ny = y+ dy[i]
                # print(nx, ny, x, y, m, n)
                if -1<nx<m and -1<ny<n and not bol[ny][nx] == 0 and  not bol[y][x] == 0:
                    xynxny.append((x, y, nx, ny))

    for x, y, nx, ny in xynxny:
        d = abs(bol[y][x] - bol[ny][nx])
        d = d // 5

        if d > 0:
            if bol[y][x] < bol[ny][nx]:
                tmp_bol[y][x] = tmp_bol[y][x] + d
                tmp_bol[ny][nx] = tmp_bol[ny][nx] - d
            else:
                tmp_bol[ny][nx] = tmp_bol[ny][nx] + d
                tmp_bol[y][x] = tmp_bol[y][x] - d

    return tmp_bol


def downBol():
    global bol, N
    tmp_bol = []

    n, m = len(bol), len(bol[0])

    for x in range(m):
        for y in range(n-1,-1,-1):
            if not bol[y][x] ==0:
                tmp_bol.append(bol[y][x])

    return tmp_bol


def levitation2():
    global  bol, N
    tmp_bol = [copy.deepcopy(bol)]

    for i in range(2):

        lx = len(tmp_bol[0])
        ly = len(tmp_bol)
        tmp_bol1 = []
        tmp_bol2 = []

        for i in range(ly):
            tmp_bol1.append(tmp_bol[i][0:lx//2])
            tmp_bol2.append(tmp_bol[i][lx//2:N])

        # 180 회전시키기
        tmp_bol1 = degree90(tmp_bol1)
        tmp_bol1 = degree90(tmp_bol1)

        tmp_bol = pile(tmp_bol1, tmp_bol2)

    return tmp_bol



N, K = map(int, input().split()) #100
bol = list(map(int, input().split())) #길이 N

ans = 0
while True:
    bol_min = min(bol)
    bol_max = max(bol)

    if bol_max-bol_min <= K:
        print(ans)
        break

    ans+=1
    #1. 물고기의 수가 가장 적은 어항에 물고기를 한 마리 넣는다.
    min_f = min(bol) #100
    for i in range(N):
        if bol[i] == min_f:
            bol[i]+=1

    #2. 공중 부양 작업1
    bol = levitation1()

    #3 물고기수 조절
    bol = moovFish()

    #4. 바닥에 일렬로
    bol = downBol()

    # 5. 공중부양 계산2
    bol = levitation2()

    # 6 물고기수 조절
    bol = moovFish()

    # 7. 바닥에 일렬로
    bol = downBol()