N, M = map(int, input().split())

def dfs(edge, deep):
    global visited, graph

    if deep == 5:
        return True

    for cnct_edge in graph[edge]:
        if not visited[cnct_edge]:
            visited[cnct_edge] = True
            if dfs(cnct_edge, deep+1):
                return True
            visited[cnct_edge] = False

    return False


graph = [[] for _ in range(N)]

for _ in range(M):
    i, j = map(int, input().split())

    graph[i].append(j)
    graph[j].append(i)
    

# for g in graph:
#     print(g)


visited = [0 for _ in range(N)]

is_ok = 0
for i in range(N):
    visited[i] = 1
    if dfs(i, 1):
        is_ok = 1
        break
    visited[i] = 0

print(is_ok)
