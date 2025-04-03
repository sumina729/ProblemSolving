'''
- (r, c)는 r행 c열 -> y x
- |r1 - r2| + |c1 - c2| = 1을 만족하는 두 칸이 (r1, c1)과 (r2, c2)를 인접 -> 오, 왼, 위, 아래 

1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
3. 2를 만족하는 칸도 여러 개인 경우에는 행(y가 작은)의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열(x가 작은거)의 번호가 가장 작은 칸으로 자리를 정한다.

'''

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

N = int(input())
M = N*N
S = [list(map(int, input().split())) for _ in range(M)]
room = [[0 for _ in range(N)]for _ in range(N)]

def likeFriend(n): #n번째 학생 자리 찾기
    cnu = [[[0, 0] for _ in range(N)]for _ in range(N)] # 각위치에 대해서 선호친구 인접수0, 빈자리수1
    for y in range(N): # 20 
        for x in range(N): #20 
            if room[y][x] == 0: # 비어 있는 자지이며
                for i in range(4): #4 방향확인
                    nx, ny = x+dx[i], y+dy[i]
                    if -1<nx<N and -1<ny<N: #유효
                        if room[ny][nx] == 0: #
                            cnu[y][x][1] +=1 # 비어있는칸
                        else:
                            for j in range(1, 5): #4
                                if room[ny][nx] ==  S[n][j]:
                                    cnu[y][x][0] +=1 # 선초하는 친구가 있는 칸
    
    f, b = -1, -1
    px, py = -1, -1
    for y in range(N): # 20
        for x in range(N): #20
            if room[y][x] == 0:
                if cnu[y][x][0] > f:
                    f, b = cnu[y][x][0], cnu[y][x][1]
                    px, py = x, y
                elif cnu[y][x][0] == f and cnu[y][x][1] > b:
                    f, b = cnu[y][x][0], cnu[y][x][1]
                    px, py = x, y

    room[py][px] = S[n][0] # 앉기

    # print("====")
    # for y in range(N):
    #     print(cnu[y])
    # for y in range(N):
    #     print(room[y])

                
def sum_s(n, x, y):

    like_s = 0
    sn = -1
    for i in range(M):
        if S[i][0]  == n:
            sn = i
            break

    for i in range(4): #4
        nx, ny = x+dx[i], y+dy[i]
        if -1<nx<N and -1<ny<N:
            for j in range(1, 5): #4
                if room[ny][nx] ==  S[sn][j]:
                    like_s +=1
    
    if like_s == 0: return 0
    if like_s == 1: return 1
    if like_s == 2: return 10
    if like_s == 3: return 100
    if like_s == 4: return 1000
    

for n in range(M): # 400
    likeFriend(n) # 20*20*4*4

ans = 0
for x in range(N): #20
    for y in range(N): #20
        ans += sum_s(room[y][x], x, y) #400
print(ans)