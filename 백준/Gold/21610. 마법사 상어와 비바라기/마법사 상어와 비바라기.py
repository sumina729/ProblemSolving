import copy

def moovCupA(d, s):
    global current_c
    tmp_list = []
    for cx, cy in current_c:
        nx = (cx+(dx[d]*s))%N 
        ny = (cy+(dy[d]*s))%N 

        # print(cx, cy, nx, ny)
        A[ny][nx] = A[ny][nx]+1
        tmp_list.append((nx, ny))

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
    tmp_list = []
    for y in range(N):
        for x in range(N):
            if A[y][x] >=2 :
                if not (x, y) in current_c:
                    tmp_list.append((x, y))
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

current_c = []
current_c.append((0, N-1))
current_c.append((1, N-1))
current_c.append((0, N-2))
current_c.append((1, N-2))


for i in range(M):
    moovCupA(d[i], s[i])
    for x, y in current_c:
        upA(x, y)
    newC()

  
print(sum(sum(A[i]) for i in range(N)))