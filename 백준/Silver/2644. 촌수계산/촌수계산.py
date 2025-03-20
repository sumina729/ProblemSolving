from collections import deque

n = int(input())
p1, p2 = map(int, input().split())
m = int(input())

glaph = [[0 for _ in range(n+1)]for _ in range(n+1)]
#-1 방문 x
visit = [-1 for _ in range(n+1)]


for _ in range(m):
    v1, v2 = map(int, input().split())
    
    glaph[v1][v2] = glaph[v2][v1] = 1


#최단경로
def bfs(v):

    ans = 0
    que = deque()
    que.append(v)
    visit[v] = 0

    while que:
        v = que.popleft()
        for i in range(1, n+1):
            if glaph[v][i] and visit[i] == -1:
                que.append(i)
                visit[i] = visit[v] + 1


bfs(p1)
print(visit[p2]) 
