from collections import defaultdict
from collections import deque

N, L, R = map(int, input().split())

pan = [list(map(int, input().split()))for _ in range(N)]
dy = [1, 0]
dx = [0, 1]

# for p in pan:
#     print(p)


def add_edge(grahp, a, b):
    grahp[a].append(b)
    grahp[b].append(a)

def add_edges(grahp):
    global N, L, R
    for y1 in range(N):
        for x1 in range(N):
            for i in range(2):
                y2 = y1+dy[i]
                x2 = x1+dx[i]

                if y2 < N and x2 < N:
                    if L <= abs(pan[y1][x1]-pan[y2][x2]) <= R:
                        add_edge(grahp, (y1, x1), (y2, x2))

def dfs(sy, sx, visited, connect_edges):
    sum_p = 0
    cnt = 0
    move_list = []
    
    que = deque()
    que.append([sy, sx])
    move_list.append([sy, sx])
    visited[sy][sx] = 1

    sum_p += pan[sy][sx]
    cnt +=1

    while que:
        cy, cx = que.popleft()

        if (cy, cx) in connect_edges:
            for ny, nx in connect_edges[(cy, cx)]:
                if visited[ny][nx] == 0:
                    que.append([ny, nx])
                    move_list.append([ny, nx])

                    visited[ny][nx] = 1

                    sum_p += pan[ny][nx]
                    cnt +=1
    
    # print(sum_p, cnt)
    # for v in visited:
    #     print(v)
    
    if cnt == 1:
        return False
    
    c = sum_p//cnt
    for y, x in move_list:
        pan[y][x] = c

    return True


ans = 0
while True:


    #경계설정
    connect_edges = defaultdict(list)
    add_edges(connect_edges)

    # print(connect_edges)


    #이동
    visited = [[0 for _ in range(N)] for _ in range(N)]

    is_end = True
    for y in range(N):
        for x in range(N):
            if visited[y][x] ==  0:
                is_move = dfs(y, x, visited, connect_edges)

                if is_move:
                    is_end = False
    
    # print()
    # for p in pan:
    #     print(p)

    if is_end:
        print(ans)
        break

    

    ans+=1
    # break