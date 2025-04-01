'''
4방향 청소 다 됐으면 (0이 없어면 , 즉 벽과 청소된거만 있으면 V  
    -> 뒤로이동
        -> 뒤가 벽이면 
            -> 끝
        -> 뒤가 벽이 아니면 
            -> 반복

4방향 청소 안됐으면 (하나도 0 이면) V
    -> 반시계 회전 (d+1) 
        -> 바라보는 앞칸 확인 V
            -> 앞칸 청소 안되어있으면
                -> 이면 전진(1) 후 반복
            -> 앞칸 청소 되어있으면
                -> 반복

벽 1, 청소x 0 , 청소한거 2

'''

#전체방향 확인
def isAllClean(x, y):
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if -1 < nx < M and -1 < ny < N and room[ny][nx] == 0: #청소 안되 있으면 
            return False
    
    return True

#앞 방향 확인
def isFrontClean(x, y, d): # 현재 방향 d

    nx, ny = x+dx[d], y+dy[d]
    if -1 < nx < M and -1 < ny < N and room[ny][nx] == 0: #청소 안되 있으면 
        return False # 
    
    return True

N, M = map(int, input().split())
y, x, d = map(int, input().split()) 
room = [list(map(int, input().split())) for _ in range(N)]

dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

ans = 0

while True:

    if room[y][x] == 0:
        room[y][x] = 2
        ans+=1

    if isAllClean(x, y): # 청소 다 됐으면
        # 후진, 방향틀기x
        x = x+dx[(d+2)%4]
        y = y+dy[(d+2)%4]
        
        if room[y][x] == 1: # 벽이면 끝
            break

    else: #청소 안된칸있으면
        d = (d-1)%4
        if not isFrontClean(x, y, d):
            x = x+dx[d]
            y = y+dy[d]
            
print(ans)