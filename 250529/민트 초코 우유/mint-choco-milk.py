from collections import deque

def cnt_kind(s):
    return len(set(s))


def sort_depo(list):
    global kind_list, power_list, N

    sort_power_list = sorted(list, key=lambda xy: (
        cnt_kind(kind_list[xy[1]][xy[0]]), 
        -power_list[xy[1]][xy[0]], 
        xy[1], 
        xy[0]
    ))   

    return sort_power_list

# 그룹 찾기, 힘 계산하기, 대표찾기
def bfs(x, y):
    global visited, kind_list, power_list, N, dx, dy
    group = []

    kind = kind_list[y][x]
    max_p = power_list[y][x]
    min_y = y
    min_x = x
    
    que = deque()
    que.append((x, y))
    visited[y][x] = 1

    group.append((x, y))

    while que:
        x, y = que.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if -1<nx<N and -1<ny<N and visited[ny][nx] == 0 and kind == kind_list[ny][nx]:
                que.append((nx, ny))
                visited[ny][nx] = 1
                group.append((nx, ny))

                if (-power_list[ny][nx], ny, nx) < (-max_p, min_y, min_x) :
                    max_p = power_list[ny][nx]
                    min_y = ny
                    min_x = nx
    
    #대표자 신앙심
    power_list[min_y][min_x] += (len(group)-1)

    #대표자 제외 그룹원 신앙심
    for x, y in group:
        if min_x==x and min_y==y:
            continue
        power_list[y][x] = max(0, power_list[y][x]-1)

    return min_x, min_y

def make_kind(kind1, kind2):
    tmp = kind1+kind2
    if 'T' in tmp and 'C' in tmp and 'M' in tmp:
        return 'TCM'
    elif 'T' in tmp and 'C' in tmp:
        return 'TC'
    elif 'T' in tmp and 'M' in tmp:
        return 'TM'
    elif 'C' in tmp and 'M' in tmp:
        return 'CM'
    elif 'T' in tmp:
        return 'T'
    elif 'C' in tmp:
        return 'C'
    elif 'M' in tmp:
        return 'M'
    
def donggik(x, y):
    global visited, kind_list, power_list, N, dx, dy, save_list
    d = power_list[y][x]%4
    want_x = power_list[y][x]-1
    power_list[y][x] = 1
    donggik_kind = kind_list[y][x]

    while True:
        x = x+dx[d]
        y = y+dy[d]

        if not(-1< x<N) or not(-1< y<N):
            break
        
        if not donggik_kind == kind_list[y][x]:
            want_y = power_list[y][x]

            if want_x > want_y: # 강한전파성공
                kind_list[y][x] = donggik_kind
                want_x -= (want_y+1)
                power_list[y][x]+=1
                save_list.add((x, y))

                if want_x < 1:
                    break
            else: # 약한전파성공
                kind_list[y][x] = make_kind(kind_list[y][x], donggik_kind)
                power_list[y][x]+=want_x
                save_list.add((x, y))
                break # 갈절함 0 바로 멈춤
   
# 입력
N, T = map(int, input().split())
kind_list = [list(input()) for _ in range(N)]
power_list =[list(map(int, input().split())) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for _ in range(T):

    #모든 사람에게 에너지 추가
    for y in range(N):
        for x in range(N):
            power_list[y][x] +=1

    #그룹 별 대표 뽑기
    visited = [[0 for _ in range(N)] for _ in range(N)]
    depo = []
    for y in range(N):
        for x in range(N): 
            if visited[y][x] == 0:
                dpx, dpy = bfs(x, y)
                
    #공격 순서 정하기
    depo = sort_depo(depo)

    #공격 하기
    save_list = set()
    for x, y in depo:
        if not (x, y) in save_list:
            donggik(x, y)

    #분야별 에너지 총합
    sum_dic = {'TCM': 0, 'TC': 0, 'TM': 0, 'CM': 0, 'M': 0, 'C': 0, 'T': 0}
    for y in range(N):
        for x in range(N):
            sum_dic[kind_list[y][x]]+=power_list[y][x]

    #결과출력
    print(sum_dic['TCM'], sum_dic['TC'], sum_dic['TM'], sum_dic['CM'], sum_dic['M'], sum_dic['C'], sum_dic['T'])