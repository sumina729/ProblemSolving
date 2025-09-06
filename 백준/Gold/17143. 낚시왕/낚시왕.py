R, C, M = map(int, input().split())

pan = [[[]for _ in range(C)]for _ in range(R)]

for _ in range(M):

    r, c, s, d, z = map(int, input().split())
    pan[r-1][c-1] = [s, d-1, z] #속도, 방향, 크기

dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]

r_d = [1, 0, 3, 2]

# for p in pan:
#     print(p)



def get_shark(x):
    global R, C, M

    ans = 0
    for y in range(R):
        if len(pan[y][x]) > 0: # 1마리 있으면
            ans = pan[y][x][2] # 크기
            pan[y][x] = []

            # print("상어잡음(깊이, 크기)", y, ans)
            break
    
    return ans

def move_shark(y, x, s, d):

    global R, C, M


    if d in (0, 1):                  # 위/아래
        cycle = 2 * (R - 1) if R > 1 else 1
        steps = s % cycle
        for _ in range(steps):
            if y == 0 and d == 0:    # 맨 위에서 위로 가려면 튕겨서 아래로
                d = 1
            elif y == R-1 and d == 1: # 맨 아래에서 아래로 가려면 튕겨서 위로
                d = 0
            y += dy[d]
    else:                            # 좌/우
        cycle = 2 * (C - 1) if C > 1 else 1
        steps = s % cycle
        for _ in range(steps):
            if x == 0 and d == 3:    # 맨 왼쪽에서 왼쪽이면 → 오른쪽으로 튕김
                d = 2
            elif x == C-1 and d == 2: # 맨 오른쪽에서 오른쪽이면 → 왼쪽으로 튕김
                d = 3
            x += dx[d]
    
    return y, x, d

        
        

def move_sharks():
    global R, C, M

    move_pan = [[[]for _ in range(C)]for _ in range(R)]
    for y in range(R):
        for x in range(C):
            if len(pan[y][x]) > 0: # 1마리 있으면 이동
                    s, d, z = pan[y][x]
                    my, mx, md = move_shark(y, x,s, d)
                    # print(y, x, pan[y][x][1],'상어의 이동위치(my, mx, md)', my, mx, md)
                    move_pan[my][mx].append([s,md,z])
                    # break
    
    for y in range(R):
        for x in range(C):
            if len(move_pan[y][x]) > 0: # 1마리 이상 있으면
                move_pan[y][x].sort(key=lambda a:(-a[2])) #z가 큰순
                move_pan[y][x]= move_pan[y][x][0]


    
    return move_pan

ans = 0
for p in range(C):
    # print()
    # print("=================이동======", p)
    #p열 에서 가장 위에 있는 상서 찾기
    ans+= get_shark(p)

    # print(p,"위치에서 상어 잡은후 ")
    # for p in pan:
    #     print(p)

    #상어 이동
    pan = move_sharks()
    # print("이동 후 상어위치")
    # for p in pan:
    #     print(p)


    # break

print(ans)