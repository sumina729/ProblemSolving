'''
N×N 크기의 격자
0은 빈칸, 1은 벽을 나타낸다.
M명의 승객을 태우는 것이 목표

1.  현재 위치에서 최단거리가 가장 짧은 승객을 고른다
    - 승객이 여러 명이면 그중 행 번호가 가장 작은 승객. -> y가 작은거
    - 그런 승객도 여러 명이면 그중 열 번호가 가장 작은 승객. -> x가 작은거
    - 택시와 승객이 같은 위치에 서 있으면 그 승객까지의 최단거리는 0
2. 연료는 한 칸 이동할 때마다 1만큼 소모된다. 
3. 한 승객을 목적지로 성공적으로 이동시키면, 
    - 그 승객을 태워 이동하면서 소모한 연료 양의 두 배가 충전된다.

4. 도중에 연료가 바닥나면 이동에 실패하고, 그 날의 업무가 끝난다.
5. 승객을 목적지로 이동시킨 동시에 연료가 바닥나는 경우는 실패한 것으로 간주하지 않는다. ***

모든 승객을 성공적으로 데려다줄 수 있는지 알아내고, 
데려다줄 수 있을 경우 최종적으로 남는 연료의 양을 출력
다음 출발지나 목적지로 이동할 수 없으면 -1을 출력한다. 
모든 손님을 이동시킬 수 없는 경우에도 -1을 출력한다.
'''

from collections import deque


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(ty, tx, pan, N):
    visited = [[-1 for _ in range(N)]for _ in range(N)]

    que = deque()
    que.append((tx, ty))
    visited[ty][tx] = 0

    while que:
        cx, cy = que.popleft()

        for i in range(4):
            nx = cx+dx[i]
            ny = cy+dy[i]

            if -1<nx<N and -1<ny<N and visited[ny][nx] == -1 and  pan[ny][nx] == 0:
                que.append((nx, ny))
                visited[ny][nx] = visited[cy][cx]+1
    
    return visited

        

def get_gngl(ty, tx, p_list, pan, N, M):
    min_l = N*N
    min_y = N
    min_x = N
    pi = -1

    v_pan = bfs(ty, tx, pan, N)
    for i in range(len(p_list)):
        py, px, gy, gx = p_list[i]

        pl = v_pan[py][px]
        if pl == -1:
            continue
        # print("택시와 사람의 거리:",i, pl)
        if (min_l, min_y, min_x) > (pl, py, px):
            min_l = pl
            min_y = py
            min_x = px
            pi = i
    
    return pi, min_l
    
N, M, F = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(N)]
ty, tx = map(int, input().split())
p_list = [list(map(int, input().split())) for _ in range(M)]

ty-=1
tx-=1
for i in range(M):
    py, px, gy, gx = p_list[i]
    p_list[i] = [py-1, px-1, gy-1, gx-1]


# print()
id_complite = True 
while p_list:

    # print()
    # print()

    #승객 고르기 0~m-1
    pn, pl, = get_gngl(ty, tx, p_list, pan, N, M)

    if pn == -1:
        print(-1)
        id_complite = False
        break

    py, px, gy, gx = p_list[pn]
    # print("최종고른 사람:", px, py, pn, pl)

    #사람태우러 가기
    F = F-pl
    tx = px
    ty = py

    #이동실패
    if F < 0: 
        print(-1)
        id_complite = False
        break

    #도착지도 이동 
    v_pan = bfs(ty, tx, pan, N)
    ml = v_pan[gy][gx]
    if ml == -1:
        print(-1)
        id_complite = False
        break

    # print("택시이동거리", ml)

    F = F-ml

    #이동실패
    if F < 0: 
        print(-1)
        id_complite = False
        break

    #이동 완료
    tx = gx
    ty = gy
    p_list.pop(pn)

    F = F + ml*2

    # print("이동 완료후")
    # print(F, p_list, tx, ty)

    # break

if id_complite:
    print(F)