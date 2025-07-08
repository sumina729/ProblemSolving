'''
RGB거리에는 집이 N개 있다. 
거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.

집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 
각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 
아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

1번 집의 색은 2번, N번 집의 색과 같지 않아야 한다.
N번 집의 색은 N-1번, 1번 집의 색과 같지 않아야 한다.
i(2 ≤ i ≤ N-1)번 집의 색은 i-1, i+1번 집의 색과 같지 않아야 한다.


'''

import math
def RGB_n_c(i, RGB_list, no_n1, no_n2):
    RGB_tmp = RGB_list[i]

    min_n = math.inf
    c = -1
    for j in range(3):
        if no_n1 == j or no_n2 == j:
            continue
        if RGB_tmp[j] < min_n:
            min_n = RGB_tmp[j]
            c = j

    return min_n, c

def det_dp(N, dp, RGB_list, no_n2):
    
    for i in range(2, N):
        f1 = dp[i-1][0] #이전꺼중에 작은거 
        f2 = dp[i-1][1] #이전꺼중에 큰거
        # print("f1, f2", f1, f2)
        if i == N-1:
            # print(f1[1], no_n2)
    
            cn1, cc1 = RGB_n_c(i, RGB_list, f1[1], no_n2)
            cn2, cc2 = RGB_n_c(i, RGB_list, f2[1], no_n2)

            n1 = f1[0]+cn1
            n2 = f2[0]+cn2

            if n1 < n2:
                return n1
            else:
                return n2

        else:
            t_l = []
            cn1, cc1 = RGB_n_c(i, RGB_list, f1[1], -1) #작은거랑 가장 작은거
            cn2, cc2 = RGB_n_c(i, RGB_list, f2[1], -1) #두번째 작은거랑 가장 작은거
            cn3, cc3 = RGB_n_c(i, RGB_list, f1[1], cc1)
            cn4, cc4 = RGB_n_c(i, RGB_list, f2[1], cc2)

            # print(cn1, f1[0])
            # print(cn2, f2[0])
            # print(cn3, f1[0])
            # print(cn4, f2[0])
            t_l.append([cn1+f1[0], cc1])
            t_l.append([cn2+f2[0], cc2])
            t_l.append([cn3+f1[0], cc3])
            t_l.append([cn4+f2[0], cc4])
            
            
            t_l.sort(key = lambda a: -a[0])

            # print(t_l, t_l[-1])
            # print(t_l, t_l[-2])
            mn1 = t_l[-1]
            mn2 = t_l[-2]
            if mn2[1] == mn1[1]:
                mn2 = t_l[-3]
            

            dp[i][0] = [mn1[0], mn1[1]]
            dp[i][1] = [mn2[0], mn2[1]]

            # print("=>", dp[i], no_n2)

            



        # print(n1, cc1)
        # print(n2, cc2)

        # if n1 < n2:
        #     dp[i][0] = [n1, cc1]
        #     dp[i][1] = [n2, cc2]
        # else:
        #     dp[i][0] = [n2, cc2]
        #     dp[i][1] = [n1, cc1]

        

        # break
    return min(dp[N-1][0][0], dp[N-1][1][0])
    
N = int(input())
RGB_list = [list(map(int, input().split())) for _ in range(N)]

# print(N)
# print(RGB_list)


ans = [] 
for i in range(3):
    dp = [ [[0, 0], [0, 0]] for _ in range(N)]

    dp[0][0] = [RGB_list[0][i], i]
    dp[0][1] = [RGB_list[0][i], i]

    n1 = dp[0][0][0] + RGB_list[1][(i+1)%3]
    n2 = dp[0][1][0] + RGB_list[1][(i+2)%3]

    # print("=====")
    # print(n1, (i+1)%3)
    # print(n2, (i+2)%3)
    if n1<n2:
        dp[1][0] = [n1, (i+1)%3]
        dp[1][1] = [n2, (i+2)%3]
    else:
        dp[1][0] = [n2, (i+2)%3]
        dp[1][1] = [n1, (i+1)%3]

    # print(dp)
    
    # print()
    # print()
    # print("===================")
    ans.append(det_dp(N, dp, RGB_list, i))
    # print(ans)
    # break

print(min(ans))



