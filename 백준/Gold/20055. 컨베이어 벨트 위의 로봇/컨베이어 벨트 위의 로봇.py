'''
벨트가 한 칸 회전하면 1번부터 2N-1번까지의 칸은 다음 번호의 칸이 있는 위치로 이동하고, 2N번 칸은 1번 칸의 위치로 이동한다. i번 칸의 내구도는 Ai이다. 위의 그림에서 1번 칸이 있는 위치를 "올리는 위치", N번 칸이 있는 위치를 "내리는 위치"라고 한다.

컨베이어 벨트에 박스 모양 로봇을 하나씩 올리려고 한다. 로봇은 올리는 위치에만 올릴 수 있다. 언제든지 로봇이 내리는 위치에 도달하면 그 즉시 내린다. 로봇은 컨베이어 벨트 위에서 스스로 이동할 수 있다. 로봇을 올리는 위치에 올리거나 로봇이 어떤 칸으로 이동하면 그 칸의 내구도는 즉시 1만큼 감소한다.

컨베이어 벨트를 이용해 로봇들을 건너편으로 옮기려고 한다. 로봇을 옮기는 과정에서는 아래와 같은 일이 순서대로 일어난다.

벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
종료되었을 때 몇 번째 단계가 진행 중이었는지 구해보자. 가장 처음 수행되는 단계는 1번째 단계이다.

'''

def rotate_a_list(a_list, N):
    return [a_list[-1]] + a_list[:-1]

def rotate_r_list(r_list, N):
    new_list = [0 for _ in range(N)]
    for i in range(N-1, 0, -1):
        new_list[i] = r_list[i-1]

    new_list[0] = 0
    new_list[N-1] = 0 # N번쨰 오면 바로 내리기

    return new_list

def move_r_list(r_list, a_list, N):
    for i in range(N-2, -1, -1):
        if r_list[i] == 1 and r_list[i+1] == 0 and a_list[i+1] > 0:
            r_list[i+1] = r_list[i] # 로봇이동
            r_list[i] = 0
            a_list[i+1]-=1 # 내구성 감소

    r_list[N-1] = 0 # N번쨰 오면 바로 내리기

    return r_list, a_list

def cnt_0(a_list):
    return a_list.count(0)

N, K = map(int, input().split())
a_list =list(map(int, input().split()))
r_list = [0 for _ in range(N)]

# N = 100
# K = 200
# a_list = [1000] * (2 * N)
# r_list = [0 for _ in range(N)]

# print(a_list)
# print(r_list)

turn = 0
while True:
    turn +=1

    #벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전
    a_list = rotate_a_list(a_list, N) 
    r_list = rotate_r_list(r_list, N) 
    # print()
    # print('벨트 회전')
    # print(a_list)
    # print(r_list)

    r_list, a_list = move_r_list(r_list, a_list, N) 
    # print()
    # print('로봇 이동')
    # print(a_list)
    # print(r_list)

    if a_list[0] > 0:
        r_list[0] = 1
        a_list[0]-=1
    
    # print()
    # print('새로운 로봇올리기')
    # print(a_list)
    # print(r_list)

    ans = cnt_0(a_list)
    # print(ans, K)
    
    if ans >= K:
        print(turn)
        break

    # break




    