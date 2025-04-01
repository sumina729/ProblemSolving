'''
- 왼쪽 윗 칸은 (1, 1)이고, 가장 오른쪽 아랫 칸은 (N, N)
- 1번 행과 N번 행을 연결했고, 1번 열과 N번 열도 연결했다.
- 비바라기를 시전하면 (N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름
- 구름에 이동을 M번 명령하려고 한다. i번째 이동 명령은 방향 di과 거리 si로 이루어져 있다.
- 방향은 총 8개의 방향이 있으며, 8개의 정수로 표현한다. 1부터 순서대로 ←, ↖, ↑, ↗, →, ↘, ↓, ↙ 이다.

마법 시전
1. 모든 구름이 di 방향으로 si칸 이동한다.
2. 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
3. 구름이 모두 사라진다.
4. 2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다. 물복사버그 마법을 사용하면, 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c)에 있는 바구니의 물이 양이 증가한다.
    - 이때는 이동과 다르게 경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아니다.
    - 예를 들어, (N, 2)에서 인접한 대각선 칸은 (N-1, 1), (N-1, 3)이고, (N, N)에서 인접한 대각선 칸은 (N-1, N-1)뿐이다.
7. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 
    - 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.


함수1. 구름 이동 후 물 증가 하는 함수 (필요한거: 현재 구름들(2중 배열), 방향, 전진 수, m 수) - 하나 만들어서 함수 돌리기
함수2. 대각선 있는 수 만큼 증가 시키는 함수 - 하나 만들어서 함수 돌리기
함수3. 새로운 구름 생성 (물의 양이 2 이상 이고, 현재 구름들이 0인 곳에 구름 생성)


'''

import copy

def moovCupA(d, s):
    global current_c
    tmp_list = set()
    for cx, cy in current_c:
        nx = (cx+(dx[d]*s))%N 
        ny = (cy+(dy[d]*s))%N 

        # print(cx, cy, nx, ny)
        A[ny][nx] = A[ny][nx]+1
        tmp_list.add((nx, ny))

    current_c = copy.deepcopy(tmp_list) 

def upA(x, y):
    for i in range(1, 8, 2):
        nx = x+dx[i]
        ny = y+dy[i]

        if -1<nx<N and -1<ny<N and A[ny][nx] > 0:
            # print(x, y, "->", nx, ny)
            A[y][x] = A[y][x]+1

def newC():
    global current_c
    tmp_list = set()
    for y in range(N):
        for x in range(N):
            if A[y][x] >=2 :
                if not (x, y) in current_c:
                    tmp_list.add((x, y))
                    A[y][x] = A[y][x]-2
    
    current_c = copy.deepcopy(tmp_list) 



N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
d, s = [], []
for i in range(M):
   td, ts= map(int, input().split())
   d.append(td-1)
   s.append(ts)

dx, dy = [-1,-1, 0, 1, 1, 1, 0, -1], [0, -1, -1, -1, 0, 1, 1, 1]

current_c = set()
current_c.add((0, N-1))
current_c.add((1, N-1))
current_c.add((0, N-2))
current_c.add((1, N-2))


for i in range(M):
    moovCupA(d[i], s[i])
    for x, y in current_c:
        upA(x, y)
    newC()

  
print(sum(sum(A[i]) for i in range(N)))