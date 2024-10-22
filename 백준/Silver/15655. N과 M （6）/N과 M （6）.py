N, M = map(int, input().split())
n_list = list(map(int, input().split()))
up_list = []

def back(n):
    if n == M:
        print(*up_list)
        return
    
    for i in range(N):
        if n == 0:
            up_list.append(n_list[i])
            back(n+1)
            up_list.pop()

        elif up_list[-1] < n_list[i]:
            up_list.append(n_list[i])
            back(n+1)
            up_list.pop()

n_list.sort()
# print(n_list)
back(0)