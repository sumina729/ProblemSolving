from collections import deque
N, M = map(int, input().split())

graph = [list(map(int, input().split()))for _ in range(N)]
visit = [[0 for _ in range(M)] for _ in range(N)]


# print(graph)

# 인접해있는 칸 수 확인하기
# 인접해있는 칸 수 만큼 녹이기
# 덩어리가 몇개인지 확인하기(BFS)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

sea = [[0 for _ in range(M)] for _ in range(N)]

def melt(x, y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if -1 < nx < M and -1 < ny < N and graph[ny][nx] == 0:
            sea[y][x]+=1

def bfs(x, y):
    que = deque()
    que.append((x, y))
    visit[y][x] = 1

    while que:
        x, y = que.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if -1 < nx < M and -1 < ny < N and visit[ny][nx] == 0 and graph[ny][nx] > 0:
                visit[ny][nx] = 1
                que.append((nx, ny))


ans = 0
while True:
    visit = [[0 for _ in range(M)] for _ in range(N)]
    cnt = 0

    for y in range(N):
        for x in range(M):
            if graph[y][x] > 0:
                cnt+=1
                melt(x, y)

    if cnt ==  0:
        print(0)
        break

    for y in range(N):
        for x in range(M):
            graph[y][x] = max(0, graph[y][x]-sea[y][x])
            sea[y][x] = 0

    

    grupe_n = 0
    for y in range(N):
        for x in range(M):
            if graph[y][x] > 0 and visit[y][x] == 0:
                grupe_n+=1
                bfs(x, y)
    
    ans+=1
    if grupe_n > 1:
        print(ans)
        break
    