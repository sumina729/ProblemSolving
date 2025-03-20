from collections import deque

N = int(input())
g_n = int(input())
graph = [[0 for _ in range(N+1) ] for _ in range(N+1)]
visit = [1 for _ in range(N+1) ]

for i in range(g_n):
    v1, v2 = map(int, input().split())
    graph[v1][v2] =  graph[v2][v1] = 1

def bfs(v):
    due = deque()
    due.append(v)
    visit[v] = 0
    
    ans = 0

    while due:
        v = due.popleft()
        # print(v, visit)

        

        for i in range(1, N+1):
            if graph[v][i] and visit[i] :
                #큐에 집어 넣을때 방문 했다고 체크
                due.append(i)
                visit[i] = 0
                ans+=1
    
    return ans

print(bfs(1))