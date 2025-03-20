from collections import deque

#가로, 세로, 높이
M, N, H = map(int, input().split())

graph = []

for _ in range(H):
    tmp = []
    for _ in range(N): 
        tmp.append(list(map(int, input().split())))
    graph.append(tmp)
        

# graph[h][y][x]

que = deque()
for h in range(H):
        for y in range(N):
            for x in range(M):
                if graph[h][y][x] == 1:
                    que.append((x, y, h))


def bfs():
    dx = [1, 0, -1, 0, 0, 0]
    dy = [0, 1, 0, -1, 0, 0]
    dh = [0, 0, 0, 0, 1, -1]

    while que:
        x, y, h = que.popleft()

        for i in range(6):
            tx = x+dx[i]
            ty = y+dy[i]
            th = h+dh[i]

            if -1 < tx < M and -1 < ty < N and -1 < th < H and graph[th][ty][tx]==0:
                graph[th][ty][tx] = graph[h][y][x] +1
                que.append((tx, ty, th))

bfs()
    


is_ans = 1
ans = 0
for h in range(H):
    for y in range(N):
        for x in range(M):
            if graph[h][y][x] == 0:
                is_ans = 0
                
    
            ans = max(ans, graph[h][y][x])

if is_ans:
    print(ans-1)
else:
    print(-1)
