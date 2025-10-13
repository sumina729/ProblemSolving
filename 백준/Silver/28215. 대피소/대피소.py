from itertools import permutations, combinations

N, K = map(int, input().split())
home_list = [list(map(int, input().split())) for _ in range(N)]

dit_com = combinations(home_list, K)

ans = 10000*10000
for dit in dit_com:

    # print("조합", dit)

    max_len = 0
    for h in home_list:

        h_min_l = 10000*10000
        for d in dit: #각 점에서 길이
            l = abs(d[0]-h[0]) + abs(d[1]-h[1])
            h_min_l = min(l, h_min_l)
        # print(h, h_min_l)
        
        max_len = max(h_min_l, max_len)

    # print(max_len)
    ans = min(ans, max_len)
    # break
print(ans)
