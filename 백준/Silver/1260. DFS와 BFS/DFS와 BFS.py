n, m, s = map(int, input().split())
from collections import deque

list_n = [[0 for _ in range(n+1)] for _ in range(n+1)]
is_v = [1 for _ in range(n+1)]

for _ in range(m):

    t1, t2 = map(int, input().split())
    list_n[t1][t2] = 1
    list_n[t2][t1] = 1


def dfs(me):
    print(me, end=" ")
    is_v[me] = 0
    for i in range(1, n+1):
        if list_n[me][i] == 1 and is_v[i] == 1:
            dfs(i)


queue = deque()
def bfs(me):
    queue.append(me)

    is_v[me] = 0
    print(me, end=" ")

    
    while queue:
        tmp = queue.popleft()
        for i in range(1, n+1):
            if list_n[tmp][i] == 1 and is_v[i] == 1:
                is_v[i] = 0
                print(i, end=" ")
                queue.append(i)

                
        


dfs(s)
is_v = [1 for _ in range(n+1)]
print()
bfs(s)

    