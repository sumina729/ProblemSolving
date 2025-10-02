N = int(input())
N_list = list(map(int, input().split()))

M = int(input())
M_list = list(map(int, input().split()))

N_list.sort(key = lambda a: -a)
M_list.sort(key = lambda a: -a)

# print(N_list)
# print(M_list)


ans = 0
while True:
    go_list = [] 
    for n in N_list: #50
        for i in range(len(M_list)): #10000
            # print(n, M_list[i])
            if M_list[i] <= n:
                go_list.append(M_list[i])
                M_list.pop(i)
                break
        
    if len(M_list) == 0:
        print(ans+1)
        break
    
    if len(go_list) == 0:
        print(-1)
        break

    ans+=1
    # print("====", ans, "====")
    # print(go_list)
    # print(M_list)
    # print("===============")
