from collections import deque

N = int(input())
graph = [ list(map(int, input()))for _ in range(N)]

def bfs(x, y):
    que = deque()
    que.append((x, y))
    graph[y][x] = 0
    ans = 1

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    while que:
        tx, ty = que.popleft()
    
        for i in range(4):
            if -1 < ty+dy[i] < N and -1 < tx+dx[i] < N and graph[ty+dy[i]][tx+dx[i]]:
                que.append((tx+dx[i], ty+dy[i]))
                graph[ty+dy[i]][tx+dx[i]] = 0
                ans+=1


    return ans


num = 0
ans_l = []

for y in range(N):
    for x in range(N):
        if graph[y][x]:
            num+=1
            ans_l.append(bfs(x, y))

ans_l.sort()

print(num)
for i in range(num):
    print(ans_l[i])
