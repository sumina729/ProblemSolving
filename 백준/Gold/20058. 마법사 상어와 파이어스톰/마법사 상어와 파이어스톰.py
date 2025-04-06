'''
- 크기가 2^N × 2^N인 격자
- A[r][c]는 (r, c) (y, x) -> 얼음의 양
    -A[r][c]가 0인 경우 얼음이 없는 것

- 단계 L
    - 파이어스톰은 먼저 격자를 2L × 2L 크기의 부분 격자로 나눈다
    - 그 후, 모든 부분 격자를 '시계 방향'으로 90도 회전시킨다.

    - 이후 얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않은 칸은 얼음의 양이 1 줄어든다.
        - (r-1, c), (r+1, c), (r, c-1), (r, c+1)  여기서 얼름이 2개 이하 이면 얼음 줄어듬. 동시다발적으로 겠찌.
        - (r, c)와 인접한 칸은 (r-1, c), (r+1, c), (r, c-1), (r, c+1)이다.

결과1, 남아있는 얼음 A[r][c]의 합
결과2 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수 bfs

함수1. 얼음 돌리는 함수 (r)
함수2. 얼음 줄어들게 하는 함수
함수3 가장큰 엄을 덩어리 구하는 함수
'''

from collections import deque

def rotate90(sx, sy, l, tmp_pan):
    global  pan
    # tmp_pan = [pan[i][:] for i in range(N)] #독집적으로 복사


    for x in range(l):# 0~2
        for y in range(l):#0~2
            tmp_pan[sy+x][sx+(l-y-1)] = pan[sy+y][sx+x]

    # pan = [tmp_pan[i][:] for i in range(N)]  # 독집적으로 복사



def rotateAll(l):
    l = 2**l
    tmp_pan = [[0 for _ in range(N)] for _ in range(N)]

    for x in range(0, N, l):
        for y in range(0, N, l):
            sx = x
            sy = y
            # print(sx, sy)
            rotate90(x, y, l, tmp_pan)
    return tmp_pan

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def melt():
    global pan
    # tmp_pan = [pan[i][:] for i in range(N)]  # 독집적으로 복사
    tmp_pan = [[0 for _ in range(N)] for _ in range(N)]

    for y in range(N):
        for x in range(N):
            if pan[y][x] > 0:
                cnt = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if -1 < nx < N and -1 < ny < N and pan[ny][nx] > 0:
                        cnt +=1

                if cnt < 3:
                    # print(x, y)
                    tmp_pan[y][x] = pan[y][x] -1
                else:
                    tmp_pan[y][x] = pan[y][x]

    return tmp_pan


def bfs(x, y):
    global visit
    n = 0

    que = deque()
    que.append((x, y))
    visit[y][x] = 1
    n+=1

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]


            if -1 <nx< N and -1 < ny < N and pan[ny][nx] > 0 and visit[ny][nx] == 0: # 엄음이면서 방문 안했으면
                # print(x, y, nx, ny)
                que.append((nx, ny))
                visit[ny][nx] = 1
                n+=1

    return n


N, Q = map(int, input().split())
N = 2**N

pan = [list(map(int, input().split())) for _ in range(N)]
L = list(map(int, input().split()))


# print("N:", N)

for l in L:
    # for y in range(N):
    #     print(pan[y])


    pan = rotateAll(l)
    # print("==> 회전")
    # for y in range(N):
    #     print(pan[y])

    pan = melt() # 얼음 녹이기
    # print("==> 얼음녹이기")
    # for y in range(N):
    #     print(pan[y])


visit = [[0 for _ in range(N)] for _ in range(N)]

max_n = 0
sum = 0
for y in range(N):
   for x in range(N):
       sum += pan[y][x]
       if pan[y][x] > 0 and visit[y][x] == 0: #얼음이면서, 방문 안했으면
           n = bfs(x, y)
           # print(n)
           max_n = max(max_n, n)
           # print("===> ", x, y, n)
           # for i in range(N):
           #     print(visit[i])

print(sum)
print(max_n)

