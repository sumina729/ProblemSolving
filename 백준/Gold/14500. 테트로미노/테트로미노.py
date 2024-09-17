import sys
input = sys.stdin.readline

N, M = map(int,input().split())
pan = [list(map(int, input().split()))for _ in range(N)]

tetromino = [
    [[0, 0, 0, 0], [0, 1, 2, 3]], 
    [[0, 0, 1, 1], [0, 1, 0, 1]], 
    [[0, 1, 2, 2], [0, 0, 0, 1]],
    [[0, 1, 1, 2], [0, 0, 1, 1]],
    [[0, 0, 0, 1], [0, 1, 2, 1]]

]

def tetromino1(x, y):
    max_num = 0
    if 0 <= y+max(tetromino[0][0]) < N and 0 <= x+max(tetromino[0][1]) < M :
        rect = [0, 0, 0, 0]
        for n in range(4):  
            rect[n] = pan[y+tetromino[0][0][n]][x+tetromino[0][1][n]]

        max_num = max(max_num, sum(rect))

    #세로
    if 0 <= y+max(tetromino[0][1])< N and 0 <= x+max(tetromino[0][0]) < M :
        rect = [0, 0, 0, 0]
        for n in range(4):  
            rect[n] = pan[y+tetromino[0][1][n]][x+tetromino[0][0][n]]
        
        max_num = max(max_num, sum(rect))
    return max_num

def tetromino2(x, y):
    max_num = 0
    if 0 <= y+max(tetromino[1][0]) < N and 0 <= x+max(tetromino[1][1]) < M :
        rect = [0, 0, 0, 0]
        for n in range(4):  
            rect[n] = pan[y+tetromino[1][0][n]][x+tetromino[1][1][n]]

        max_num = max(max_num, sum(rect))
    return max_num

def tetromino3(x, y):
    max_num = 0
    for i in range(2):
        for j in range(2):
            dx = 1
            dy = 1
            if i == 1 :
                dx = -1
            if j == 1 :
                dy = -1

            if 0 <= y+max(tetromino[2][0])*dy < N and 0 <= x+max(tetromino[2][1])*dx < M :
                rect = [0, 0, 0, 0]
                for n in range(4):  
                    rect[n] = pan[y+tetromino[2][0][n]*dy][x+tetromino[2][1][n]*dx]

                max_num = max(max_num, sum(rect))

            #세로
            if 0 <= y+max(tetromino[2][1])*dy < N and 0 <= x+max(tetromino[2][0])*dx < M :
                rect = [0, 0, 0, 0]
                for n in range(4):  
                    rect[n] = pan[y+tetromino[2][1][n]*dy][x+tetromino[2][0][n]*dx]
                
                max_num = max(max_num, sum(rect))
    
    return max_num


def tetromino4(x, y):
    max_num = 0
    for i in range(2):
        dx = 1
        if i == 1 :
            dx = -1

        if 0 <= y+max(tetromino[3][0]) < N and 0 <= x+max(tetromino[3][1])*dx < M :
            rect = [0, 0, 0, 0]
            for n in range(4):  
                rect[n] = pan[y+tetromino[3][0][n]][x+tetromino[3][1][n]*dx]

            max_num = max(max_num, sum(rect))

        #세로
        if 0 <= y+max(tetromino[3][1]) < N and 0 <= x+max(tetromino[3][0])*dx < M :
            rect = [0, 0, 0, 0]
            for n in range(4):  
                rect[n] = pan[y+tetromino[3][1][n]][x+tetromino[3][0][n]*dx]
            
            max_num = max(max_num, sum(rect))
    
    return max_num

def tetromino5(x, y):
    max_num = 0
    for i in range(2):
        for j in range(2):
            dx = 1
            dy = 1
            if i == 1 :
                dx = -1
            if j == 1 :
                dy = -1

            if 0 <= y+max(tetromino[4][0])*dy < N and 0 <= x+max(tetromino[4][1])*dx < M :
                rect = [0, 0, 0, 0]
                for n in range(4):  
                    rect[n] = pan[y+tetromino[4][0][n]*dy][x+tetromino[4][1][n]*dx]

                max_num = max(max_num, sum(rect))

            #세로
            if 0 <= y+max(tetromino[4][1])*dy < N and 0 <= x+max(tetromino[4][0])*dx < M :
                rect = [0, 0, 0, 0]
                for n in range(4):  
                    rect[n] = pan[y+tetromino[4][1][n]*dy][x+tetromino[4][0][n]*dx]
                
                max_num = max(max_num, sum(rect))
    
    return max_num


max_num = 0
for y in range(N):
    for x in range(M):
        max_num = max(max_num, tetromino1(x, y))
        max_num = max(max_num, tetromino2(x, y))
        max_num = max(max_num, tetromino3(x, y))
        max_num = max(max_num, tetromino4(x, y))
        max_num = max(max_num, tetromino5(x, y))

print(max_num)