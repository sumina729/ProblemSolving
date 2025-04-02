'''
1. 모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다.
    - 이동하는 중에는 같은 칸에 여러 개의 파이어볼이 있을 수도 있다.
2. 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
    2-1 같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.
    2-2 파이어볼은 4개의 파이어볼로 나누어진다.
    2-3 나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다.
        - 질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋이다.
        - 속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋이다.
        - 합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.
        - 질량이 0인 파이어볼은 소멸되어 없어진다.
마법사 상어가 이동을 K번 명령한 후, 남아있는 파이어볼 질량의 합을 구해보자.

'''

N, M, K = map(int, input().split())
bolls = [] # y, x, m, s, d, _ -> 0, 1, 2, 3, 4
for i in range(M):
    y, x, m, s, d = map(int, input().split())
    bolls.append((y-1, x-1, m, s, d))

bool_map = [[[] for _ in range(N)]for _ in range(N)]


dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
 

for _ in range(K):
    # 이동
    while bolls:
       y, x, m, s, d =  bolls.pop()
    
       y = (y+(dy[d]*s))%N
       x = (x+(dx[d]*s))%N

       bool_map[y][x].append([m, s, d])
    
    # 계산
    for y in range(N):
        for x in range(N):
            cnt = len(bool_map[y][x]) 
            if cnt > 1: # 2개 이상이면

                sum_m = 0
                sum_s = 0
                sum_odd = 0
                sum_even = 0
                s4 = 1
                
                while bool_map[y][x]:
                    m, s, d = bool_map[y][x].pop()
                    sum_m += m
                    sum_s += s

                    if d%2 == 0:
                        sum_even+=1
                    else:
                        sum_odd+=1
                
                if sum_even == cnt or sum_odd == cnt:
                    s4 = 0
                
                if sum_m//5> 0:
                    for i in range(s4, 8, 2):
                        bolls.append((y, x, sum_m//5, sum_s//cnt, i)) #나뉠준비 아직 이동은 x, 공 생긴거지
                
            elif cnt == 1: # 1개
                m, s, d = bool_map[y][x].pop()
                bolls.append((y, x, m, s, d))


ans = 0
while bolls:
    y, x, m, s, d =  bolls.pop()
    ans+=m 

print(ans)
