from collections import deque

sp, ep = map(int, input().split()) 
point_visited = [-1 for _ in range(100001)]
point_prv = [-1 for _ in range(100001)]

if sp == ep:
    print(0)
    print(sp)
    exit()
    
que = deque()
que.append(sp)
point_visited[sp] = 0

while que:
    cp = que.popleft()

    np_list = []
    np_list.append(cp-1)
    np_list.append(cp+1)
    np_list.append(cp*2)

    for np in np_list:
        if -1<np<100001 and point_visited[np] == -1:
            
            point_prv[np] = cp
            que.append(np)
            point_visited[np] = point_visited[cp]+1

            if np == ep:
                print(point_visited[np])
                
                paint_list = []
                paint_list.append(ep)

                while True:
                    if ep == sp:
                        paint_list.reverse()
                        print(*paint_list)
                        break
                    
                    ep = point_prv[ep]
                    paint_list.append(ep)

                break

# print(point_visited[0:19])
# print(point_prv[0:19])
