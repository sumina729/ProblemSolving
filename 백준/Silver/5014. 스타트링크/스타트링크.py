from collections import deque

F, S, G, U, D =  map(int, input().split())

gragh = [-1 for _ in range(F+1) ]

def bfs(v):
    que = deque()
    que.append(v)
    gragh[v] = 0

    while que:
        v = que.popleft()
        if v == G:
            break
        
        if 0 < v+U < F+1 and gragh[v+U] == -1:
            gragh[v+U] = gragh[v]+1
            que.append(v+U) 

        if 0 < v-D < F+1 and gragh[v-D] == -1:
            gragh[v-D] = gragh[v]+1
            que.append(v-D)

bfs(S)
if gragh[G] == -1:
    print("use the stairs")
else:
    print(gragh[G])