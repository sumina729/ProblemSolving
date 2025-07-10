import sys
input = sys.stdin.readline

from collections import deque

def bfs():
    visited = [0 for _ in range(N+1)]
    oi = 0


    if not order[oi] == 1:
        return 0
    
    que = deque()
    que.append(1)
    visited[1] = 1


    
    while que:

        n = que.popleft()

        n_nodes = set()
        for nxt in graph[n]:
            if visited[nxt] == 0:
                n_nodes.add(nxt)

        
        # print(n_nodes)
        for _ in range(len(n_nodes)):
            oi+=1

            # print(oi, order[oi])
            if order[oi] in n_nodes:
                nxt = order[oi]
                que.append(nxt)
                visited[nxt] = 1
            else:
                return 0
        
    return 1
    


N = int(input())
graph = [[] for i in range(N+1)]

for _ in range(N-1):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

order = list(map(int, input().split()))

# for g in graph:
#     print(g)

print(bfs())