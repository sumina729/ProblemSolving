from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visit = [[0 for _ in range(N)]for _ in range(N)]

def bfs(x, y, n):
    que = deque()
    que.append((x, y))

    while que:
        x, y = que.popleft()
        
        dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if -1 < nx < N and -1 < ny < N and graph[ny][nx] > n  and visit[ny][nx] ==0 :
                visit[ny][nx] = 1
                que.append((x+dx[i],y+dy[i]))
    

max_r = max(map(max, graph))
ans = 0

for i in range(0, max_r):
    visit = [[0 for _ in range(N)]for _ in range(N)]
    num = 0
    for y in range(N):
        for x in range(N):
            if graph[y][x] > i and visit[y][x] == 0:
                num+=1
                bfs(x, y, i)
    ans = max(ans, num)

print(ans)