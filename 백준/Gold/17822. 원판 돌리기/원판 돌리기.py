'''
번호가 xi의 배수인 원판을 di방향으로 ki칸 회전시킨다. di가 0인 경우는 시계 방향, 1인 경우는 반시계 방향이다.

1. 원판에 수가 남아 있으면, 인접하면서 수가 같은 것을 모두 찾는다.
2. 그러한 수가 있는 경우에는 원판에서 인접하면서 같은 수를 모두 지운다.
3. 없는 경우에는 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수에서 1을 빼고, 작은 수에는 1을 더한다.

원판을 T번 회전시킨 후 원판에 적힌 수의 합을 구해보자.
'''

def get_rotate_pan(one_pan_n, di, ki, M):
    # if di == 0: md = 1*ki
    # else: md = -1*ki

    
    if di == 0:
        # print("시계방향", ki, "칸")
        return one_pan_n[M-ki:M]+one_pan_n[0:M-ki]
    else:
        # print("반시계방향", ki, "칸")
        return one_pan_n[ki:M]+one_pan_n[0:ki]

def remove_num(one_pan, one_pan_tmp, num, N, n, m):
    is_get = False

    if one_pan[n][(m+1)%M] == num:
        one_pan_tmp[n][(m+1)%M] = 0
        is_get = True

    if one_pan[n][m-1] == num:
        one_pan_tmp[n][m-1] = 0
        is_get = True

    if n+1 < N and one_pan[n+1][m] == num:
        one_pan_tmp[n+1][m] = 0
        is_get = True
    
    if n-1 > -1 and one_pan[n-1][m] == num:
        one_pan_tmp[n-1][m] = 0
        is_get = True

    return is_get


def remove_adjust(one_pan, N, M):
    one_pan_tmp = [one_pan[n][:] for n in range(N)]
    # print(one_pan_tmp)
    is_get = False

    for n in range(N):
        for m in range(M):
            # print(n, m, one_pan_tmp[n][m])
            if not one_pan_tmp[n][m] == 0:
                
                if remove_num(one_pan, one_pan_tmp, one_pan[n][m], N, n, m):
                    # print(n, m, "와 인접한거 지우기")
                    one_pan_tmp[n][m] = 0
                    is_get = True
                    # for i in range(N):
                    #     print(one_pan_tmp[i])
    
    return is_get, one_pan_tmp


def cumput_pan(one_pan, N, M):
    cnt = 0
    p_sum = 0 
    for n in range(N):
        for m in range(M):
            if not one_pan[n][m] == 0:
                cnt+=1
                p_sum += one_pan[n][m]
    
    return p_sum, cnt

N, M, T = map(int, input().split()) # 지름, 판 안에 워소 개수
one_pan = [list(map(int, input().split())) for _ in range(N)] #0번~N-1번 판
t_list = [list(map(int, input().split())) for _ in range(T)] 


for xi, di, ki in t_list:

    #판 회전하기
    for n in range(N):
        if (n+1)%xi == 0:
            # print()
            # print(n+1,"번 판 회전:",one_pan[n])
            one_pan[n] = get_rotate_pan(one_pan[n], di, ki, M)
            # print("회전완료", one_pan[n])
    

    #인접한 같은 수 지우기
    is_ok, one_pan = remove_adjust(one_pan, N, M)
    if not is_ok:

        pan_sum, pan_cnt = cumput_pan(one_pan, N, M)
        if not pan_cnt == 0:
            mean = pan_sum/pan_cnt

            for n in range(N):
                for m in range(M):
                    if not one_pan[n][m] == 0:
                        if one_pan[n][m] > mean:
                            one_pan[n][m]-=1
                        elif one_pan[n][m] < mean:
                            one_pan[n][m]+=1
                    
    # print()
    # for n in range(N):
    #     print(one_pan[n])

ans = 0
for n in range(N):
    ans +=sum(one_pan[n])

print(ans)


    # break
