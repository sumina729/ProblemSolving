import copy

_move = {
    'F' : #2<->3, 4<->2
        [('U', 2, 'R', 3),
        ('R', 3, 'D', 2), 
        ('D', 2, 'L', 4), 
        ('L', 4, 'U', 2)
    ],


    'B' : [ #1<->3, 1<->4
        ('U', 1, 'L', 3),
        ('L', 3, 'D', 1), 
        ('D', 1, 'R', 4), 
        ('R', 4, 'U', 1)
    ],

    'R' : [#3->3, 4<->3, 4->4
        ('U', 4, 'B', 3),
        ('B', 3, 'D', 3),
        ('D', 3, 'F', 4),
        ('F', 4, 'U', 4)
    ],

    'L' : [ #3->3, 4<->3, 4->4
        ('U', 3, 'F', 3),
        ('F', 3, 'D', 4),
        ('D', 4, 'B', 4),
        ('B', 4, 'U', 3)
    ],

    'U':[ #1->1
        ('F', 1, 'L', 1),
        ('L', 1, 'B', 1),
        ('B', 1, 'R', 1),
        ('R', 1, 'F', 1)
    ],

    'D':[ #2->2
        ('F', 2, 'R', 2),
        ('R', 2, 'B', 2),
        ('B', 2, 'L', 2),
        ('L', 2, 'F', 2)
    ]
}

def move1_1(t_qube, a, b, r): #0 이면 a1 -> b1, 1이면 b1 ->a1 호 상 -> 상
    global qube
    if r == 0:
        qube[b][0] = t_qube[a][0]
    if r == 1:
        qube[a][0] = t_qube[b][0]

def move2_2(t_qube, a, b, r):  #하 -> 하
    global qube
    if r == 0:
        qube[b][2] = t_qube[a][2]
    if r == 1:
        qube[a][2] = t_qube[b][2]

def move3_3(t_qube, a, b, r):  #죄 -> 좌
    global qube
    if r == 0:
        for i in range(3):
            qube[b][i][0] = t_qube[a][i][0]
    if r == 1:
        for i in range(3):
            qube[a][i][0] = t_qube[b][i][0]

def move4_4(t_qube, a, b, r):  #우 ->우
    global qube
    if r == 0:
        for i in range(3):
            qube[b][i][2] = t_qube[a][i][2]
    if r == 1:
        for i in range(3):
            qube[a][i][2] = t_qube[b][i][2]

def move4_3(t_qube, a, b, r):  #우 ->좌, a4->b3
    global qube
    if r == 0:
        for i in range(3): #a4->b3
            qube[b][i][0] = t_qube[a][2-i][2]
    if r == 1:
        for i in range(3): #b3 -> a4
            qube[a][2-i][2] = t_qube[b][i][0]

def move3_4(t_qube, a, b, r):  #우 ->좌, a4->b3
    global qube
    if r == 0:
        for i in range(3): #a3->b4
            qube[b][2-i][2]= t_qube[a][i][0]
    if r == 1:
        for i in range(3): #b4 -> a3
            qube[a][i][0] = t_qube[b][2-i][2]

def move1_3(t_qube, a, b, r):  #상 ->좌
    global qube
    if r == 0:
        for i in range(3): #a3->b4
            qube[b][2-i][0]= t_qube[a][0][i]
    if r == 1:
        for i in range(3): #b4 -> a3
            qube[a][0][i] = t_qube[b][2-i][0]

def move3_1(t_qube, a, b, r):  #상 ->좌
    global qube
    if r == 0:
        for i in range(3): 
            qube[b][0][i]= t_qube[a][2-i][0]
    if r == 1:
        for i in range(3):
            qube[a][2-i][0] = t_qube[b][0][i]

def move1_4(t_qube, a, b, r):  #상 ->우
    global qube
    if r == 0:
        for i in range(3): 
            qube[b][i][2]= t_qube[a][0][i]
    if r == 1:
        for i in range(3): 
            qube[a][0][i] = t_qube[b][i][2]

def move4_1(t_qube, a, b, r):  #우-> 상
    global qube
    if r == 0:
        for i in range(3): 
            qube[b][0][i]= t_qube[a][i][2]
    if r == 1:
        for i in range(3): 
            qube[a][i][2] = t_qube[b][0][i]

def move2_3(t_qube, a, b, r):  #하 ->좌
    global qube
    if r == 0:
        for i in range(3): #a3->b4
            qube[b][i][0]= t_qube[a][2][i]
    if r == 1:
        for i in range(3): #b4 -> a3
            qube[a][2][i] = t_qube[b][i][0]

