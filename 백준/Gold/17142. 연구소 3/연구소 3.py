from collections import deque

N , M = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(N)]

# for p in pan:
#     print(p)


v_list = []
for y in range(N):
    for x in range(N):
        if pan[y][x] == 2:
            v_list.append([y, x])

# print("바이러스 리스트", v_list)


def bfs(av_list):
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    for y in range(N):
        for x in range(N):
            # print(y, x)
            if (y, x) in av_list: #활성 바이러스
                visited[y][x] = 0

            elif pan[y][x] == 1: #벽
                visited[y][x] = -2

            elif  pan[y][x] == 2:
                visited[y][x] = -3 # 비활성 바이러스
                
    que = deque()
    for av in av_list:
        que.append(av)


    dy = [1, -1, 0,0]
    dx = [0, 0, 1, -1]
    while que:
        cy, cx = que.popleft()
        # print(cy, cx)

        for i in range(4):
            ny = cy+dy[i]
            nx = cx+dx[i]

            if -1<ny<N and -1<nx<N and (visited[ny][nx] == -1 or visited[ny][nx] == -3): # 빈공간 이면
                que.append((ny, nx))
                visited[ny][nx] = visited[cy][cx]+1

    # print()
    # for v in visited:
    #     print(v)

    ans = 0
    for y in range(N):
        for x in range(N):
            if visited[y][x] == -1: #확산 끝까지 못함
                return -1
            
            if pan[y][x] == 0:
                ans = max(ans, visited[y][x])

    
    # ans = max(max(v) for v in  visited)
    # print(ans)
    return ans


def dfs(si, av_list):
    global M, v_visited, v_list, is_ans, ans

    if len(av_list) == M:
        a = bfs(av_list)
        if a > -1:
            is_ans = True
            ans = min(a, ans)
        # print("조합:", av_list, a)
        return

    for i in range(si, len(v_list)):
        vy, vx = v_list[i]

        av_list.add((vy, vx))
        dfs(i+1, av_list)
        av_list.remove((vy, vx))
    
    
#조합찾기
is_ans = False
ans = N*N*N
v_visited = [[0 for _ in range(N)] for _ in range(N)]

av_list = set()
dfs(0, av_list)
    

if is_ans:
    print(ans)
else:
    print(-1)



