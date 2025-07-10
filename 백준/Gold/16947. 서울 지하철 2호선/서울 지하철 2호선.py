import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)


def dfs(n):
    global visited, graph

    for nxt in graph[n]:
        if visited[nxt] == 0:
            visited[nxt] = visited[n]+1
            dfs(nxt)

def get_cn(n):

    global visited, graph
    for nxt in graph[n]:
        if visited[n]+1 < visited[nxt]:
            return nxt
        
    return 0

def dfs2(n):
    global visited, graph, ans

    for nxt in graph[n]:
        if ans[nxt] == -1:
            if visited[n]+1 == visited[nxt]:
                ans[nxt] = ans[n]+1
                dfs2(nxt)
            elif visited[n]-1 == visited[nxt]:
                ans[nxt] = 0
                dfs2(nxt)

N = int(input())

graph = [[]for _ in range(N+1)]

for _ in range(N):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)


visited = [ 0 for _ in range(N+1)]
visited[1] = 1
dfs(1)

sn, en = 0, 0
for i in range(1, N+1):
    cn = get_cn(i)
    if cn > 0:
        visited = [ 0 for _ in range(N+1)]
        visited[i] = 1
        dfs(i)
        break

ans = [ -1 for _ in range(N+1)]
ans[cn] = 0
dfs2(cn)

print(*ans[1:])


