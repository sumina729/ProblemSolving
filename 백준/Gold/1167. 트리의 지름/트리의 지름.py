import sys
input = sys.stdin.readline

from collections import deque

V = int(input())

graph = [ [] for _ in range(V+1)]

for _ in range(V):
    g_list = deque(list(map(int, input().split())))
    v = g_list.popleft()
    while True:
        nv = g_list.popleft()
        if nv == -1:
            break

        nw = g_list.popleft()

        graph[v].append([nv, nw])

def dfs(n):
    global V
    visited = [-1 for _ in range(V+1)]

    que = deque()
    que.append(n)
    visited[n] = 0

    max_n = -1
    max_l = -1

    while que:
        cn = que.popleft()
        for nxt_n, nxt_w in graph[cn]:
            if visited[nxt_n] == -1:
                visited[nxt_n] = visited[cn]+nxt_w
                que.append(nxt_n)
            
                if visited[nxt_n] > max_l:
                    max_l = visited[nxt_n]
                    max_n = nxt_n
    # print(visited)
    # print(max_n, max_l)

    return max_n, max_l
    

max_n, _ = dfs(1)
_, max_l = dfs(max_n)

print(max_l)
