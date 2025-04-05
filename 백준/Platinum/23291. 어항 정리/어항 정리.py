'''
어항정리
1. 물고기의 수가 가장 적은 어항에 물고기를 한 마리 넣는다. 
    - 만약, 그러한 어항이 여러개라면 물고기의 수가 최소인 어항 모두에 한 마리씩 넣는다.

2. 어항을 쌓는다.
    1. 맨 왼쪽꺼 하나 옆에다 쌓음
    2. 2둘언 쌓음
    3. 2줄인거 쌓음
    4. 공중 부양 되기 전까지 쌓음

3. 물고기의 수를 조절
    1. 모든 인접한 두 어항에 대해서, 물고기 수의 차이를 구한다. 이 차이를 5로 나눈 몫을 d라고 하자. 
    2. d가 0보다 크면, 두 어항 중 물고기의 수가 많은 곳에 있는 물고기 d 마리를 적은 곳에 있는 곳으로 보낸다. 
    3. 이 과정은 모든 인접한 칸에 대해서 동시에 발생한다. 

4. 다시 어항을 바닥에 일렬
    - 가장 왼쪽에 있는 어항부터, 그리고 아래에 있는 어항부터 가장 위에 있는 어항까지 순서대로 바닥에 놓아야 한다. 

5. 다시 공중 부양 작업
    -  가운데를 중심으로 왼쪽 N/2개를 공중 부양시켜 전체를 시계 방향으로 180도 회전 시킨 다음, 오른쪽 N/2개의 위에 놓아야 한다. 
    - 이 작업은 두 번 반복해야한다.

6. 물고기의 수를 조절, 다시 어항을 바닥에 일렬

7. 가장 많이 들어있는 어항과 가장 적게 들어있는 어항의 물고기 수 차이 계산


물고기가 가장 많이 들어있는 어항과 가장 적게 들어있는 어항의 물고기 수 차이가 K 이하가 되려면 어항을 몇 번 

4 ≤ N ≤ 100
N은 4의 배수
0 ≤ K ≤ 10

1. 시계방향 90도 회전하는 함수
2. 두 배열을 쌓는 함수
3. 어항을 바닥에 일렬로 두는 함수
4. 물고기수 조절 함수

'''

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
            # print("두개")
            # print(tmp_bol1)
            # print(tmp_bol2)

            #1. tmp_bol1 반시계 90 회전시키기
            tmp_bol1 = degree90(tmp_bol1)

            #2. 쌓기
            tmp_bol3 = []
            tmp_bol3.append([]) # 이중 배열로 바꾸기
            for _ in range(l):
                tmp_bol3[0].append(tmp_bol2.popleft())

            tmp_bol1 = pile(tmp_bol1, tmp_bol3) # tmp_bol3위에 tmp_bol1 쌓기

            # print("쌓기")
            # for r in tmp_bol1:
            #     print(r)

        else:
            break

    if tmp_bol2:
        tmp_bol1[len(tmp_bol1) - 1] = tmp_bol1[len(tmp_bol1) - 1] + list(tmp_bol2)

        # print(tmp_bol1[len(tmp_bol1) - 1], tmp_bol2)
        l = len(tmp_bol2)
        # print(l)
        # print(len(tmp_bol1[len(tmp_bol1) - 1]), len(tmp_bol2))
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
    # print(n , m)
    for y in range(n):
        for x in range(m):
            for i in range(2):
                nx = x + dx[i]
                ny = y+ dy[i]
                # print(nx, ny, x, y, m, n)
                if -1<nx<m and -1<ny<n and not bol[ny][nx] == 0 and  not bol[y][x] == 0:
                    xynxny.append((x, y, nx, ny))

    # print(xynxny)
    for x, y, nx, ny in xynxny:
        d = abs(bol[y][x] - bol[ny][nx])
        d = d // 5

        # print("=>", bol[y][x], bol[ny][nx], d)
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

        # print(lx, ly)
        for i in range(ly):
            tmp_bol1.append(tmp_bol[i][0:lx//2])
            tmp_bol2.append(tmp_bol[i][lx//2:N])

        # print(tmp_bol1)
        # print(tmp_bol2)

        # 180 회전시키기
        tmp_bol1 = degree90(tmp_bol1)
        tmp_bol1 = degree90(tmp_bol1)

        tmp_bol = pile(tmp_bol1, tmp_bol2)

        # print("===>", i)
        # for y in range(len(tmp_bol)):
        #     print(tmp_bol[y])



    return tmp_bol



N, K = map(int, input().split()) #100
bol = list(map(int, input().split())) #길이 N

ans = 0
while True:
    bol_min = min(bol)
    bol_max = max(bol)

    if bol_max-bol_min <= K:
        # print(bol_max-bol_min, ans)
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
    # print("==> 공중부양 계산1")
    # for y in range(len(bol)):
    #     print(bol[y])

    #3 물고기수 조절
    bol = moovFish()
    # print("==> 물고기 계산")
    # for y in range(len(bol)):
    #     print(bol[y])

    #4. 바닥에 일렬로
    bol = downBol()
    # print("==>바닥에 일렬로1")
    # print(bol)

    bol = levitation2()
    # print("==> 공중부양 계산2")
    # for y in range(len(bol)):
    #     print(bol[y])

    bol = moovFish()
    # print("==> 물고기 계산")
    # for y in range(len(bol)):
    #     print(bol[y])

    bol = downBol()
    # print("==>바닥에 일렬로2")
    # print(bol)








