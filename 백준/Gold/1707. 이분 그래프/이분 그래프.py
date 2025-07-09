from collections import deque

import sys
input = sys.stdin.readline

def dfs(n):

    global graph, visited

    que = deque()
    que.append(n)
    visited[n] = 1 #1, 2

    while que:
        n = que.popleft()

        if  visited[n] == 1:
            num = 2
        else:
            num = 1

        for nxt in graph[n]:
            if visited[nxt] == 0:
                que.append(nxt)
                visited[nxt] = num
            elif not visited[nxt] == num:
                return False
    return True

T = int(input())

for _ in range(T):
    V, E = map(int, input().split())
    graph = [[]for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]

    ans = 'YES'

    for _ in range(E):
        i, j = map(int, input().split())

        graph[i].append(j)
        graph[j].append(i)
    
    for i in range(1, V+1):
        if visited[i] == 0:
            if dfs(i) == False:
                ans = 'NO'
                break
    
    print(ans)
    
    