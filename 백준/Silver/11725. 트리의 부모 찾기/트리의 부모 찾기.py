from collections import deque

V = int(input())

graph = [[]for _ in range(V+1)]


for _ in range(V-1):
    i, j = map(int, input().split())

    graph[i].append(j)
    graph[j].append(i)

ans = [ -1 for _ in range(V+1)]

que = deque()
que.append(1)
ans[1] = 0

while que:
    n = que.popleft()

    for nxt in graph[n]:
        if ans[nxt] == -1:
            ans[nxt] = n
            que.append(nxt)


for i in ans[2:V+1]:
    print(i)