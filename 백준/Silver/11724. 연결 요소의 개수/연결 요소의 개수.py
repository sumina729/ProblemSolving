
from collections import deque

import sys
input = sys.stdin.readline

def bfs(n):
    global vivited, graph

    que = deque()
    que.append(n)
    vivited[n] = 1

    while que:
        n = que.popleft()

        for nxt in graph[n]:
            if vivited[nxt] == 0:
                que.append(nxt)
                vivited[nxt] = 1

N, M = map(int, input().split())


graph = [[] for _ in range(N+1)]

for _ in range(M):
    i, j = map(int, input().split())

    graph[i].append(j)
    graph[j].append(i)

vivited = [0 for _ in range(N+1)]

ans = 0
for i in range(1, N+1):
    if vivited[i] == 0:
        ans+=1
        bfs(i)
        # print(vivited)

print(ans)


