'''
n*n
T -> 민트
C -> 초코
M -> 우유

아침
- 모든 사람의 신앙심 +1

점심
- 인접한 신봉음식끼리 그룹
    - 대표자
        - 신앙심 튼사람
        -> y 가 가장 작은
        -> x 가 가장 작은
    - 대표자 (그룹원수 -1) 만큼 얻기
    - 대표자 뺸 그룹원원 각각 -1

저녁
전파순서
 1. (단일 -> 이중 -> 삼중)
 2. 안에서 신앙심 높은순
 3. y 작은순
 4. x 작은순

전파자
신앙심 = 1
간절감 = 신앙심 -1 (1 되기전)
이동방향 = 신앙심%4 (0,1, 2, 3 => 위, 아래 왼, 오)

종료조건
- 격가 밖으로 나가거나
- 간절함 a 0이 되면

한칸ㄱ씩히동
- 같으면 그냥 다름
- 다르면
    - y = 대상의 신앙심
    - x > y 
        - 전파대상 : 신봄음식변경
        - 전파차 x -(y+1)
            -   만양 0 이되면 종료
    - x. <= y
        - 전파대상 : 두 신앙심 합쳐지기
        - 전파대상 : +=x
        - 전파자 0 끝

추가조선
- 방어상태가 되면 전파 x
- 전파 당할수는 있음

'''

from collections import deque



def cnt_kind(s):
    if s == 'T' or  s == 'C' or  s == 'M':
        return 1
    elif s == 'TC' or  s == 'TM' or  s == 'CM':
        return 2
    elif s == 'TCM':
        return 3
    
    # print("===종유 이상함")

def sort_depo(list):
    global kind_list, power_list, N
    sort_power_list = []
    tmp = list[:]

    while tmp:
        x, y = tmp[0]
        min_k = cnt_kind(kind_list[y][x])
        max_p = power_list[y][x]
        min_y = y
        min_x = x

        for x, y in tmp:
            if min_k > cnt_kind(kind_list[y][x]):
                min_k = cnt_kind(kind_list[y][x])
                max_p = power_list[y][x]
                min_y = y
                min_x = x
            elif min_k == cnt_kind(kind_list[y][x]) and max_p < power_list[y][x]:
                min_k = cnt_kind(kind_list[y][x])
                max_p = power_list[y][x]
                min_y = y
                min_x = x
            elif min_k == cnt_kind(kind_list[y][x]) and max_p == power_list[y][x] and min_y > y:
                min_k = cnt_kind(kind_list[y][x])
                max_p = power_list[y][x]
                min_y = y
                min_x = x
            elif min_k == cnt_kind(kind_list[y][x]) and max_p == power_list[y][x] and min_y == y and min_x > x:
                min_k = cnt_kind(kind_list[y][x])
                max_p = power_list[y][x]
                min_y = y
                min_x = x
            
        # print(min_k, max_p, min_y, min_x, kind_list[min_y][min_x])
        


        sort_power_list.append((min_x, min_y))
        tmp.remove((min_x, min_y))    

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

                if max_p < power_list[ny][nx]:
                    max_p = power_list[ny][nx]
                    min_y = ny
                    min_x = nx
                elif max_p == power_list[ny][nx] and min_y > ny:
                    max_p = power_list[ny][nx]
                    min_y = ny
                    min_x = nx
                elif max_p == power_list[ny][nx] and min_y == ny and min_x > nx:
                    max_p = power_list[ny][nx]
                    min_y = ny
                    min_x = nx
    
    # print()
    # print("그룹 찾기, 대표찾기")
    # print(min_x, min_y, group, len(group))
    #대표자 신앙심
    power_list[min_y][min_x] += (len(group)-1)

    # if len(group) < 2:
    #     return -1, -1

    #대표자 제외 그룹원 신앙심
    for x, y in group:
        if min_x==x and min_y==y:
            continue
        power_list[y][x] = max(0, power_list[y][x]-1)
    # print("힘 계산하기")
    # print(power_list)


    return min_x, min_y


# elif kind_list[y][x] == 'TC' or  kind_list[y][x] == 'TM' or  kind_list[y][x] == 'CM':
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
    # print(donggik_kind)

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

# print("초기 입력")
# print(N, T)
# print(kind_list)
# print(power_list)



for _ in range(T):

    # 1. 아침
    for y in range(N):
        for x in range(N):
            power_list[y][x] +=1

    # print()
    # print("=====================아침===================")
    # print("전체 1씩 증가")
    # for y in range(N):
    #     print(*kind_list[y])
    # for y in range(N):
    #     print(*power_list[y])
    # print("===========================================")


    #2. 점심
    # print()
    # print("=====================점심===================")

    visited = [[0 for _ in range(N)] for _ in range(N)]
    depo = []
    for y in range(N):
        for x in range(N): 
            if visited[y][x] == 0:
                dpx, dpy = bfs(x, y)
                if dpx > -1:
                    depo.append((dpx, dpy))

    # print("최종 공격자 리스트와 힘")
    depo = sort_depo(depo)
    # print(depo)
    # for y in range(N):
    #     print(*kind_list[y])
    # for y in range(N):
    #     print(*power_list[y])
    # print("===========================================")

    save_list = set()

    # print("=====================저녁===================")
    for x, y in depo:
        if not (x, y) in save_list:
            donggik(x, y)
            # print(x, y, "공격")
            # for y in range(N):
            #     print(*kind_list[y])
            # for y in range(N):
            #     print(*power_list[y])


    sum_dic = {'TCM': 0, 'TC': 0, 'TM': 0, 'CM': 0, 'M': 0, 'C': 0, 'T': 0}
    for y in range(N):
        for x in range(N):
            sum_dic[kind_list[y][x]]+=power_list[y][x]

    # for y in range(N):
    #         print(*kind_list[y])
    # for y in range(N):
    #         print(*power_list[y])
    print(sum_dic['TCM'], sum_dic['TC'], sum_dic['TM'], sum_dic['CM'], sum_dic['M'], sum_dic['C'], sum_dic['T'])



    




