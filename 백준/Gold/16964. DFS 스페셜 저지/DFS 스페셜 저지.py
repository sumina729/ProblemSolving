import sys
input = sys.stdin.readline

def dfs(n):
    global oi

    if not order[oi] == n:
        return 0

    n_nodes = set()
    for nxt in graph[n]:
        if visited[nxt] == 0:
            n_nodes.add(nxt)

    oi+=1
    for _ in range(len(n_nodes)):

        if order[oi] in n_nodes:
            nxt = order[oi]
            visited[nxt] = 1
            
            dfs(nxt)
        else:
            return 0

        

N = int(input())
graph = [[] for i in range(N+1)]

for _ in range(N-1):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

order = list(map(int, input().split()))

visited = [0 for _ in range(N+1)]
oi = 0
visited[1] = 1
dfs(1)
if oi == N:
    print(1)
else:
    print(0)