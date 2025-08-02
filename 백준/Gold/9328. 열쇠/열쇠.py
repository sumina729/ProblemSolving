'''
상근이는 1층 빌딩에 침입해 매우 중요한 문서를 훔쳐오려고 한다. 
상근이가 가지고 있는 평면도에는 문서의 위치가 모두 나타나 있다. 
빌딩의 문은 모두 잠겨있기 때문에, 문을 열려면 열쇠가 필요하다. 
상근이는 일부 열쇠를 이미 가지고 있고, 일부 열쇠는 빌딩의 바닥에 놓여져 있다. 
상근이는 상하좌우로만 이동할 수 있다.

상근이가 훔칠 수 있는 문서의 최대 개수를 구하는 프로그램을 작성하시오.

.'는 빈 공간을 나타낸다.
'*'는 벽을 나타내며, 상근이는 벽을 통과할 수 없다.
'$'는 상근이가 훔쳐야하는 문서이다.
알파벳 대문자는 문을 나타낸다.
알파벳 소문자는 열쇠를 나타내며, 
그 문자의 대문자인 모든 문을 열 수 있다.

'''

from collections import deque

def is_in_pan(y, x):
    global H, W

    if -1<y<H and -1<x<W:
        return True
    
    return False


dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

T = int(input())

for _ in range(T):


    H, W = map(int, input().split())

    pan = [list(input().strip()) for _ in range(H)]
    my_key = list(input().strip())

    ans = 0

    if my_key[0] == '0':
        my_key = set()
    else:
        my_key = set(my_key)          


    que = deque()
    visited = [[0 for _ in range(W)]for _ in range(H)]

    rock_door = {chr(i): [] for i in range(ord('A'), ord('Z')+1)}
            

    for y in range(H):
        for x in range(W):
            if y == 0 or y == H-1 or x == 0 or x == W-1 :
                if not pan[y][x] == '*':
                    if pan[y][x].isupper(): # 대문자
                        if pan[y][x].lower() in my_key: # 키 있으면 
                            que.append([y, x])
                            visited[y][x] = 1
                        else:
                            rock_door[pan[y][x]].append([y, x])
                            # print("잠겨있는 문: ", rock_door, pan[ny][nx])
                    

                    else:
                        que.append([y, x])
                        visited[y][x] = 1

                        if pan[y][x] == '$': # 서류이면
                            ans+=1

                        if pan[y][x].islower(): #소문자
                            my_key.add(pan[y][x])
                            # print("현재키: ", my_key)
                            if len(rock_door[pan[y][x].upper()]) > 0:
                                # print(pan[ny][nx], len(rock_door[pan[ny][nx].upper()]), "키 구해서 문열어야함")
                                
                                for l in range(len(rock_door[pan[y][x].upper()])):
                                    tmp = rock_door[pan[y][x].upper()][l]
                                    
                                    que.append(tmp)
                                    visited[tmp[0]][tmp[1]] = 1


                            #새로운 키를 얻었을떄 


    # print(my_key)
    # print(que)

    while que:
        cy, cx = que.popleft()

        for i in range(4):
            ny = cy+dy[i]
            nx = cx+dx[i]

            if is_in_pan(ny, nx) and not pan[ny][nx] == '*' and visited[ny][nx] == 0: # 벽 아니면

                if pan[ny][nx].isupper(): # 대문자
                    if pan[ny][nx].lower() in my_key: # 키 있으면 
                        que.append([ny, nx])
                        visited[ny][nx] = 1
                    else:
                        rock_door[pan[ny][nx]].append([ny, nx])
                        # print("잠겨있는 문: ", rock_door, pan[ny][nx])
                    

                else:
                    que.append([ny, nx])
                    visited[ny][nx] = 1

                    if pan[ny][nx] == '$': # 서류이면
                        ans+=1

                    if pan[ny][nx].islower(): #소문자
                        my_key.add(pan[ny][nx])
                        # print("현재키: ", my_key)
                        if len(rock_door[pan[ny][nx].upper()]) > 0:
                            # print(pan[ny][nx], len(rock_door[pan[ny][nx].upper()]), "키 구해서 문열어야함")
                            
                            for l in range(len(rock_door[pan[ny][nx].upper()])):
                                tmp = rock_door[pan[ny][nx].upper()][l]
                                
                                que.append(tmp)
                                visited[tmp[0]][tmp[1]] = 1


                        #새로운 키를 얻었을떄

    # for v in visited:
    #     print(v)

    # print(rock_door)
    print(ans)
                        