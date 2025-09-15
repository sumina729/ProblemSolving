from collections import deque

N, M = map(int, input().split()) 
pan = [ list(map(int, input().split()) ) for _ in range(N)]

# print(pan)



def go_v(b_list):
    global N, M 
    dy = [-1, 1, 0 , 0]
    dx = [0, 0, -1, 1]

    que = deque()

    visited = [ [ 0 for _ in range(M)]for _ in range(N)]
    for y in range(N):
        for x in range(M):
                if pan[y][x] == 2:
                    que.append((y, x))
                    visited[y][x] = 1
                elif (y, x) in b_list:
                    visited[y][x] = 1
    
    # print()
    # for v in visited:
    #     print(v)
    while que:
        cy, cx = que.popleft()

        for i in range(4):
            ny = cy+dy[i]
            nx = cx+dx[i]

            if -1<ny<N and -1<nx<M and pan[ny][nx] == 0 and visited[ny][nx] == 0:
                que.append((ny, nx))
                visited[ny][nx] = 1
    # print("==")
    # for v in visited:
    #     print(v)

    remain_n = sum(visited[i].count(0) for i in range(N)) - sum(pan[i].count(1) for i in range(N))
    # print(ans)
    return remain_n


ans = 0
def dfs(s):
    global N, M, b_list, L, list_0, ans

    if len(b_list) == 3:
        
        
    
        ans = max(go_v(b_list), ans)
        # print("3개 조합완료", b_list, ans)
        # exit()
        return
    
    for i in range(s, L):
        # print(i)
        y, x = list_0[i]

        if pan[y][x] == 0:
            b_list.add((y, x))

            dfs(i+1)

            b_list.remove((y, x))
    

b_list = set()
list_0 = []

for y in range(N):
    for x in range(M):
        if pan[y][x] == 0:
            list_0.append((y, x))
L = len(list_0)

# print(L)
dfs(0)


print(ans)