def move3_2(t_qube, a, b, r):  #좌 ->하
    global qube
    if r == 0:
        for i in range(3): 
            qube[b][2][i]= t_qube[a][i][0]
    if r == 1:
        for i in range(3):
            qube[a][i][0] = t_qube[b][2][i]

def move2_4(t_qube, a, b, r):  #하 ->우
    global qube
    if r == 0:
        for i in range(3): 
            qube[b][i][2]= t_qube[a][2][2-i]
    if r == 1:
        for i in range(3):
            qube[a][2][2-i] = t_qube[b][i][2]

def move4_2(t_qube, a, b, r):  #우->하
    global qube
    if r == 0:
        for i in range(3): 
            qube[b][2][2-i]= t_qube[a][i][2]
    if r == 1:
        for i in range(3):
            qube[a][i][2] = t_qube[b][2][2-i]


def print_f(qube):
    print()
    print()
    print("D")
    for y in range(3):
        print(qube['D'][y])

    print("B")
    for y in range(3):
        print(qube['B'][y])

    print("U")
    for y in range(3):
        print(qube['U'][y])

    print("F")
    for y in range(3):
        print(qube['F'][y])

    print("L")
    for y in range(3):
        print(qube['L'][y])

    print("R")
    for y in range(3):
        print(qube['R'][y])


def move_r(qube_a):
    new_qube_a = [t[:] for t in qube_a]

    for y in range(3):
        for x in range(3):
            new_qube_a[x][2-y] = qube_a[y][x]

    return new_qube_a

def move_l(qube_a):
    new_qube_a = [t[:] for t in qube_a]

    for y in range(3):
        for x in range(3):
            new_qube_a[2-x][y] = qube_a[y][x]
            
    return new_qube_a


T = int(input())
# N = int(input())
# m_c_list = list(input().split())
# print(m_c_list)
# print_f(qube)

for _ in range(T):
    qube = {
        'F': [['r', 'r', 'r'], 
            ['r', 'r', 'r'], 
            ['r', 'r', 'r']],

        'B': [['o', 'o', 'o'], 
            ['o', 'o', 'o'], 
            ['o', 'o', 'o']],

        'L': [['g', 'g', 'g'], 
            ['g', 'g', 'g'], 
            ['g', 'g', 'g']],

        'R': [['b', 'b', 'b'], 
            ['b', 'b', 'b'], 
            ['b', 'b', 'b']],

        'U': [['w', 'w', 'w'], 
            ['w', 'w', 'w'], 
            ['w', 'w', 'w']],

        'D': [['y', 'y', 'y'], 
            ['y', 'y', 'y'], 
            ['y', 'y', 'y']]
    }

    N = int(input())
    m_c_list = list(input().split())


    for q in range(N):
        m_c = m_c_list[q]
        # print(m_c[0], m_c[1])
        move_list = _move[m_c[0]]
        if m_c[1] == '+':
            c = 0 #0-> 시계 1, 반시계
            qube[m_c[0]] = move_r(qube[m_c[0]])
        else:
            c = 1
            qube[m_c[0]] = move_l(qube[m_c[0]])

        # 앞편 돌리기
        

        t_qube = copy.deepcopy(qube)
        for m_list in move_list:
            a, an, b, bn = m_list


            #옆면 돌리기
            if an == 1 and bn== 1:
                move1_1(t_qube, a, b, c)

            elif an == 2 and bn== 2:
                move2_2(t_qube, a, b, c)

            elif an == 3 and bn== 3:
                move3_3(t_qube, a, b, c)
            
            elif an == 4 and bn== 4:
                move4_4(t_qube, a, b, c)

            elif an == 4 and bn== 3:
                move4_3(t_qube, a, b, c)

            elif an == 3 and bn== 4:
                move3_4(t_qube, a, b, c)
            
            elif an == 1 and bn== 3:
                move1_3(t_qube, a, b, c)
            
            elif an == 3 and bn== 1:
                move3_1(t_qube, a, b, c)
            
            elif an == 1 and bn== 4:
                move1_4(t_qube, a, b, c)
            
            elif an == 4 and bn== 1:
                move4_1(t_qube, a, b, c)
            
            elif an == 2 and bn== 3:
                move2_3(t_qube, a, b, c)

            elif an == 3 and bn== 2:
                move3_2(t_qube, a, b, c)
            
            elif an == 2 and bn== 4:
                move2_4(t_qube, a, b, c)
            
            elif an == 4 and bn== 2:
                move4_2(t_qube, a, b, c)



            # print(a, b)
            # print_f(qube)
    for y in range(3):
        for x in range(3):
            print(qube['U'][y][x], end="")
        print()
