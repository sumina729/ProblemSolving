'''

1. 주사위 이동 방향
- 주사위가 이동 방향으로 한 칸 굴러간다. 만약, 이동 방향에 칸이 없다면, 이동 방향을 반대로 한 다음 한 칸 굴러간다.
- 주사위가 도착한 칸 (x, y)에 대한 점수를 획득한다.

- 주사위의 아랫면에 있는 정수 A와 주사위가 있는 칸 (x, y)에 있는 정수 B를 비교해 이동 방향을 결정한다.
    - A > B인 경우 이동 방향을 90도 시계 방향으로 회전시킨다.
    - A < B인 경우 이동 방향을 90도 반시계 방향으로 회전시킨다.
    - A = B인 경우 이동 방향에 변화는 없다.



2. 점수체크(bfs)
 - (x, y)에 있는 정수를 B라고 했을때, (x, y)에서 동서남북 방향으로 연속해서 이동할 수 있는 칸의 수 C를 모두 구한다. 
 - 이때 이동할 수 있는 칸에는 모두 정수 B가 있어야 한다. 여기서 점수는 B와 C를 곱한 값이다.
 - 즉, 그 숫자가 연속으로 놓여있는 칸의 갯수 * 그 수
    - 2가 연속으로 4카 있으면 2*4

함수 1. 현재 주사위 전개도 변화, 주어진 방향으로 이동할때 주사위 전개도가 어떻게 바뀌는지 변화해주기, 리턴 A
[-, 북, -]
[서, 하, 동]
[-, 남, -]
[-, 상, -]

함수 2. bfs 를 활용해 점수 체크


'''

import copy
from collections import deque

def moovCube(d):
    global cube

    tmp = [[0, 0, 0] for _ in range(4)]
    if d == 0: #동
        tmp[0][1] = cube[0][1]
        tmp[1][0] = cube[1][1]
        tmp[1][1] = cube[1][2]
        tmp[1][2] = cube[3][1]
        tmp[2][1] = cube[2][1]
        tmp[3][1] = cube[1][0]

    if d == 1: #남
        tmp[0][1] = cube[1][1]
        tmp[1][0] = cube[1][0]
        tmp[1][1] = cube[2][1]
        tmp[1][2] = cube[1][2]
        tmp[2][1] = cube[3][1]
        tmp[3][1] = cube[0][1]

    if d == 2: #서
        tmp[0][1] = cube[0][1]
        tmp[1][0] = cube[3][1]
        tmp[1][1] = cube[1][0]
        tmp[1][2] = cube[1][1]
        tmp[2][1] = cube[2][1]
        tmp[3][1] = cube[1][2]

    if d == 3: #북
        tmp[0][1] = cube[3][1]
        tmp[1][0] = cube[1][0]
        tmp[1][1] = cube[0][1]
        tmp[1][2] = cube[1][2]
        tmp[2][1] = cube[1][1]
        tmp[3][1] = cube[2][1]
    
    # print()
    # for i in range(4):
    #     print(tmp[i])

    cube = copy.deepcopy(tmp)
    return tmp[1][1] 


def bfs(x, y, B):
    global M, N

    visit = [[0 for _ in range(M)]for _ in range(N)]
    C = 0

    que = deque()
    que.append((x, y))
    visit[y][x] = 1
    C = C+1


    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if -1<nx<M and -1<ny<N and pan[ny][nx]==B and visit[ny][nx] == 0 :
                que.append((nx,ny))
                visit[ny][nx] = 1
                C = C+1
    
    # for y in range(N):
    #     print(visit[y])
    # print(x, y, B, C)
    return C*B


N, M, K = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(N)]

#+1 은 시계방향 , -1은 반시계방향
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

cube = [
    [0, 2, 0],
    [4, 6, 3],
    [0, 5, 0],
    [0, 1, 0]
]

d_i = 0 #동쪽부터 시작
cx, cy = 0, 0
ans = 0

for _ in range(K):

    if -1<cx+dx[d_i]<M and -1<cy+dy[d_i]<N: #이동 가능하면 그대로
        cx = cx+dx[d_i]
        cy = cy+dy[d_i]
    else: # 이동 불가능 하면 방향 반대로
        d_i = (d_i+2)%4
        cx = cx+dx[d_i]
        cy = cy+dy[d_i]
    
    A = moovCube(d_i) # 주사위 이동
    B = pan[cy][cx]
    jumsu = bfs(cx, cy, B)

    ans += jumsu

    if A > B:
        d_i = (d_i+1)%4
    elif A < B:
        d_i = (d_i-1)%4
    
    
print(ans)