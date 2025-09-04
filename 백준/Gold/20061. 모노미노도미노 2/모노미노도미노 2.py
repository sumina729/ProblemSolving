K = int(input())
B = [ list(map(int, input().split())) for _ in range(K)]

block = [
    [],
    [[0, 0], [0, 0]],
    [[0, 0], [0, 1]], #가로로 긴거
    [[0, 0], [1, 0]] #새로로 긴거
]

B_PAN = [[0 for _ in range(6)] for _ in range(4)]
G_PAN = [[0 for _ in range(4)] for _ in range(6)]

def set_pan(pi, bt, sy, sx):


    if pi == 'G': 
        sy = 0
        sx = sx

        y1, x1 = block[bt][0][0]+sy, block[bt][0][1]+sx
        y2, x2 = block[bt][1][0]+sy, block[bt][1][1]+sx

        #밑으로 이동
        while True:       
            
            if y1+1 > 5 or y2+1 > 5 or G_PAN[y1+1][x1] == 1 or G_PAN[y2+1][x2]:
                break
            
            #y이동
            y1 +=1
            y2 +=1

        G_PAN[y1][x1] =1
        G_PAN[y2][x2] =1

    if pi == 'B':
        sy = sy
        sx = 0

        y1, x1 = block[bt][0][0]+sy, block[bt][0][1]+sx
        y2, x2 = block[bt][1][0]+sy, block[bt][1][1]+sx

        #옆으로 이동
        while True:       
            
            if x1+1 > 5 or x2+1 > 5 or B_PAN[y1][x1+1] == 1 or B_PAN[y2][x2+1] == 1:
                break
            
            #x이동
            x1 +=1
            x2 +=1

        B_PAN[y1][x1] =1
        B_PAN[y2][x2] =1


def move_pan(pi, i):
    if pi == 'G':
        G_PAN[i][0] = G_PAN[i][1] = G_PAN[i][2] = G_PAN[i][3] = 0

        #아래로 으로 당기기
        for y in range(i, -1, -1):
            for x in range(4):
                if y-1 < 0:
                    G_PAN[y][x] = 0
                else:
                    G_PAN[y][x] = G_PAN[y-1][x]
    
    elif pi == 'B':
        B_PAN[0][i] = B_PAN[1][i] = B_PAN[2][i] = B_PAN[3][i] = 0

        for x in range(i, -1, -1):
            for y in range(4):
                # print(">",y, x)
                if x-1 < 0:
                    B_PAN[y][x] = 0
                else:
                    B_PAN[y][x] = B_PAN[y][x-1]
                
        
def get_jumsu(pi):
    jumsu = 0
    for i in range(6):

        if pi == 'G':
            s = G_PAN[i][0]+G_PAN[i][1]+G_PAN[i][2]+G_PAN[i][3]
            if s == 4: # 꽉차있으면
                jumsu +=1

                move_pan(pi, i)


        
        elif pi == 'B':
            s = B_PAN[0][i]+B_PAN[1][i]+B_PAN[2][i]+B_PAN[3][i]
            if s == 4: # 꽉차있으면
                jumsu +=1

                move_pan(pi, i)
        
    return jumsu
                

def start_game(pi, bt, sy, sx):
    jumsu = 0
    #판에 두기
    set_pan(pi, bt, sy, sx)

    #점수체크하기
    jumsu += get_jumsu(pi)

    #특별칸확인
    if pi == 'G':
        s1 = G_PAN[0][0]+G_PAN[0][1]+G_PAN[0][2]+G_PAN[0][3]
        s2 = G_PAN[1][0]+G_PAN[1][1]+G_PAN[1][2]+G_PAN[1][3]

        if s1 > 0:
            move_pan(pi, 4)
            move_pan(pi, 5)
        elif s2 > 0:
            move_pan(pi, 5)
    
    elif pi =='B':
        s1 = B_PAN[0][0]+B_PAN[1][0]+B_PAN[2][0]+B_PAN[3][0]
        s2 = B_PAN[0][1]+B_PAN[1][1]+B_PAN[2][1]+B_PAN[3][1]
        # print(s1, s2)
        if s1 > 0:
            move_pan(pi, 4)
            move_pan(pi, 5)
        elif s2 > 0:
            move_pan(pi, 5)

    return jumsu


ans = 0
for bt, by, bx in B:

    ans += start_game("G", bt, by, bx)
    ans += start_game("B", bt, by, bx)


print(ans)
print(sum(sum(b)for b in B_PAN)+sum(sum(g)for g in G_PAN ))
