'''
블록은 검은색 블록, 무지개 블록, 일반 블록이 있다.
    -  일반 블록은 M가지 색상이 있고,
        - 색은 M이하의 자연수로 표현한다. 검
    - 검은색 블록은 -1, 무지개 블록은 0으로 표현한다.

(i, j)는 격자의 i번 행, j번 열을 의미하고, 인접한 칸 위, 아래, 오, 왼

블록 그룹
- 일반 블록이 적어도 하나(1개 이상)
    - 일반 블록의 색은 모두 같아야 함
- 검은색 블록은 포함되면 안 되고, 무지개 블록은 얼마나 들어있든 상관없다.

- 그룹의 속한 블록의 개수는 2개 이상
- 기준블록: 무지개 블록이 아닌 블록 중에서 행의 번호가 가장 작은 블록, 그러한 블록이 여러개면 열의 번호가 가장 작은 블록 y작은순, x 작은순


오토게임시작
1. 크기가 가장 큰 블록 그룹을 찾는다.
    - 그러한 블록 그룹이 여러 개라면 포함된 무지개 블록의 수가 가장 많은 블록 그룹
    - 그러한 블록도 여러개라면 기준 블록의 행이 가장 큰 것을,
    - 그 것도 여러개이면 열이 가장 큰 것을 찾는다.

2. 1에서 찾은 블록 그룹의 모든 블록을 제거한다.
    - 블록 그룹에 포함된 블록의 수를 B라고 했을 때, B^2점을 획득한다.
3. 격자에 중력이 작용한다.
4. 격자가 90도 반시계 방향으로 회전한다.
5. 다시 격자에 중력이 작용한다.

중력작용
검은색 블록을 제외한 모든 블록이 행의 번호가 큰 칸으로 이동한다. 이동은 다른 블록이나 격자의 경계를 만나기 전까지 계속

1. 가장큰 블록 찾는 함수 (bfs)
2. 중력작용 함수
3. 반시계방향 회전 함수

1 ≤ N ≤ 20
1 ≤ M ≤ 5

'''
import copy
from collections import deque

def bfs(x, y, m, r):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    cnt = 0
    star_cnt = 0

    due = deque()
    due.append((x, y))
    visited[y][x] = 1
    if r:
        pan[y][x] = -2
    else:
        cnt+=1

    while due:
        x, y = due.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1<nx<N and -1<ny<N and visited[ny][nx] == 0 and (pan[ny][nx] == m or pan[ny][nx] == 0):
                visited[ny][nx] = 1
                due.append((nx, ny))
                if r:
                    pan[ny][nx] = -2
                else:
                    cnt += 1
                    if pan[ny][nx] == 0:
                        star_cnt+=1

    start_x = -1
    start_y = -1

    if cnt >1:
        end = 0
        for y in range(N):
            for x in range(N):
                if visited[y][x] == 1 and not pan[y][x] == 0:
                    start_x = x
                    start_y = y
                    end = 1
                    break
            if end:
                break

    return cnt, star_cnt, start_x, start_y

def remove_pan():
    # 1. 가장 큰 블럭 찾기
    is_end = 1
    mx, my, mc, ms, sx, sy = 0, 0, 0, -1, -1, -1
    for y in range(N):
        for x in range(N):
            if pan[y][x] > 0: #색깔있는 블럭이면
                c, s, tx, ty = bfs(x, y, pan[y][x], 0)
                if c > 1: #블럭은 2보다 커야함
                    # print(x, y)
                    is_end = 0
                    if mc < c:
                        mc = c
                        ms = s
                        sy = ty
                        sx = tx
                        mx, my = x, y
                    elif mc == c and ms < s:
                        mc = c
                        ms = s
                        sy = ty
                        sx = tx
                        mx, my = x, y
                    elif mc == c and ms == s and sy < ty:
                        mc = c
                        ms = s
                        sy = ty
                        sx = tx
                        mx, my = x, y
                    elif mc == c and ms == s and sy == ty and sx < tx:
                        mc = c
                        ms = s
                        sy = ty
                        sx = tx
                        mx, my = x, y

    # 2. 가장 큰 블럭 지우기
    if is_end:
        return 0
    bfs(mx, my, pan[my][mx], 1)

    return mc*mc


def moveDown(x): # 한줄에 대해서 중력 작용
    global N
    for y in range(N-1, -1, -1):#20
        if pan[y][x] > -1: # 검은 색이 아니면 중력
            ny = y
            while True: #20
                ny = ny + 1
                if ny >= N or pan[ny][x]  > -2 or pan[ny][x] == N : # 검은블럭 이거나, 경계이면, 위치해 있으면
                    break

            if ny-1 != y:
                pan[ny-1][x] = pan[y][x]
                pan[y][x] = -2

def degre90():
    global pan
    tmp_pan = [[0 for _ in range(N)] for _ in range(N)]
    for y in range(N):
        for x in range(N):
            tmp_pan[y][x] = pan[x][N-1-y]

    pan = copy.deepcopy(tmp_pan)



N, M = map(int, input().split())
pan =  [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

ans = 0

#게임한판
while True:
    # 1. 가장 큰 블럭 지우기
    tmp_ans = remove_pan() #리턴이 0 이면 지울거 없읍
    if tmp_ans == 0:
        # print("지울 수 있는 블럭 없음")
        break
    else:
        ans+=tmp_ans

    # 2. 중력 작용
    for x in range(N): #20
        moveDown(x)

    # 3. 반식계 90도 회전
    degre90()

    # 4. 중력 작용
    for x in range(N): #20
        moveDown(x)

print(ans)
