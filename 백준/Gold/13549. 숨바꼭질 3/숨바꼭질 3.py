from collections import deque

sp, ep = map(int, input().split()) 
point_visited = [-1 for _ in range(100001)]
point_prv = [-1 for _ in range(100001)]

if sp == ep:
    print(0)
    exit()

que = deque()
que.append(sp)
point_visited[sp] = 0

while que:
    cp = que.popleft()

    np = cp
    while True:
        np = np*2

        if -1<np<100001 and point_visited[np] == -1:
            que.append(np)
            point_visited[np] = point_visited[cp]

            if np == ep:
                print(point_visited[np])
                # print(point_visited[0:21])
                exit()
        else:
            break
    
    np_list = []
    np_list.append(cp-1)
    np_list.append(cp+1)

    for np in np_list:
        if -1<np<100001 and point_visited[np] == -1:
            
            que.append(np)
            point_visited[np] = point_visited[cp]+1

            if np == ep:
                print(point_visited[np])
                # print(point_visited[0:21])
                exit()

                break
    # break
