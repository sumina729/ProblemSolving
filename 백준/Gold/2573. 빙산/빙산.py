from collections import deque
N, M = map(int, input().split())

graph = [list(map(int, input().split()))for _ in range(N)]
visit = [[0 for _ in range(M)] for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


b_list = []
for y in range(N):
    for x in range(M):
        if graph[y][x] > 0:
            b_list.append((x, y))

def bfs(x, y):
    que = deque()
    que.append((x, y))
    visit[y][x] = 1

    m_list = []

    while que:
        x, y = que.popleft()

        ac = 0
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            
            if -1 < nx < M and -1 < ny < N :
                if graph[ny][nx] == 0: #바다이면
                    ac+=1
                elif visit[ny][nx] == 0: # 바다 아닌데, 방문 안되거면
                    que.append((nx, ny))
                    visit[ny][nx] = 1
        m_list.append((x, y, ac))

    for x, y, ac in m_list:
        graph[y][x] = max(0, graph[y][x] - ac)

    # print()
    # for i in range(N):
    #     print(*visit[i])
    

year = 0
while True:
    cnt = 0
    db_list = []
    visit = [[0 for _ in range(M)] for _ in range(N)]

    if not b_list:
        print(0)
        break
    for x, y in b_list:
        if visit[y][x] == 0:
            cnt+=1
            bfs(x, y)
        if graph[y][x] == 0:
            db_list.append((x, y))   

    if cnt > 1:
        print(year)
        break

    b_list = list(set(b_list) - set(db_list)) 
    year+=1

    
