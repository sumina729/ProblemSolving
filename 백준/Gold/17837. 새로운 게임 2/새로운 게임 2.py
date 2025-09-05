N, K = map(int, input().split())
c_pan = [list(map(int, input().split()))for _ in range(N)] # 0->흰 , 1->빨, 2 -> 파

m_pan = [[[]for _ in range(N)]for _ in range(N)]
m_list = []

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

re_d = [1, 0, 3, 2]

for i in range(K):
    y, x, d = map(int, input().split())

    m_pan[y-1][x-1].append(i)
    m_list.append([y-1, x-1, d-1])

# print(m_list)
# print()
# for m in m_pan:
#     print(m)



def get_move_list(my, mx, n):

    # print(my, mx, n, m_pan[my][mx])

    for i in range(0, len(m_pan[my][mx])):
        if m_pan[my][mx][i] == n:
            split_i = i
            # print(split_i)
            break
    
    
    move_list = m_pan[my][mx][split_i:]
    m_pan[my][mx] = m_pan[my][mx][:split_i]

    return move_list
            
ans = 0      
while True:
    ans+=1 
    if ans > 1000:
        print(-1)
        exit()
    # print(ans, "턴 시작")
    for k in range(K):
        
        # print("================시작", k)
        cy = m_list[k][0]
        cx = m_list[k][1]
        cd = m_list[k][2]


        move_list = get_move_list(cy, cx, k)
        # print(move_list)

        ny = cy+dy[cd]
        nx = cx+dx[cd]

        # print(ny, nx, cd)


        #일차확인 처음에 이거버면 방향 바꾸기
        if not (-1 < ny < N and  -1< nx < N):
            # print("범위넘어감 방향 바꿈")
            cd = re_d[cd]

            ny = cy+dy[cd]
            nx = cx+dx[cd]

        elif c_pan[ny][nx] == 2:
            # print("파안색임 방향 바꿈")
            cd = re_d[cd] 

            ny = cy+dy[cd]
            nx = cx+dx[cd]

        # print(ny, nx, cd)
        #2차
        if not(-1 < ny < N and  -1< nx < N) or c_pan[ny][nx] == 2:
            # print("또 못움직임")
            m_pan[cy][cx] = m_pan[cy][cx]+move_list

            for ni in move_list:
                m_list[ni][0] = cy
                m_list[ni][1] = cx
            

        elif c_pan[ny][nx] == 0: # 흰색이면
            m_pan[ny][nx] = m_pan[ny][nx]+move_list

            for ni in move_list:
                m_list[ni][0] = ny
                m_list[ni][1] = nx

        elif  c_pan[ny][nx] == 1: 
            move_list.reverse()
            m_pan[ny][nx] = m_pan[ny][nx]+move_list

            for ni in move_list:
                m_list[ni][0] = ny
                m_list[ni][1] = nx

        m_list[k][2] = cd #방향 맞추기

            
        
        # print()
        # print(m_list)
        # for m in m_pan:
        #     print(m)
        
        for y in range(N):
            for x in range(N):
                if len(m_pan[y][x]) > 3:
                    print(ans)
                    exit()
    # break
            