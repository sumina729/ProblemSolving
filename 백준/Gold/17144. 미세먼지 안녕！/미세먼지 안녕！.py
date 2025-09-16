

N, M, T = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(N)]
clener = [] #0번위 위쪽, 1번이 아래쪽

# for p in pan:
#     print(p)

for y in range(N):
    if pan[y][0] == -1:
        clener.append((y, 0))


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def spread_mungi():
    global N, M
    mungi_list =  []
    for y in range(N):
        for x in range(M):
            if pan[y][x] > 0:
                mungi_list.append((y, x, pan[y][x])) #초기 먼지 양도 같이


    # print("초기 먼지들:", mungi_list)

    for y, x, c in mungi_list:
        # print(y, x)
        n = c//5

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if -1<ny<N and -1<nx<M and not pan[ny][nx] == -1: #공기 청정기
                pan[ny][nx]+=n 
                pan[y][x]-=n 

    # print("먼지들 이동후")
    # for p in pan:
    #     print(p)

def start_clener(sysx, d_list, b_sysx):
    global N, M

    
    sy = sysx[0]
    sx = sysx[1]

    di = 0

    while True:

        if (sy, sx) in b_sysx:
            # print("방향전환", b_sysx)
            di+=1 #방향전환
        
        ny = sy+dy[d_list[di]]
        nx = sx+dx[d_list[di]]

        # print(ny, nx)

        if ny == sysx[0] and nx == sysx[1]: #다시 제자리로 돌아오면 종료
            pan[sy][sx] = 0
            break 
        
        if not(sy == sysx[0] and sx == sysx[1]):
            pan[sy][sx] = pan[ny][nx]
        sy = ny
        sx = nx

    # print("공기 청전기 가동후")
    # for p in pan:
    #     print(p)
    
    
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
for _ in range(T):
    # 먼지 확산
    spread_mungi()

    # 공기 청전기 가동
    start_clener(clener[0],[1, 2, 0, 3], [(0, 0), (0, M-1), (clener[0][0],M-1)]) #상 ->우 -> 하 -> 좌
    start_clener(clener[1],[0, 2, 1, 3], [(N-1, 0), (N-1, M-1), (clener[1][0],M-1)]) #하 ->우 ->상 -> 좌


    # break

print(sum(sum(pan[i]) for i in range(N)) + 2)