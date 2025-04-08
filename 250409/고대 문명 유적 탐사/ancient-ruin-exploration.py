from collections import deque


'''
1. 탐사진행
- 중심 위치 9가지 y:1~3,x:1~3
    - 각 중심으로 부터 회전 (90, 180 270)
        - 회전후 유물 가치 계산 (함수 사용) bfs
            - 가치가 전보다 큰기 확인 n
            - 가치가 같으면 회선수 작은거 r
            - 회전수 같으면 x가 작은거 x
            - 회전수 같으면 y가 작은거 y
            => 만족하면 x, y, r, n 저장

- 저장된 x, y 의 r번 회전으로 배열 수정
'''

def rotate(sx, sy, tmp_pan):
    tmp = [[tmp_pan[y][x] for x in range(5)] for y in range(5)]

    for y in range(3):
        for x in range(3):
            tmp[sy+x][sx+(3-y-1)] = tmp_pan[sy+y][sx+x]

    # for y in tmp:
    #     print(y)

    return tmp

def bfs1(x, y, tmp_pan):
    global visited
    cnt = 0

    que =  deque()
    que.append((x, y))
    visited[y][x] = 1
    cnt+=1


    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if -1<nx<5 and -1<ny<5 and visited[ny][nx] == 0 and tmp_pan[ny][nx] == tmp_pan[y][x]:
                # print(nx, ny)
                visited[ny][nx] = 1
                que.append((nx, ny))
                cnt += 1

    return cnt

def serch(tmp_pan):
    global visited
    visited = [[0 for _ in range(5)] for _ in range(5)] #초기화

    ans = 0
    for y in range(5):
        for x in range(5):
            if visited[y][x] == 0:
                n = bfs1(x, y, tmp_pan)
                if n>2:
                    ans+=n
                # print(n)
                # for i in visited:
                #     print(i)
    return ans

def rotate_pan():
    max_p = [-1, -1, -1, 0] # x, y, r, n

    for y in range(1, 4): #1, 2, 3
        for x in range(1, 4):
            r = 0
            tmp_pan = [[pan[y][x] for x in range(5)] for y in range(5)]
            for i in range(3):
                r+=1
                # print("=>", x-1, y-1, r)
                tmp_pan = rotate(x-1, y-1, tmp_pan) #회전

                # print("회전", i)
                # for q in tmp_pan:
                #     print(q)

                # tmp_pan 에 대해서 가능한 유뮬 찾기
                n = serch(tmp_pan)

                if max_p[3] < n: max_p = [x, y, r, n]
                elif max_p[3] == n and max_p[2] > r: max_p = [x, y, r, n]
                elif max_p[3] == n and max_p[2] == r and max_p[0] > x: max_p = [x, y, r, n]
                elif max_p[3] == n and max_p[2] == r and max_p[0] == x and max_p[1] > y: max_p = [x, y, r, n]

    # print(max_p)
    return max_p[0], max_p[1], max_p[2], max_p[3]

def bfs2(x, y, tmp_pan):
    visited2 = [[0 for _ in range(5)] for _ in range(5)]

    que =  deque()
    que.append((x, y))
    visited2[y][x] = 1
    number = tmp_pan[y][x]
    tmp_pan[y][x] = 0


    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if -1<nx<5 and -1<ny<5 and visited2[ny][nx] == 0 and tmp_pan[ny][nx] == number:
                # print(nx, ny)
                visited[ny][nx] = 1
                tmp_pan[ny][nx] = 0
                que.append((nx, ny))

def remove_pan():
    global visited
    visited = [[0 for _ in range(5)] for _ in range(5)] #초기화

    ans = 0
    for y in range(5):
        for x in range(5):
            if visited[y][x] == 0:
                n = bfs1(x, y, pan) #유뮬인지 찾기
                if n>2: #유뮬이면
                    ans+=n
                    bfs2(x, y, pan) #진짜 지우기

    return ans

def add_pan():
    global m_list, m_cnt
    for x in range(5):
        for y in range(4, -1, -1):
            if pan[y][x] == 0:
                pan[y][x] = m_list[m_cnt]
                m_cnt+=1



dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

K, M = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(5)]
m_list = list(map(int, input().split()))
visited = [[0 for _ in range(5)] for _ in range(5)]
m_cnt = 0

# print("==> 1. 초기 입력 및 판")
#     print(K, M)
#     for y in range(5):
#         print(pan[y])
#     print(m_list)

for _  in range(K):
    ans = 0

    mx, my, mr, mn= rotate_pan() #만약에 0 이면 끝 찾을 유물 없음

    if mn == 0:
        # print("유물없을 즉시종료")
        # print(ans)
        break

    for _ in range(mr):  # 회전
        pan = rotate(mx - 1, my - 1, pan)

    ans += remove_pan() #3개이상인 유물 찾아서 지우기 0이면 지울서 없음
    # print("==> 1. 유물 찾아서 지우기", mx, my, mr)
    # for y in range(5):
    #     print(pan[y])

    add_pan()
    # print("==> 2. 유물 추가", mx, my, mr)
    # for y in range(5):
    #     print(pan[y])

    while True:
        n = remove_pan()
        if n == 0:
            break
        else:
            ans+=n
        add_pan()

    # print("1턴 끝나고 최종유물")
    # for y in range(5):
    #     print(pan[y])
    print(ans, end=" ")