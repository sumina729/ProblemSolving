'''
토데이도 이동
토네이도 계산
'''

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def cal(x, y, d):
    # print("======", x, y, d)

    global ans
    global pan

    moov =[
        [ #0 왼
            (1, 1, 0.01), (1, -1, 0.01),
            (0, 1, 0.07), (0, -1, 0.07),
            (-1, 1, 0.1), (-1, -1, 0.1),
            (0, 2, 0.02), (0, -2, 0.02),
            (-2, 0, 0.05)
        ],
        [ #1 아래
            (1, -1, 0.01), (-1, -1, 0.01),
            (1, 0, 0.07), (-1, 0, 0.07),
            (1, 1, 0.1), (-1, 1, 0.1),
            (2, 0, 0.02), (-2, 0, 0.02),
            (0, 2, 0.05)

        ],
        [ #2 오
            (-1, 1, 0.01), (-1, -1, 0.01),
            (0, 1, 0.07), (0, -1, 0.07),
            (1, 1, 0.1), (1, -1, 0.1),
            (0, 2, 0.02), (0, -2, 0.02),
            (2, 0, 0.05)

        ],
        [ #3 위
            (1, 1, 0.01), (-1, 1, 0.01),
            (1, 0, 0.07), (-1, 0, 0.07),
            (1, -1, 0.1), (-1, -1, 0.1),
            (2, 0, 0.02), (-2, 0, 0.02),
            (0, -2, 0.05)

        ],
    ]

    a = pan[y][x]
    for tdx, tdy, r in moov[d]:

        cal = int(pan[y][x]*r)

        nx = x+tdx
        ny = y+tdy

        if -1<nx<N and -1<ny<N:
            pan[ny][nx] += cal
        else:
            ans+=cal
        
        a -= cal

    if -1<y+dy[d]<N and -1<x+dx[d]<N:
        pan[y+dy[d]][x+dx[d]] += a
    else:
        ans+=a

     
    
def start_tornado(x, y):

    # dx = [-1,0, 1, 0]
    # dy = [0,1, 0, -1]

    d = 0
    r = 1
    r_again = 0

    count = 0

    while True:
        
        x = x+dx[d] 
        y = y+dy[d]
    
        # print(x, y, n)

        #x, y, 위치에서 모래 계산 
        cal(x, y, d)

        count +=1
        if count == r:
           count = 0
           d = (d+1)%4
           r_again+=1
        
        if r_again == 2:
            r_again = 0
            r +=1
        
        if x == 0 and y == 0:
            break


N = int(input())
pan = [list(map(int, input().split())) for _ in range(N)]
ans = 0

start_tornado(N//2, N//2)
print(ans)
