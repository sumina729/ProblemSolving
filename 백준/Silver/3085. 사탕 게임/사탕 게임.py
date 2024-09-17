import sys
input = sys.stdin.readline

N = int(input())
pan = [list(input().strip()) for _ in range(N)]


def max_len(x, y):
    global N
    cnt_x, cnt_y = 0, 0
    max_x, max_y = 0, 0
    tmp_x, tmp_y = pan[y][0], pan[0][x]
    for i in range(0, N):

        if tmp_x == pan[y][i]:
            cnt_x+=1
        else:
            cnt_x = 1
        max_x = max(max_x, cnt_x)
        
        if tmp_y == pan[i][x]:
            cnt_y+=1
        else:
            cnt_y = 1
        max_y = max(max_y, cnt_y)

        tmp_x = pan[y][i]
        tmp_y = pan[i][x]
    
    return(max(max_x, max_y))
  

resert = 0
for y in range(N):
    for x in range(N):
        resert = max(max_len(x, y), resert)
        dx, dy = [1,0], [0,1]
        for i in range(2):
            nx, ny = dx[i] + x, dy[i] + y
            tmp = pan[y][x]

            if 0 <= nx < N and 0 <= ny < N:
                pan[y][x] = pan[ny][nx]
                pan[ny][nx] = tmp

                #바뀐거 체크
                resert = max(max_len(x, y), resert)
                resert = max(max_len(nx, ny), resert)

                pan[ny][nx] = pan[y][x]
                pan[y][x] = tmp
        
print(resert)