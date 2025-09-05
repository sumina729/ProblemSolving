from collections import deque

N = int(input())
pan = [list(map(int, input().split())) for _ in range(N)]

# print(pan)



s_y = 0
s_x = 0
s_n = 2

for y in range(N):
    for x in range(N):
        if pan[y][x] == 9:
            s_y = y
            s_x = x

            break


dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

def get_fish_l(s_y, s_x, s_n, ey, ex):
    global N, pan
    visited = [[-1 for _ in range(N)]for _ in range(N)]

    que = deque()
    que.append([s_y, s_x])
    visited[s_y][s_x] = 0

    while que:
        cy, cx = que.popleft()
        
        for i in range(4):
            ny = cy+dy[i]
            nx = cx+dx[i]

            # 범위내, 상어보다 "작거나 같은", 방문 안한
            if -1<ny<N and -1<nx<N and pan[ny][nx] <= s_n and visited[ny][nx] ==  -1:
                que.append([ny, nx])
                visited[ny][nx] = visited[cy][cx]+1
                if ny == ey and nx == ex:
                    return visited[ey][ex]
    
    # print("거리", visited[ey][ex])
    # for v in visited:
    #     print(v)
    
    return visited[ey][ex]
    
ans = 0
e_cnt = 0 
while True:  
    # print("=======지난시간", ans)
    # print("================시작: 현재 상어크기:", s_n)
    fish_list = [] # y, x, l
    for y in range(N):
        for x in range(N):
            if pan[y][x] == 9: #상어 무시
                continue

            if 0 < pan[y][x] < s_n: #존재 하는데 상어보다 작으면
                # print("상어보다 작은 물고기(y, x, n)", y, x, pan[y][x])
                l = get_fish_l(s_y, s_x, s_n, y, x)
                if l > -1:
                    fish_list.append([y, x, l])

    if len(fish_list) == 0:
        # print("먹을 물고기 없음!!")
        print(ans)
        break


    #정렬
    fish_list.sort(key= lambda a: (a[2], a[0], a[1]))
    # print("물고기 리스트", fish_list)

    #상어 이동후 초 추가
    y, x, l = fish_list[0]
    ans += l # 이동시간

    pan[s_y][s_x] = 0

    s_y = y
    s_x = x

    ## 물고기 먹기
    pan[s_y][s_x] = 9
    e_cnt+=1
    

    #자기 그기만큼 먹으면 커지기
    if e_cnt == s_n:
        s_n +=1
        e_cnt = 0
    


    # for p in pan:
    #     print(p)


