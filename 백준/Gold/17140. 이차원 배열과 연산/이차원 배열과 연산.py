r, c, k = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(3)]

r = r-1
c = c-1


def comput(pan_unit):
    r_dic = dict()

    #갯수새기
    for u in pan_unit: 
        if u == 0: # 0인거 계산 x
            continue
        elif u not in r_dic:
            r_dic[u] = 1
        else:
            r_dic[u]+=1

    
    #리스트호 하기
    r_list = []
    for rk in r_dic.keys():
        r_list.append([rk, r_dic[rk]])
    

    #솔팅하기
    r_list.sort(key=lambda a: (a[1], a[0]))
    
    #최종 형태
    r_unit = []
    for rl in r_list:
        r_unit +=rl
    
    if len(r_unit)>100:
        r_unit = r_unit[len(r_unit)-100:len(r_unit)]
    return r_unit


def get_pan(pan, N, M):
    t_pan = [[0 for _ in range(N)] for _ in range(M)]

    for y in range(N):
        for x in range(M):
            t_pan[x][y] = pan[y][x]
    
    return t_pan
            

cnt = 0
while True:

    N = len(pan)
    M = len(pan[0])
        
    if -1<r<N and -1<c<M and pan[r][c] == k:
        print(cnt)
        break
    

    is_r = False

    if N < M:
        pan = get_pan(pan, N, M)
        is_r = True

        N = len(pan)
        M = len(pan[0])
    
        # for p in pan:
        #     print(p)
    
    #연산
    max_l = 0
    for i in range(N):

        r_unit = comput(pan[i])
        pan[i] = r_unit

        max_l = max(max_l, len(r_unit))

    for i in range(N):
        pan[i] += [0]*(max_l-len(pan[i]))


    if is_r:
        N = len(pan)
        M = len(pan[0])

        pan = get_pan(pan, N, M)
    # for p in pan:
    #     print(p)

    cnt+=1
    if cnt > 100:
        print(-1)
        break